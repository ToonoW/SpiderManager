from django.urls import path
from django.conf.urls import include
from django.contrib import admin

urlpatterns = [
    path('admin', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'', include('scrapyinfo.urls')),
    path('api/', include('scrapyinfo.urls')),
    path('api/', include('scrapycmd.urls')),
]
