from django.urls import path
from .views import spare_part_list, spare_part_detail

urlpatterns = [
    path('spare-parts/', spare_part_list, name='spare-part-list'),
    path('spare-parts/<int:pk>/', spare_part_detail, name='spare-part-detail'),
]
