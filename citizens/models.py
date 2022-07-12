from django.contrib.auth import get_user_model
from django.db import models
from .validators import validate_interval

User = get_user_model()


class Citizen(models.Model):
    """Модель Сословия"""
    STATUS = (
        ('Феодал', 'Феодал'),
        ('Духовенство', 'Духовенство'),
        ('Крестьянин', 'Крестьянин')
    )

    first_name = models.CharField('Имя', max_length=200)
    last_name = models.CharField('Фамилия', max_length=200)
    age = models.IntegerField(
        'Возраст',
        validators=[validate_interval]
    )
    status = models.CharField('Статус', max_length=50, choices=STATUS)
    master = models.ForeignKey(
        'self', 
        on_delete=models.CASCADE,
        verbose_name='Хозяин',
        null=True,
        blank=True
    )
    income = models.DecimalField(
        'Доход',
        max_digits=5,
        decimal_places=2, 
        default=0,
    )

    def save(self, *args, **kwargs):
        if self.status == 'Феодал':
            self.master = None
            self.income = 100
        elif self.status == 'Духовенство':
            self.income = 75
        else:
            self.income = 50
        super(Citizen, self).save(*args, **kwargs)

    def __str__(self):
        return self.last_name

    class Meta:
        ordering = ('-age',)
        verbose_name = 'Сословие'
        verbose_name_plural = 'Сословия'
        constraints = [
            models.CheckConstraint(check=models.Q(age__gte=120), name='age_gte_120'),
            models.CheckConstraint(check=models.Q(age__lte=0), name='age_lte_0'),
        ]