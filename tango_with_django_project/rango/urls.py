from django.urls import path
from rango import views
app_name = 'rango'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('category/<slug:category_name_slug>/',
        views.show_category, name='show_category'),
    path('static/', views.static, name='static'),
    path('static/images/rango.jpg', views.rangojpg, name='static/image/rango.jpg')
]