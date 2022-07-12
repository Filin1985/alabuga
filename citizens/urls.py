from django.urls import path
from .views import index, citizen_create, citizen_detail, citizens, citizen_edit, CitizenDeleteView
app_name = 'citizens'

urlpatterns = [
    path('', index, name='index'),
    path('citizen/<int:citizen_id>/', citizen_detail, name='citizen_detail'),
    path('create/', citizen_create, name='citizen_create'),
    path('citizens/', citizens, name='citizens_list'),
    path('citizens/<int:citizen_id>/edit/', citizen_edit, name='citizen_edit'),
    path('<int:pk>/delete/', CitizenDeleteView.as_view(), name="citizen_delete"),
]