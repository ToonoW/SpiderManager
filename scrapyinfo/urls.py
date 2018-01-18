from django.urls import path

from scrapyinfo import views


urlpatterns = [
    path('refresh_platform_information', views.RefreshPlatformView.as_view()),
    path('scrapyds', views.ScrapydList.as_view()),
    path('scrapyd/<pk>', views.ScrapydDetial.as_view()),
    path('projects', views.ProjectList.as_view()),
    path('project/<pk>', views.ProjectDetial.as_view()),
    path('spiders', views.SpiderList.as_view()),
    path('spider/<pk>', views.SpiderDetial.as_view()),
    path('groups', views.GroupList.as_view()),
    path('group/<pk>', views.GroupDetial.as_view()),
]
