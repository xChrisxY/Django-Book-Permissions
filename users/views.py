from .models import UserModel
from .serializer import UserSerializer, LoginSerializer
from rest_framework import status, viewsets
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer 

    def create(self, request, *args, **kwargs):
        return Response(
            {"detail": "Please use the register endpoint to create a user."},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # [+] Definimos una acción personalizada para el registro de usuarios
    @action(detail=False, methods=['post'])
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
    
        username = serializers.CharField()
    # [+] Acción personalizada para el login de usuarios
    @action(detail=False, methods=['post'])
    def login(self, request):
        
        serializer = LoginSerializer(request.data)

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
        