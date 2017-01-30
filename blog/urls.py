from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.home_page, name="HomePage"),
    url(r'^post/(?P<id>\d+)/$', views.post_page, name="PostPage"),

]
