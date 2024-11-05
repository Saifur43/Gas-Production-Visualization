from django.urls import path
from . import views
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('api/well-data/', views.get_well_data, name='well_data'),
    path('api/field-wells/', views.get_field_wells, name='field-wells'), 
]