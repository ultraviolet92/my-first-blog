from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)



class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')



class CustomUserCreationForm(UserCreationForm):
    is_student = forms.BooleanField(required=False)


    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'is_student')

