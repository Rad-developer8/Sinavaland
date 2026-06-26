from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pwa.urls')),
    path('', include(('core.urls', 'core'), namespace='core')),
    path('accommodations/', include(('accommodations.urls', 'accommodations'), namespace='accommodations')),
    path('tours/', include(('tours.urls', 'tours'), namespace='tours')),
    path('marketplace/', include(('marketplace.urls', 'marketplace'), namespace='marketplace')),
    path('magazine/', include(('magazine.urls', 'magazine'), namespace='magazine')),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
