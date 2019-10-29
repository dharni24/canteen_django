"""canteen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^view_menu/', 'canteen_app.views.view_menu', name = 'view_menu'),
    url(r'^index/', 'canteen_app.views.index', name = 'index'),
    url(r'^indexstu/', 'canteen_app.views.indexstu', name = 'indexstu'),
    url(r'^nextpage/', 'canteen_app.views.nextpage', name = 'nextpage'),
    url(r'^laceorder/', 'canteen_app.views.placeorder', name = 'placeorder'),
    url(r'^signup/', 'canteen_app.views.signup', name = 'signup'),
    url(r'^student/', 'canteen_app.views.student', name = 'student'),
    url(r'^wallet/', 'canteen_app.views.wallet', name = 'wallet'),
    url(r'^yourorder/', 'canteen_app.views.yourorder', name = 'yourorder'),
    url(r'^placeorder/', 'canteen_app.views.placeorder', name = 'placeorder'),
    url(r'^login_req/', 'canteen_app.views.login_req', name = 'login_req'),
    url(r'^place_req/', 'canteen_app.views.place_req', name = 'place_req'),
    url(r'^order_req/', 'canteen_app.views.order_req', name = 'order_req'),
    url(r'^add_money/', 'canteen_app.views.add_money', name = 'add_money'),
    url(r'^remove_money/', 'canteen_app.views.remove_money', name = 'remove_money'),
    url(r'^show_order/', 'canteen_app.views.show_order', name = 'show_order'),
    url(r'^remove_ord/', 'canteen_app.views.remove_ord', name = 'remove_ord'),
]

