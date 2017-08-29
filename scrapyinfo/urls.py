from django.conf.urls import url, include

from scrapyinfo import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^api/v1/', include('scrapyinfo.api_urls')),
]
