from django.db import models


class BlogEntryModel(models.Model):
    title = models.CharField(
        max_length=32,
        blank=False,
        null=False,
        default='Запись блога',
    )

    description = models.CharField(
        max_length=128,
        blank=False,
        null=False,
        default='Краткая информация о записи в блог',
    )

    article = models.CharField(
        max_length=8192,
        blank=False,
        null=False,
        default='Краткая информация о записи в блог',
    )

    created = models.DateTimeField(
        auto_created=True,
    )
