from rest_framework.decorators import api_view
from .serializers import UserLoginValidateSerializer, UserCreateValidateSerializer, UserConfirmValidateSerializer, UserLoginSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import Confirm
from rest_framework.views import APIView


class AuthorizationApiView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer
        serializer.is_valid(raise_exception=True)
        username = request.data.get("username")
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response(data={'key': token.key})
        return Response(status=status.HTTP_401_UNAUTHORIZED, data={'errors': 'Username osr password wrong!'})




@api_view(['POST'])
def registration_api_view(request):
    serializer = UserCreateValidateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = User.objects.create_user(**serializer.validated_data, is_active=False)
    return Response(data={'user_id': user.id},
                    status=status.HTTP_201_CREATED)

@api_view(['POST'])
def confirmation_api_view(request):
    serializer = UserConfirmValidateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    if Confirm.objects.filter(user_ptr_id=request.data['user_id'], code=request.data['code']):
        User.objects.update(is_active=True)
        return Response(status=status.HTTP_202_ACCEPTED,
                        data={'code': 'confirmed'})
    return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                    data={'error': 'not correct id or code'})