"""calttc_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

#static
from django.views.static import serve

# media
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    path('membership/', include('membership.urls')),
    path('sessions/', include('session.urls')),
    path('schedule/', include('schedule.urls')),
    path('announcements/', include('announcements.urls')),
    path('team/', include('team.urls')), 
    path('images/', include('images.urls')),
    path('table_locations/', views.table_locations, name='table-locations'),
    path('graphics/', views.graphics, name='graphics'),
    path('all_graphics/', views.all_graphics, name='all-graphics'),
    path('home/', views.home, name='home'),
    path('', views.home, name=''),
    ]

# media url patterns
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# configure admin portal headers
admin.site.site_header = "Cal Table Tennis Admin Portal"
admin.site.site_title = "Cal Table Tennis"
admin.site.index_title = "Admin Home"