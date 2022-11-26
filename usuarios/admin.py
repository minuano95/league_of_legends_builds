from django.contrib import admin
from .models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ('id', 'username', 'email', 'is_superuser')

    def id(self, obj):
        return obj.user.id


admin.site.register(User, UserAdmin)
