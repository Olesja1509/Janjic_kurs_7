from rest_framework import serializers


class HabitExceptionValidator:
    def __init__(self, field_1, field_2):
        self.field_1 = field_1  #'associated_habit'
        self.field_2 = field_2  #'prize'

    def __call__(self, value):
        if value.get(self.field_1) and value.get(self.field_2):
            raise serializers.ValidationError(
                'Исключён одновременный выбор связанной привычки и указания вознаграждения'
            )


class TimeValidator:
    def __init__(self, field):
        self.field = field  #'lead_time'

    def __call__(self, value):
        if value.get(self.field) > 120:
            raise serializers.ValidationError('Время выполнения должно быть не больше 120 секунд')


class IsPleasantValidator:
    def __init__(self, field_1):
        self.field_1 = field_1  #'associated_habit'

    def __call__(self, value):
        if dict(value).get(self.field_1) is not None:
            if not value.get(self.field_1).is_pleasurable:
                raise serializers.ValidationError(
                    'В связанные привычки могут попадать только привычки с признаком приятной привычки')


class IsPleasantOrPrizeValidator:
    def __init__(self, field_1, field_2, field_3):
        self.field_1 = field_1  #'is_pleasurable'
        self.field_2 = field_2  #'prize'
        self.field_3 = field_3  # 'associated_habit'

    def __call__(self, value):
        if dict(value).get(self.field_1):
            if dict(value).get(self.field_2) is not None or dict(value).get(self.field_3) is not None:
                raise serializers.ValidationError(
                    'У приятной привычки не может быть вознаграждения или связанной привычки')


class PeriodValidator:
    def __init__(self, field):
        self.field = field  #'period'

    def __call__(self, value):
        if value.get(self.field) > 7:
            raise serializers.ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней')

