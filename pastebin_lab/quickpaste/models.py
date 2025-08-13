from datetime import datetime, timedelta

from django.db import models
from django.urls import reverse

from pastebin_lab.settings import LANGUAGE
from quickpaste.services import create_unique_url_for_slug


class Post(models.Model):
    content = models.TextField(verbose_name='Контент',
                               help_text="Вставьте ваш текст здесь..."
                               )
    slug = models.SlugField(max_length=100,
                            unique=True,
                            verbose_name='Slug'
                            )
    publicity = models.BooleanField(default=False,
                                    verbose_name='Публичный пост'
                                    )
    author = models.CharField(max_length=100,
                              blank=True,
                              verbose_name='Автор',
                              default='',
                              )
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/",
                              default=None,
                              blank=True,
                              null=True,
                              verbose_name='Фото'
                              )
    language = models.CharField(max_length=100,
                                choices=LANGUAGE,
                                default=None,
                                verbose_name='Язык'
                                )
    time_create = models.DateTimeField(auto_now=True,
                                       verbose_name='Время создания'
                                       )
    time_life = models.DateTimeField(verbose_name='Время жизни',
                                     blank=True,
                                     default=datetime.now() + timedelta(days=30)
                                     )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = create_unique_url_for_slug(Post, self.content[:10])
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('save_post', kwargs={'user_slug': self.slug})

    class Meta:
        db_table = 'Post'
