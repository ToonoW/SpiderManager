from django.urls import path

from scrapycmd import views


urlpatterns = [
    path('run_spider$', views.RunSpider.as_view()),
    path('run_group_spiders$', views.RunGroupSpiders.as_view()),
    path('cancel_spider$', views.CancelSpider.as_view()),
    path('cancel_group_spiders$', views.CancelGroupSpiders.as_view()),
    path('query_spiders_log$', views.QuerySpidersLog.as_view()),
    path('query_all_spiders_log$', views.QueryAllSpidersLog.as_view()),
]
