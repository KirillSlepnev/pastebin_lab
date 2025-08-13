from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .forms import PostForm
from .models import Post


def show_main_page(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect(post.get_absolute_url())
    else:
        form = PostForm()

    return render(request, 'quickpaste/index.html', {'form': form})


def show_contacts(request):
    return render(request, 'quickpaste/contacts.html')


def show_post(request, user_slug):
    post = get_object_or_404(Post, slug=user_slug)
    return render(request, 'quickpaste/user_post.html', {'post': post})


def save_post(request, user_slug):
    post = get_object_or_404(Post, slug=user_slug)
    post_url = request.build_absolute_uri(
        reverse('show_post', kwargs={'user_slug': post.slug})
    )
    return render(request, 'quickpaste/save_post.html',
                  {'post': post, 'full_post_url': post_url})


def login(request):
    return render(request, 'quickpaste/login.html')


def register(request):
    return render(request, 'quickpaste/login.html')
