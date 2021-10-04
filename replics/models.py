from django.db import models

# Create your models here.

from django.db import models


class Worker(models.Model):
    """
    Модель сотрудник.
    """

    fio = models.CharField(
        verbose_name='Name',
        max_length=150,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = 'worker'
        verbose_name_plural = 'workers'
        db_table = 'worker'
