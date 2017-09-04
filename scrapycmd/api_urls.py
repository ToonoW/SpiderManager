from django.conf.urls import url

from scrapycmd import api_views


urlpatterns = [
    url(r'^run_spider$', api_views.RunSpider.as_view(), name='run-spider'),

    url(r'^run_group_spiders$', api_views.RunGroupSpiders.as_view(), name='run-group-spiders'),

    url(r'^cancel_spider$', api_views.CancelSpider.as_view(), name='cancel-spider'),

    url(r'^cancel_group_spiders$', api_views.CancelGroupSpiders.as_view(), name='cancel-group-spiders'),

    url(r'^query_spiders_log$', api_views.QuerySpidersLog.as_view(), name='query-spiders-log'),

    url(r'^query_all_spiders_log$', api_views.QueryAllSpidersLog.as_view(), name='query-all-spiders-log'),

]