from django_celery_beat.models import CrontabSchedule, PeriodicTask


def set_shedule(habit):
    """Создание периодичности и задачи на отправку"""
    crontab_schedule, _ = CrontabSchedule.objects.get_or_create(
        minute=habit.time.minute,
        hour=habit.time.hour,
        day_of_month=f'*/{habit.period}',
        month_of_year='*',
        day_of_week='*'
    )

    PeriodicTask.objects.create(
        crontab=crontab_schedule,
        name=f'habit task {habit.action}',
        task='habits.tasks.send_message_telegram',
        args=[habit.id]
    )
