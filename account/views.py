from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from account.serializers import RegisterSerializer,LoginSerializer
from rest_framework import status
from django.contrib.auth.models import authenticate
from rest_framework.authtoken.models import Token

class LoginAPI(APIView):
    def post(self,request):
        data=request.data
        serializer=LoginSerializer(data=data)
        if not serializer.is_valid():
            return Response({
                'status':False,
                'message':serializer.errors
            },status.HTTP_400_BAD_REQUEST)
        
        user=authenticate(username=serializer.data['username'], password=serializer.data['password'])
        token, _=Token.objects.get_or_create(user=user)
        
        return Response({'status':True, 'message':'user login', 'token': str(token)},status.HTTP_201_CREATED)



class Resgisteruser(APIView):
    def post(self, request):
        data=request.data
        serializer=RegisterSerializer(data=data)

        if not serializer.is_valid():
            return Response({
                'status':False,
                'message':serializer.errors
            },status.HTTP_400_BAD_REQUEST)
        
        serializer.save()

        return Response({'status':True, 'message':'User Created'},status.HTTP_201_CREATED)
    



