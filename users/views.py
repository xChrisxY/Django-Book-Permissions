from .models import UserModel
from .serializer import UserSerializer, LoginSerializer, PasswordSerializer
from rest_framework import status, viewsets
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer 
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        return Response(
            {"detail": "Please use the register endpoint to create a user."},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # [+] Definimos una acción personalizada para el registro de usuarios
    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def register(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(serializer.validated_data['password'])
            user.save()

            refresh = RefreshToken.for_user(user)
            return Response({
                'message' : 'User registered succesfully',
                'access_token' : str(refresh.access_token),
                'refresh_token' : str(refresh)
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # [+] Acción personalizada para el login de usuarios
    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def login(self, request):
        
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = UserModel.objects.filter(username=username).first()
            if user is None or not user.check_password(password):
                return Response(
                    {'error' : 'Invalid credentials'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # [+] Creamos el JWT para el usuario
            refresh = RefreshToken.for_user(user)
            return Response({
                'access_token' : str(refresh.access_token),
                'refresh_token' : str(refresh)
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # [+] Acción personalizada para cambiar contraseña
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def change_password(self, request, pk=None):
        user = self.get_object()
        serializer = PasswordSerializer(data=request.data)

        if serializer.is_valid():
            current_password = serializer.validated_data['current_password']
            new_password = serializer.validated_data['new_password']

            if not current_password or not new_password:
                return Response(
                    {"error": "Both current_password and new_password are required."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            if not user.check_password(current_password):
                return Response(
                    {"error": "Current password is incorrent"},
                    status=status.HTTP_400_BAD_REQUEST
                )
                
            user.set_password(new_password)
            user.save()

            return Response(
                {"message": "Password updated succesfully"},
                status=status.HTTP_200_OK
            )


    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated])
    def create_admin(self, request):

        if not request.user.admin:
            return Response(
                {'error': 'You do not have permission to perform this action.'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        
        serializer = UserSerializer(request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(serializer.validated_data['password'])
            user.admin = True 
            user.save()

            return Response(
                {'message': 'Admin user created succesfully.'},
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        