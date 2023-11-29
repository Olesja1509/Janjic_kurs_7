from telebot import TeleBot
from celery import shared_task
from django.conf import settings

from habits.models import Habit


@shared_task
def send_message_telegram(habit_id):
    """Задача для отправки сообщения телеграм-ботом"""
    habit = Habit.objects.get(id=habit_id)
    tg_bot = TeleBot(settings.TG_TOKEN)
    message = f'Напоминаем Вам о выполнении привычки {habit.action} в {habit.time} в {habit.place}'
    tg_bot.send_message(habit.user.chat_id, message)
