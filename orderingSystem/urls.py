"""orderingSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.urls import path
from orders import views as order_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', order_views.welcome_page),
    path('admin/', admin.site.urls),
    path('client/', order_views.show_articles),
    path('send_order/', order_views.send_order),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
