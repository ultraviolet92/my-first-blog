from django.shortcuts import render
from django.utils import timezone
from .models import Post, Track, Lesson, Comment, CustomUser
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, TrackForm, LessonForm, CommentForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

@login_required
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return render(request, 'blog/post_detail.html', {'post': post})


    return render(request, 'blog/post_detail.html', {'post': post})


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})



@login_required
def track_list(request):
    tracks = Track.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'tracks/track_list.html', {'tracks': tracks})



@login_required
def profile(request):
    tracks = Track.objects.filter(students__id=request.user.id).order_by('published_date')
    return render(request, 'profile.html', {'tracks': tracks})


@login_required
def track_detail(request, pk):
    track = get_object_or_404(Track, pk=pk)
    
    user = request.user
    lessons = Lesson.objects.filter(tracks__id=track.id, students=user).order_by('published_date')
    activelessons = Lesson.objects.filter(tracks__id=track.id).exclude(students=user).order_by('published_date')

    #track.students
    #enroll = track.students.contains(students__id=request.user.id)

    enroll = Track.objects.filter(students__id=request.user.id, pk=pk).exists()
    
    if request.method == "POST" and 'enroll' in request.POST:
        track.students.add(request.user)
        track.save()
        tracks = Track.objects.filter(students__id=request.user.id).order_by('published_date')
        enroll = True
        return render(request, 'profile.html', {'tracks': tracks, 'enroll': enroll, 'user': user})

    elif request.method == "POST" and 'unenroll' in request.POST:
        track.students.remove(request.user)
        track.save()
        tracks = Track.objects.filter(students__id=request.user.id).order_by('published_date')
        enroll = False
        return render(request, 'profile.html', {'tracks': tracks, 'enroll': enroll, 'user': user})

    return render(request, 'tracks/track_detail.html', {'track': track, 'lessons': lessons, 'activelessons': activelessons, 'enroll': enroll, 'user': user})

 


@login_required
def lesson_detail(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    
    comments = Comment.objects.filter(lesson__id=pk).order_by('published_date')

    user = get_object_or_404(CustomUser, id=request.user.id)
    completed = CustomUser.objects.filter(completedlessons__id=pk, id=request.user.id).exists()


    if request.method == "POST" and 'comment' in request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.lesson = lesson
            post.published_date = timezone.now()
            post.save()
            return render(request, 'lessons/lesson_detail.html', {'lesson': lesson, 'form':form, 'comments':comments, 'completed':completed})
    else:
        form = CommentForm()
    
    form = CommentForm()

    if request.method == "POST" and 'complete' in request.POST:
        user.completedlessons.add(lesson)
        user.save()
        completed = True
        #return render(request, 'lessons/lesson_detail.html', {'lesson': lesson, 'form':form, 'comments':comments, 'completed':completed})

    elif request.method == "POST" and 'active' in request.POST:
        user.completedlessons.remove(lesson)
        user.save()
        completed = False
        #return render(request, 'lessons/lesson_detail.html', {'lesson': lesson, 'form':form, 'comments':comments, 'completed':completed})


    return render(request, 'lessons/lesson_detail.html', {'lesson': lesson, 'form':form, 'comments':comments, 'completed':completed})


   



@login_required
def track_new(request):
    if request.method == "POST" and 'save' in request.POST:
        form = TrackForm(request.POST)
        if form.is_valid():
            track = form.save(commit=False)
            track.creator = request.user
            track.published_date = timezone.now()
            track.save()
            track.students.add(request.user)
            track.save()
            form.save_m2m()
            return redirect('track_detail', pk=track.pk)
    elif request.method == "POST" and 'save-ex' in request.POST:
        form = TrackForm(request.POST)
        if form.is_valid():
            track = form.save(commit=False)
            track.creator = request.user
            track.published_date = timezone.now()
            track.save()
            return redirect('track_detail', pk=track.pk)
    else:
        form = TrackForm()
    return render(request, 'tracks/track_edit.html', {'form': form})


@login_required
def add_track(request) :
    return render(request, 'tracks/profile.html')



@login_required
def lesson_list(request):
    lessons = Lesson.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'lessons/lesson_list.html', {'lessons': lessons})




@login_required
def lesson_new(request):
    if request.method == "POST":
        form = LessonForm(request.POST)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.creator = request.user
            lesson.published_date = timezone.now()
            lesson.save()
            return redirect('lesson_detail', pk=lesson.pk)
    else:
        form = LessonForm()
    return render(request, 'lessons/lesson_edit.html', {'form': form})



class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'