"""codeselfstudy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
import os

from django.contrib import admin
from django.urls import path, include
from . import settings
from .views import robots_txt

admin_url = os.environ.get("ADMIN_URL")

handler404 = "codeselfstudy.views.not_found"
handler500 = "codeselfstudy.views.server_error"
# handler403 = "codeselfstudy.views.denied"
# handler400 = "codeselfstudy.views.bad_request"


urlpatterns = [
    path("robots.txt", robots_txt),
    # path("puzzles/", include("puzzles.urls")),
    path("slack/", include("slack.urls")),
    path(f"{admin_url}/", admin.site.urls),
    path("", include("pages.urls")),
]

if settings.DEBUG is True:
    import debug_toolbar
    urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)))
