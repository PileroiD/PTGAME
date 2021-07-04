from django import template

from game import models, forms

register = template.Library()


@register.inclusion_tag('game/_sidebar.html')
def for_sidebar_inclusiontag(md=4, percent=49):
    categories = models.Category.objects.all()
    genres = models.Genre.objects.all()
    popular = models.Game.objects.order_by('-views')[:12]
    return {'categories': categories, 'genres': genres, 'popular': popular, 'md': md, 'percent': percent}

