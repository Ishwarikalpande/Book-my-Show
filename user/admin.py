from django.contrib import admin
from .models import Theatre
from .models import User
from .models import User1
from .models import User2


admin.site.register(Theatre)

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'movie', 'theatre', 'date', 'time')

@admin.register(User1)
class UserAdmin1(admin.ModelAdmin):
    list_display = ('name', 'email', 'message','contact')

@admin.register(User2)
class UserAdmin2(admin.ModelAdmin):
    list_display = ('name', 'email', 'user_name', 'password')