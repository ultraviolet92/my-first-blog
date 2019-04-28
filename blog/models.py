from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone



class CustomUser(AbstractUser):
    # add additional fields in here
    is_student = models.BooleanField('student_status', default=False)
    is_teacher = models.BooleanField('teacher status', default=False)
    completedlessons = models.ManyToManyField('Lesson', related_name='students', default=False)
    #    add_form = CustomUserCreationForm
#    form = CustomUserChangeForm
#    model = CustomUser
#    list_display = ['email', 'username', 'is_student']

    def __str__(self):
        return self.email


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



class Track(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    introduction = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)
    lessons = models.ManyToManyField('Lesson', related_name='tracks')
    students = models.ManyToManyField('CustomUser', related_name='tracks')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Lesson(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    source = models.URLField(blank=True, null=True)
    introduction = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text


