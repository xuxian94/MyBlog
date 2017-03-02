from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index , name='index'),
    url(r'^article/(?P<blog_body_id>[0-9]+)/$',views.article,name='article'),
    url(r'^python/',views.artical_python,name='python')
]