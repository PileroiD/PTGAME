from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Категории"""
    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=100, verbose_name='URL', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('get_category', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Genre(models.Model):
    """Жанры"""
    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=100, verbose_name='URL', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('get_genre', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Company(models.Model):
    """Студия розработки, компания"""
    title = models.CharField('Компания', max_length=100)
    slug = models.SlugField(max_length=100, verbose_name='URL', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('company', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


# -----------------------------------------------------------------------------------------------------------------------

class Game(models.Model):
    """Игры"""
    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=100, verbose_name='URL', unique=True)
    content = models.TextField(verbose_name='Контент')
    poster = models.ImageField(verbose_name='Постер', upload_to='photos/%Y/%m/%d/', blank=True)
    special_image = models.ImageField(verbose_name='Картинка в header', upload_to='special_game_photos/%Y/%m/%d/')
    category = models.ManyToManyField(Category, verbose_name='Категория')
    genre = models.ManyToManyField(Genre, verbose_name='Жанры')
    main_category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Главная категория',
                                      related_name='main_category', null=True)
    main_genre = models.ForeignKey(Genre, on_delete=models.PROTECT, verbose_name='Главный жанр',
                                   related_name='main_genre', null=True)
    company = models.ManyToManyField(Company, verbose_name='Компания')
    date_of_issue = models.DateField('Дата выпуска игры')
    gamers = models.ManyToManyField(User, through='UserGameRelation', related_name='games')
    added = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0, verbose_name='Количество просмотров')
    draft = models.BooleanField(default=False, verbose_name='Черновик')
    videogameplay = models.CharField(max_length=300, verbose_name='Геймплей игры', unique=True, null=True, blank=True)
    interface_lang = models.CharField(max_length=255, verbose_name='Язык интерфейса', null=True, blank=True)
    voice_acting_lang = models.CharField(max_length=255, verbose_name='Язык озвучки', null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'


class MinSysReq(models.Model):
    """Минимальные системные требования"""
    oc = models.CharField(max_length=100, verbose_name='Операционная система', null=True, blank=True)
    processor = models.CharField(max_length=100, verbose_name='Процессор', null=True, blank=True)
    ozu = models.CharField(max_length=100, verbose_name='Оперативка', null=True, blank=True)
    videocart = models.CharField(max_length=100, verbose_name='Видеокарта', null=True, blank=True)
    placeondisk = models.CharField(max_length=100, verbose_name='Место на жёстком диске', null=True, blank=True)
    directx = models.CharField(max_length=100, verbose_name='DirectX', null=True, blank=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name='Игра')

    class Meta:
        verbose_name = 'Мин. сис. требования'
        verbose_name_plural = 'Мин. сис. требования'


class TorrentFile(models.Model):
    """Торрент файлы"""
    REPACK_AUTHORS = [
        ('Igruha', 'Igruha'),
        ('Xatab', 'Xatab'),
        ('R.G.Механики', 'R.G.Механики'),
        ('SxS-Fenixx', 'SxS-Fenixx'),
        ('R.G.Freedom', 'R.G.Freedom'),
        ('SEYTER', 'SEYTER'),
        ('SeregA-Lus', 'SeregA-Lus'),
        ('qoob', 'qoob'),
        ('GOG', 'GOG'),
        ('RGL-Rip', 'RGL-Rip'),
        ('Pioneer', 'Pioneer'),
        ('FitGirl', 'FitGirl'),
        ('Decepticon', 'Decepticon'),
    ]
    torrent_file_name = models.CharField(max_length=255, verbose_name='Имя торрент файла', null=True, blank=True)
    torrent_file = models.FileField(upload_to='files/%Y/%m/%d/', verbose_name='Торрент файл', blank=True, null=True)
    torrent_file_size = models.CharField(max_length=100, blank=True, null=True, verbose_name='Размер торрент-файла')
    repack_author = models.CharField(max_length=100, verbose_name='Репак от', choices=REPACK_AUTHORS, blank=True,
                                     null=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name='Игра', blank=True, null=True)
    click_count = models.IntegerField(default=0)
    descriptions = models.TextField('Особености репака', null=True)

    class Meta:
        verbose_name = 'Торрент файл'
        verbose_name_plural = 'Торрент файлы'


# ----------------------------------------------------------------------------------------------------------------------

class GameShots(models.Model):
    """ Кадры из игры """
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    image = models.ImageField(upload_to='movie_game_shots/', verbose_name='Картинка')
    game = models.ForeignKey(Game, verbose_name='Игра', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Кадр из игры'
        verbose_name_plural = 'Кадры из игры'


# ----------------------------------------------------------------------------------------------------------------------

class Reviews(models.Model):
    """ Отзывы """
    email = models.EmailField()
    name = models.CharField('Имя', max_length=100)
    text = models.TextField('Сообщение', max_length=5000)
    parent = models.ForeignKey('self', verbose_name='Родитель', on_delete=models.SET_NULL, blank=True, null=True)
    game = models.ForeignKey(Game, verbose_name='Игра', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    likes = models.ManyToManyField(User, related_name='game_comments')

    def __str__(self):
        return f"{self.name} - {self.game}"

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-created_at']


# ----------------------------------------------------------------------------------------------------------------------


class UserGameRelation(models.Model):
    """Лайки, закладки и рейтинг"""
    RATE_CHOICES = (
        (1, 'Ok'),
        (2, 'Fine'),
        (3, 'Good'),
        (4, 'Amazing'),
        (5, 'Incredible'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    in_bookmarks = models.BooleanField(default=False)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES)

    def __str__(self):
        return f'{self.user.username}: Game-{self.game}, Rate-{self.rate}'


class RatingStar(models.Model):
    """Звезда рейтинга"""
    value = models.SmallIntegerField("Значение", default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"
        ordering = ["-value"]


class Rating(models.Model):
    """Рейтинг"""
    ip = models.CharField("IP адрес", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="звезда")
    game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name="игра", related_name="games")

    def __str__(self):
        return f"{self.star} - {self.game}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"
