from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.shortcuts import render, redirect, get_object_or_404

from .models import *
from .utils import *
from .forms import *


class IndexListView(ListView, DataMixin):
    model = Phone
    template_name = 'phone/index.html'
    context_object_name = 'posts'
    paginate_by = 7

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Phone.objects.filter(is_published=True).select_related('cat').order_by('-id')


class PhoneUpdateView(UpdateView):
    model = Phone
    template_name = 'phone/addpage.html'
    fields = '__all__'
    success_url = reverse_lazy('index')


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'phone/addpage.html'
    success_url = reverse_lazy('index')
    login_url = reverse_lazy('index')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить товар")
        return dict(list(context.items()) + list(c_def.items()))


class ShowPost(DataMixin, DetailView):
    model = Phone
    template_name = 'phone/post.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


class PhoneCategory(DataMixin, ListView):
    model = Phone
    template_name = 'phone/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Phone.objects.filter(cat__id=self.kwargs['cat_id'], is_published=True).select_related('cat').order_by('-id')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(id=self.kwargs['cat_id'])
        c_def = self.get_user_context(title='Категория - ' + str(c.name),
                                      cat_selected=c.pk)
        return dict(list(context.items()) + list(c_def.items()))


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'phone/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('index')


def logout_user(request):
    logout(request)
    return redirect('index')
