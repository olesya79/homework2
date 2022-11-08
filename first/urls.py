"""first URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import to include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from seasons.views import months
# from seasons.views import season
# from seasons.views import winter
# from seasons.views import autumn
# from seasons.views import summer
# from seasons.views import spring

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<months>', months)
    # path('<seasons>', index)
    # path('season/', season),
    # path('season/winter', winter),
    # path('season/autumn', autumn),
    # path('season/summer', summer),
    # path('season/spring', spring),
]
