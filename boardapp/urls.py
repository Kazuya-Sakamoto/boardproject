from django.urls import path 
from .views import signupfunc, loginfunc, listfunc
from django.conf import settings #画像の設定
from django.conf.urls.static import static #画像の設定

urlpatterns = [
    path('signup', signupfunc, name='signup'),
    path('login', loginfunc, name='login'),
    path('list/', listfunc),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #画像の設定
