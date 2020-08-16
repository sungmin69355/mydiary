from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth #내부 유저모델 사용

def signup(request):
    if request.method  == 'POST':
        if User.objects.filter(username=request.POST['username']).exists(): #아이디 중복 체크 
            return render(request, 'signup_error.html')
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                request.POST['username'], password= request.POST['password1'])
        auth.login(request, user)
        return redirect('home')
    return render(request, 'signup.html')

def login(request):
    if request.method  == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password= password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': '아이디 또는 비밀번호를 확인해주세요'})
    else:
        return render(request, 'login.html')

def logout_request(request):
    auth.logout(request)
    return redirect('/')
    return render(request, 'login.html')   

def kakao_login(request):
    app_rest_api_key = os.environ.get("KAKAO_REST_API_KEY")
    redirect_uri = main_domain + "users/login/kakao/callback"
    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={'45f14f583e184b0b0b976cf5ef4b3095'}&redirect_uri={'home'}&response_type=code"
    )