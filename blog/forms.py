from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from .models import Post, Track, Lesson, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class TrackForm(forms.ModelForm):

    class Meta:
        model = Track
        fields = ('title', 'introduction','lessons',)


class LessonForm(forms.ModelForm):

    class Meta:
        model = Lesson
        fields = ('title', 'source','introduction', 'published_date')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'is_teacher', 'completedlessons')



class CustomUserCreationForm(UserCreationForm):
    is_teacher = forms.BooleanField(required=False)


    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'is_teacher')

