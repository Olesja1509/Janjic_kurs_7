from django.db import models
from django.utils import timezone

NULLABLE = {'null': True, 'blank': True}


class Habit(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='пользователь', **NULLABLE)
    place = models.CharField(max_length=50, verbose_name='место')
    time = models.TimeField(verbose_name='время', **NULLABLE)
    action = models.TextField(verbose_name='действие')
    is_pleasurable = models.BooleanField(default=False, verbose_name='признак приятной привычки')
    associated_habit = models.ForeignKey('self', on_delete=models.SET_NULL, **NULLABLE,
                                         verbose_name='связанная привычка')
    period = models.IntegerField(default=1, verbose_name='периодичность (в днях)')
    prize = models.CharField(max_length=100, verbose_name='вознаграждение', **NULLABLE)
    lead_time = models.PositiveIntegerField(verbose_name='время на выполнение')
    public = models.BooleanField(default=True, verbose_name='признак публичности')

    def __str__(self):
        return f'Я буду {self.action} в {self.time} в {self.place}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
