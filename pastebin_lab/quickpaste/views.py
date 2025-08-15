from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView

from .forms import PostForm
from .models import Post
from .utils import DataMixin


class MainPage(DataMixin, CreateView):
    form_class = PostForm
    template_name = 'quickpaste/index.html'
    success_url = reverse_lazy('main')
    title_page = 'QuickPaste'


def show_contacts(request):
    return render(request, 'quickpaste/contacts.html')


class ShowPost(DataMixin, DetailView):
    model = Post
    template_name = 'quickpaste/user_post.html'
    slug_url_kwarg = 'user_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_author = Post.objects.get(slug=self.kwargs['user_slug']).author
        if post_author:
            context['title'] = 'Пост ' + post_author
        else:
            context['title'] = 'Пост анонимного пользователя'
        return context
