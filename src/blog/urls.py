from django.urls import path
from . import views

#start urls  # inja omadim path haiee tarif kardim ke mian az oon func haye dakhele file 
# view stefade mikonand ta oon chiz ro dar oon route moshakhas shode namayesh bede
urlpatterns = [
    path('', views.Home, name='home_blog'),
    path('about/', views.About, name='home_about'),
]
#end urls