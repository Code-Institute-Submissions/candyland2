"""CandyLand URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from accounts import views as accounts_views
from CandyLand_app import views as Candyland_app_views
from paypal_store import views as paypal_views
from paypal.standard.ipn import urls as paypal_urls
from products import views as product_views
from newsletter import views as newsletter_views


from CandyLand_app import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.get_home),
    url(r'^home/$', views.get_home),
    url(r'^base/$', views.get_home),
    url(r'^packages/$', views.get_packages),
    url(r'^gallery/$', views.get_gallery),
    url(r'^sweetlist/$', views.get_sweetlist),
    url(r'^bookus/$', views.get_bookus),
    url(r'^members/$', views.get_members),
    url(r'^register/$', accounts_views.register, name='register'),
    url(r'^profile/$', accounts_views.profile, name='profile'),
    url(r'^login/$', accounts_views.login, name='login'),
    url(r'^logout/$', accounts_views.logout, name='logout'),

    # PayPal URL's
    url(r'^a-very-hard-to-guess-url/', include(paypal_urls)),
    url(r'^paypal-return', paypal_views.paypal_return),
    url(r'^paypal-cancel', paypal_views.paypal_cancel),

    # Product URL's
    url(r'^products/$', product_views.all_products),
    # Newsletter URL's
    url(r'^newsletter/$', newsletter_views.all_newsletter),
]