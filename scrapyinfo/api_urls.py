from django.conf.urls import url

from scrapyinfo import api_views


urlpatterns = [
    url(r'^refresh_platform_information$', api_views.RefreshPlatformView.as_view(), name='refresh-platform-information'),

    url(r'^scrapyd_list$', api_views.ScrapydList.as_view(), name='scrapyd-list'),
    url(r'^scrapyd_detial/(?P<pk>[0-9]+)$', api_views.ScrapydDetial.as_view(), name='scrapyd-detial'),

    url(r'^project_list$', api_views.ProjectList.as_view(), name='prject-list'),
    url(r'^project_detial/(?P<pk>[0-9]+)$', api_views.ProjectDetial.as_view(), name='project-detial'),

    url(r'^spider_list$', api_views.SpiderList.as_view(), name='spider-list'),
    url(r'^spider_detial/(?P<pk>[0-9]+)$', api_views.SpiderDetial.as_view(), name='spider-detial'),

    url(r'^group_list$', api_views.GroupList.as_view(), name='group-list'),
    url(r'^group_detial$', api_views.GroupDetial.as_view(), name='group-detial'),
]
