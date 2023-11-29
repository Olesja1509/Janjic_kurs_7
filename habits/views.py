from rest_framework import generics
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.paginators import HabitPaginator
from habits.serializers import HabitSerializer
from users.permissions import IsOwner, IsModerator


class HabitCreateAPIView(generics.CreateAPIView):
    """Контроллер для создания привычки"""
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]


class HabitListAPIView(generics.ListAPIView):
    """Контроллер для просмотра списка привычек"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitPaginator
    permission_classes = [IsAuthenticated, IsOwner | IsModerator]

    def get_queryset(self):
        qs = super().get_queryset()

        if not self.request.user.is_staff:
            qs = qs.filter(user=self.request.user)

        return qs


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """Контроллер для получения описания привычки"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsModerator]


class HabitUpdateAPIView(generics.UpdateAPIView):
    """Контроллер для редактирования привычки"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitDestroyAPIView(generics.DestroyAPIView):
    """Контроллер для удаления привычки"""
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class PublicHabitListView(ListAPIView):
    """Вывод списка публичных привычек"""
    queryset = Habit.objects.filter(public=True).order_by('pk')
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator
