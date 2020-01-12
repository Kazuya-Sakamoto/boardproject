from django.contrib import admin
from django.urls import path, include
from django.conf import settings #画像の設定
from django.conf.urls.static import static #画像の設定

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('boardapp.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#画像の設定 #css読み込み