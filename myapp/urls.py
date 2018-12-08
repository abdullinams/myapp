from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^mydoctor$', views.mydoctor, name='mydoctor'),
    url(r'^newdoctor/$', views.newdoctor, name='newdoctor'),
    url(r'^deletedoctor/$', views.deletedoctor, name='deletedoctor'),
    url(r'^mynurse$', views.mynurse, name='mynurse'),
    url(r'^newnurse/$', views.newnurse, name='newnurse'),
    url(r'^myclient$', views.myclient, name='myclient'),
    url(r'^newclient$', views.newclient, name='newclient'),
    url(r'^myhistory$', views.myhistory, name='myhistory'),
    url(r'^newhistory$', views.newhistory, name='newhistory'),    
]
