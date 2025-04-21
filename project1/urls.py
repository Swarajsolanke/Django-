from django.contrib import admin
from django.urls import path
from app1 import views

from app2 import views  as views2   
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name='home'),
    path("index/",views.index,name="index"),
    path("learn/",views.learn,{"status":"ok"},name='learn'),
    path("index2/",views2.index2,name="index2"),
    path("study/",views.study,{"status":"ok"},name="study"),
    path("py/",views.study,name="study"),
]
