from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from .models import Post
from .models import Track, Lesson, Comment

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = UserAdmin.list_display + ('is_teacher',)
    fieldsets = UserAdmin.fieldsets + (
        (None, {
            'fields': ('is_teacher','completedlessons',),
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Post)
admin.site.register(Track)
admin.site.register(Lesson)
admin.site.register(Comment)

