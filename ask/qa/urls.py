from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'.*', views.test),
    url(r'^$', views.test, name='index'),
    url(r'^(?P<question_id>[0-9]+)/$', views.test, name='question'),
    # url(r'^popular/.*$', views.popular, name='popular'),

]
