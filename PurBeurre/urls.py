"""PurBeurre URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.utils.translation import gettext as _


urlpatterns = [
    path('admin/', admin.site.urls),
    path(_(''), include('App.urls', namespace=_('app'))),
    path(_('user/'), include('User.urls', namespace=_('user'))),
    path(_('food/'), include('Food.urls', namespace=_('food'))),
    path(_('favorite/'), include('Favorite.urls', namespace=_('favorite'))),
]