from django.conf.urls import url

from backend import api_views


urlpatterns = [
    url(r'^scrapyd_list', api_views.ScrapydList.as_view(), name='scrapyd_list'),
    url(r'^scrapyd_detial/(?P<pk>[0-9]+)$', api_views.ScrapydDetial.as_view(), name='scrapyd_detial'),
    url(r'project_list', api_views.ProjectList.as_view(), name='prject_list'),
    url(r'project_detial/(?P<pk>[0-9]+)$', api_views.ProjectDetial.as_view(), name='project_detial'),
    url(r'spider_list', api_views.SpiderList.as_view(), name='spider_list'),
    url(r'spider_detial/(?P<pk>[0-9]+)$', api_views.SpiderDetial.as_view(), name='spider_detial'),
]