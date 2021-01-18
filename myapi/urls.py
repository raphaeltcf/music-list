from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls import url
from myapp import views

urlpatterns = [
    url(r'^musics/$', views.MusicList.as_view(), name='music-list'),
    url(r'^', include('myapp.url')),
    url(r'^admin/', admin.site.urls),

]