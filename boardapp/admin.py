from django.contrib import admin
from .models import BoardModel
# Register your models here.

# <管理画面のところで読み込ませないと表示できない>
admin.site.register(BoardModel)
