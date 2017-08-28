from django.conf.urls import url

from backend import api_views


urlpatterns = [
    url(r'^scrapyd_list', api_views.ScrapydList.as_view(), name='scrapyd_list'),
    url(r'^scrapyd_detial/(?P<pk>[0-9]+)$', api_views.ScrapydDetial.as_view(), name='scrapyd_detial')

]