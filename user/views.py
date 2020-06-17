import json
import bcrypt
import jwt

from Westar2.settings import SECRET_KEY

from django.views import View
from django.http import JsonResponse, HttpResponse
from .models import Account
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name = "dispatch")
class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)
        try :
            if Account.objects.filter(email = data['email']).exists(): # 존재하는 이메일인지 확인
                print("혹시 여기타니?")
                return HttpResponse(status=400)

            # 비밀번호 암호화
            password = data['password'].encode('utf-8')
            password_bcrypt = bcrypt.hashpw(password, bcrypt.gensalt())
            password = password_bcrypt.decode('utf-8')

            Account(
                email = data['email'],
                password = password
            ).save()
            return HttpResponse(status=200) 
        except KeyError:
            return JsonResponse({"message":"INVALID_KEYS"}, status = 400)

@method_decorator(csrf_exempt, name = "dispatch")
class SignInView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if Account.objects.filter(id = data['id']).exists():
                user = Account.objects.get(id = data['id'])
                print(user)
                if bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')) == True:
                    token = jwt.encode({'id': user.id}, SECRET_KEY, algorithm="HS256")
                    token = token.decode('utf-8')
                    print("제발 여기타라")
                    return JsonResponse({"token": token}, status =200)
                return HttpResponse(status = 401)

            return HttpResponse(status ==400)
        except KeyError:
            return JsonResponse({"message": "INVALID KEY"}, status = 400 )

class TokenCheckView(View):
    def post(self,request):
        data = json.loads(request.body)

        user_token_info = jwt.decode(data['token'], SECRET_KEY, algorithm = 'HS256')

        if Account.objects.filter(email=user_token_info['email']).exists() :
            return HttpResponse(status=200)

        return HttpResponse(status=403)