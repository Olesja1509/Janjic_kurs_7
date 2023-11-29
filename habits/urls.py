from django.urls import path

from habits.apps import HabitsConfig
from habits.views import *

app_name = HabitsConfig.name


urlpatterns = [
    path('habit/create/', HabitCreateAPIView.as_view(), name='create_habit'),
    path('habit/', HabitListAPIView.as_view(), name='list_habit'),
    path('habit/<int:pk>/', HabitRetrieveAPIView.as_view(), name='get_habit'),
    path('habit/update/<int:pk>/', HabitUpdateAPIView.as_view(), name='update_habit'),
    path('habit/delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='delete_habit'),
    path('habit/public/', PublicHabitListView.as_view(), name='list_public_habit'),
]
