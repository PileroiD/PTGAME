import os
import random

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login, logout
from django.db.models import F
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic, View
from django.contrib.auth.forms import UserCreationForm
from rest_framework.mixins import UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from . import models
from .forms import UserRegisterForm, UserLoginForm, ReviewForm, RatingForm


# def LikeView(request, pk):
#     comment = get_object_or_404(models.Reviews, id=request.POST.get('review_id'))
#     comment.likes.add(request.user)
#     return HttpResponseRedirect(reverse('category', args=[str(pk)]))

class NewGames(generic.ListView):
    """Самые новые игры"""
    template_name = 'game/index.html'
    context_object_name = 'game_list'
    paginate_by = 48
    queryset = models.Game.objects.filter(draft=False).order_by('-date_of_issue')
    extra_context = {'new': True}


class MostWaiting(generic.ListView):
    """Самые ожидаемые игры"""
    template_name = 'game/index.html'
    context_object_name = 'game_list'
    paginate_by = 48
    queryset = models.Game.objects.filter(torrentfile__game=None)
    extra_context = {'mostwaiting': True}


class Home(generic.ListView):
    """Главная страничка"""
    model = models.Game
    template_name = 'game/index.html'
    queryset = models.Game.objects.filter(draft=False).order_by('-views')
    paginate_by = 48


class GameDetail(generic.DetailView):
    """Детали игры"""
    model = models.Game

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        context['anothers'] = models.Game.objects.exclude(slug=self.object.slug).filter(draft=False, main_category=self.object.main_category, main_genre=self.object.main_genre)[:6]
        context['created_at'] = models.Game.objects.filter(draft=False).order_by('-added')[:20]
        context['star_form'] = RatingForm()
        # Остальное догружается в templatetags
        return context


class AddStarRating(View):
    """Добавление рейтинга фильму"""

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        form = RatingForm(request.POST)
        if form.is_valid():
            models.Rating.objects.update_or_create(
                ip=self.get_client_ip(request),
                game_id=int(request.POST.get("game")),
                defaults={'star_id': int(request.POST.get("star"))}
            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)


class Category(generic.ListView):
    """Игры по категориям"""
    model = models.Game
    template_name = 'game/index.html'
    context_object_name = 'game_list'
    paginate_by = 24

    def get_queryset(self):
        return models.Game.objects.filter(draft=False, category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = models.Category.objects.get(slug=self.kwargs['slug'])
        return context


class Genre(generic.ListView):
    """Игры по жанрам"""
    template_name = 'game/index.html'
    context_object_name = 'game_list'
    paginate_by = 24

    def get_queryset(self):
        return models.Game.objects.filter(draft=False, genre__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genre'] = models.Genre.objects.get(slug=self.kwargs['slug'])
        return context


class Company(generic.ListView):
    """Вывод игр, сортировка по компаниям"""
    model = models.Company
    template_name = 'game/index.html'
    context_object_name = 'game_list'

    def get_queryset(self):
        return models.Game.objects.filter(draft=False, company__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = models.Company.objects.get(slug=self.kwargs['slug'])
        context['referer'] = self.request.META.get('HTTP_REFERER')
        game = models.Game.objects.get(slug=context['referer'].split('/')[::-1][1])
        context['game_from_bread'] = game.title
        return context


class Search(generic.ListView):
    """Поиск игр"""
    template_name = 'game/index.html'

    def get_queryset(self):
        return models.Game.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context


def register(request):
    """ Для регистрации пользователей """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()  # Для входа сразу после регистрации
            messages.success(request, 'Вы успешно зарегестрировались!')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'game/registry.html', {'form': form})


def user_login(request):
    """ Для входа пользователей """
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'game/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')


class AddReview(generic.View):
    """Отзывы"""

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        game = models.Game.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)  # Сохранение формы приостанавливается
            if request.POST.get('parent', None):
                form.parent_id = int(request.POST.get('parent'))
            form.game = game
            form.save()
        else:
            form = ReviewForm()
        return redirect(game.get_absolute_url())


class DownloadCount(generic.View):
    """Подсчек количества скачиваний"""

    def post(self, request, pk):
        game = models.Game.objects.get(id=pk)
        post_file_name = request.POST.get('click')[24:]
        # print(post_file_name)
        file = models.TorrentFile.objects.get(torrent_file_name=post_file_name)
        if file:
            file.game = game
            file.click_count += 1
            file.save()
            file.refresh_from_db()
        return redirect(game.get_absolute_url())


