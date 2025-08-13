from django.apps import apps
from django.utils.text import slugify
from unidecode import unidecode


def save_post_to_db(post) -> str:
    """Сохраняет пост в БД и возвращает URL"""
    pass


def create_unique_url_for_slug(model, field, max_length=10) -> str:  # fixme исправить на генерацию без контекста
    """Создает уникальный слаг длиной не превышающей определенное
    количество символов"""

    field = f"{str(field):0>{max_length}}"[:max_length]

    origin_slug = slugify(unidecode(field))
    unique_slug = origin_slug
    extra_slug = 1
    while model.objects.filter(slug=unique_slug).exists():
        unique_slug = f'{origin_slug[:max_length-(len(str(extra_slug)) + 1)]}-{extra_slug}'
        extra_slug += 1

    return unique_slug
