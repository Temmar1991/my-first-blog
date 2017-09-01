from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [

  url(r'^$', views.post_list, name='post_list'),
 # url(r'^post/(?P<pk>[0-9]+)/$'), views.post_detail, name='post_detail'),
  url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
  url(r'^post/new/$', views.post_new, name='post_new'),
  url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),

  url(r'^bootstap$', TemplateView.as_view(template_name='blog/bootstap_demo1.html')),
]
