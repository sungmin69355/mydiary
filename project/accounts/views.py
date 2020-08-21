from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth #내부 유저모델 사용
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required

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
##비밀번호 변경란 수정중....

def change_pw(request):
    return render(request, "change_pw.html")

"""
@login_required
def change_password(request):
    context= {}
    if request.method == "POST":
        current_password = request.POST.get("origin_password")
        user = request.user
        if check_password(current_password,user.password):
            new_password = request.POST.get("password1")
            password_confirm = request.POST.get("password2")
            if new_password == password_confirm:
                user.set_password(new_password)
                user.save()
                auth.login(request,user)
                return redirect("home")
            else:
                context.update({'error':"새로운 비밀번호를 다시 확인해주세요."})
    else:
        context.update({'error':"현재 비밀번호가 일치하지 않습니다."})

    return render(request, "change_pw.html",context)
"""
