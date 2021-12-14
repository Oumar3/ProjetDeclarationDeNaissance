from django.urls import path
from . import views
urlpatterns = [
    path('', views.listeEnfantEnregistrer),
    path('personnel/',views.info_Personnel),
    path('detail/<int:id>',views.detail,name='detail'),
]