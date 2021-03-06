from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from bscloud.system.api.serializers import SerializersRouter
from bscloud.views import board_reg


urlpatterns = patterns('',    
    url(r'^api/', include(SerializersRouter.get_router().urls)),
    url(r'^api/register/', board_reg),

    # for future authentication
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
