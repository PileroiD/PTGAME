from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe

from .models import *


class GameAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Game
        fields = '__all__'


class TorrentFileInLine(admin.StackedInline):
    model = TorrentFile
    extra = 1


class MinSysReqInLine(admin.StackedInline):
    model = MinSysReq
    extra = 1


class GameShotsInLine(admin.StackedInline):
    model = GameShots
    extra = 1


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    """Игры"""
    prepopulated_fields = {'slug': ('title',)}
    form = GameAdminForm
    save_as = True
    save_on_top = True
    list_display = ('id', 'title', 'draft', 'get_poster', 'added', 'date_of_issue')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('company',)
    readonly_fields = ('get_poster', 'views')
    list_editable = ('draft',)
    fields = (
        'title', 'slug', 'content', 'poster', 'special_image', 'get_poster', 'category', 'genre', 'main_category',
        'main_genre', 'videogameplay', 'company', 'interface_lang', 'voice_acting_lang', 'date_of_issue')
    inlines = [GameShotsInLine, TorrentFileInLine, MinSysReqInLine]

    def get_poster(self, obj):
        if obj.poster:
            return mark_safe(f"<img src='{obj.poster.url}' width='50px' >")
        return '-'

    get_poster.short_description = 'Постер'


@admin.register(TorrentFile)
class TorrentFileAdmin(admin.ModelAdmin):
    """Торрент-файлы"""
    list_display = ('id', 'torrent_file', 'torrent_file_size', 'repack_author', 'game', 'click_count')
    list_display_links = ('id', 'repack_author')
    list_filter = ('game', 'repack_author')
    fields = ('game', 'torrent_file', 'torrent_file_name', 'torrent_file_size', 'repack_author', 'descriptions')
    save_as = True


# ----------------------------------------------------------------------------------------------------------------------

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """ Категории """
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'slug')
    list_display_links = ('id', 'title')
    fields = ('title', 'slug')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """ Категории """
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'slug')
    list_display_links = ('id', 'title')
    fields = ('title', 'slug')


@admin.register(MinSysReq)
class MinSysReqAdmin(admin.ModelAdmin):
    """Минимальные системные требования"""
    list_display = ('id', 'game')
    fields = ('game', 'oc', 'processor', 'ozu', 'videocart', 'placeondisk', 'directx')


# ----------------------------------------------------------------------------------------------------------------------

@admin.register(GameShots)
class GameShotsAdmin(admin.ModelAdmin):
    """ Для картинок из игры """
    save_as = True
    save_on_top = True
    list_display = ('id', 'title', 'game', 'get_image')
    list_display_links = ('id', 'title')
    readonly_fields = ('get_image',)
    fields = ('title', 'game', 'image')

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width='50px' >")
        return '-'

    get_image.short_description = 'Фото'


# ----------------------------------------------------------------------------------------------------------------------

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    """ Отзывы """
    save_on_top = True
    list_display = ('id', 'name', 'parent', 'game')
    list_display_links = ('id', 'name')
    fields = ('name', 'email', 'text', 'parent', 'game')


# ----------------------------------------------------------------------------------------------------------------------

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    """Компании"""
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'slug')
    list_display_links = ('id', 'title')
    fields = ('title', 'slug')


@admin.register(UserGameRelation)
class UserGameRelationAdmin(admin.ModelAdmin):
    pass


# ----------------------------------------------------------------------------------------------------------------------


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Рейтинг"""
    list_display = ("star", "game", "ip")


admin.site.register(RatingStar)
