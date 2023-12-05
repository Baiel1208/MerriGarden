from django.db import models
from django.utils.translation import gettext_lazy as _
# from .choices import Adult

# Create your models here.
class Order(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name=_('ФИО')
    )
    phone_number = models.CharField(
        max_length=20,
        verbose_name=_('Номер телефона')
    )
    date = models.DateField(
        verbose_name=_('Дата')
    )


    def __str__(self) -> str:
        return f'{self.name}'
    

    class Meta:
        verbose_name = _('Заказы')
        verbose_name_plural = _('Заказы')