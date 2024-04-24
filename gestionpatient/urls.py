from django.urls import path
from dossierpatient import views

urlpatterns = [
     path('', views.index, ),
    path('patient/', views.patient_views, name='patient_views'),
]


