"""pur_beurre URL Configuration

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
from django.urls import path
from favorites import views, views_account, views_product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('legal/', views.legal, name='legal'),
    path('registration/', views_account.registration, name='registration'),
    path('account/', views_account.account, name='account'),
    path('login/', views_account.login_view, name='login'),
    path('logout/', views_account.logout_view, name='logout'),
    path('search/', views_product.search, name='search'),
    path('results/<int:product_id>/<query>', views_product.results, name='results'),
    path('detail/<int:product_id>/', views_product.detail_product, name='detail'),
    path('save/<int:product_id>/', views_product.save_substitute, name='save'),
    path('favorite/', views_product.favorites_page, name='favorite'),
]
