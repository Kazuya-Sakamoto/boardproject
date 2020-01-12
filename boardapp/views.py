from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.

def signupfunc(request):
    # <get method を使って取り出す>
    # user2 = User.objects.get(username='aaa')
    # print(user2.email)
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        try:
            User.objects.get(username=username2)
            return render(request, 'signup.html', {'error': 'このユーザーは登録されています'})
        except:
            # <model = User table >
            user = User.objects.create_user(username2, '', password2)
            return render(request, 'signup.html', {'some': 100})
    return render(request, 'signup.html', {'some': 100})