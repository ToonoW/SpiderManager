from django.conf.urls import url, include

from backend import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^api/v1/', include('backend.api_urls')),
]