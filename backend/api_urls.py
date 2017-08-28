from django.conf.urls import url

from backend import api_views


urlpatterns = [
    url(r'^scrapyd', api_views.ScrapydView.as_view(), name='scrapyd'),

]