from django.urls import path

from scrapycmd import views


urlpatterns = [
    path('runSpider/<int:spider_id>', views.RunSpider.as_view()),
    path('runGroup/<int:group_id>', views.RunGroupSpiders.as_view()),
    path('stopSpider/<int:spider_id>', views.CancelSpider.as_view()),
    path('stopGroup/<int:group_id>', views.CancelGroupSpiders.as_view()),
    path('jobs', views.QueryAllSpidersLog.as_view()),
    # path('listJob//', views.QuerySpidersLog.as_view()),
]
