from django.urls import path

from. import views

urlpatterns = [
    path('', views.liste_traiteurs, name = 'traiteur'),
    path('traiteurs/<int:id>/detail/', views.detail, name = 'detail_traiteur'),
    path('ajout_traiteur/', views.ajouter_traiteur, name = 'ajout_traiteur'),
    path('signup/', views.SignUpView.as_view(), name = 'signup')

]