import os

from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from openwisp_users.api.urls import get_api_urls as get_users_api_urls

def home(request):
    return HttpResponse("Welcome to OpenWISP IPAM")

urlpatterns = [
    path('', home, name='home'),  # Default view for root URL
    path('admin/', admin.site.urls),
    path('api/v1/', include('openwisp_utils.api.urls')),
    path('api/v1/', include((get_users_api_urls(), 'users'), namespace='users')),
    path('', include('openwisp_ipam.urls')),
]

if os.environ.get('SAMPLE_APP', False):
    from openwisp_ipam.urls import get_urls
    from .sample_ipam import views as api_views
    urlpatterns += [
        path('', include(get_urls(api_views))),
    ]

if settings.DEBUG and 'debug_toolbar' in settings.INSTALLED_APPS:
    import debug_toolbar
    urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)))

