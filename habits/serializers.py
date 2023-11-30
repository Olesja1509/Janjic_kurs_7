from habits.tasks import send_message_telegram

from habits.models import Habit
from habits.validators import *


class HabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            HabitExceptionValidator(field_1='associated_habit', field_2='prize'),
            TimeValidator(field='lead_time'),
            IsPleasantValidator(field_1='associated_habit'),
            IsPleasantOrPrizeValidator(field_1='is_pleasurable', field_2='prize', field_3='associated_habit'),
            PeriodValidator(field='period')
        ]
