from django.urls import path
from app_aviacao import views

urlpatterns = [
#rota, viwe responsável, nome de referência
   path('',views.home,name='home')
]
