from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('accounts/register', views.registration, name='registration'),
    path('idol/profile/<pk>', views.idoldetailview,  name='idoldetailview'),
    path('idol/', views.idolfulllist, name='idolfulllist'),
    path('idol/register', views.idolregister, name='idolregister'),
    path('idol/profile/<pk>/edit', views.idol_edit, name='idol_edit')
]