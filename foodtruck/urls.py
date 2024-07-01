"""foodtruck URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.first),
    path('index',views.index),
    path('reg/',views.reg),
    path('reg/userreg',views.userreg),
    path('login/',views.login),
    path('login/addlogin',views.addlogin),
    path('addlogin',views.addlogin),
    path('logout/',views.logout),
    path('truck',views.truck),
    path('addtruck',views.addtruck),
    path('viewtruck',views.viewtruck),
    path('viewuser',views.viewuser),
    path('userprofile',views.userprofile),
    path('category',views.category),
    path('addcategory',views.addcategory),
    path('food',views.food),
    path('addfood',views.addfood),
    path('viewfood',views.viewfood),
    path('charity',views.charity),
    path('addcharity',views.addcharity),
    path('viewcharity',views.viewcharity),
    path('truckprofile',views.truckprofile),
    path('viewfood_truck',views.viewfood_truck),
    path('charityprofile',views.charityprofile),
    path('charityaccept/<int:id>',views.charityaccept),
    path('charityreject/<int:id>',views.charityreject),
    path('viewfood_charity',views.viewfood_charity),
    path('foodreqtoadmin/<int:id>',views.foodreqtoadmin),
    path('foodreqtoadmin/addfoodreq/<int:id>',views.addfoodreq),
    path('viewreqfood',views.viewreqfood),
    path('foodaccept/<int:id>',views.foodaccept),
    path('foodreject/<int:id>',views.foodreject),
    path('assigntruck/<int:id>',views.assigntruck),
    path('assigntruck/assignwork/<int:id>',views.assignwork),
    path('viewrequest',views.viewrequest),
    path('truckaccept/<int:id>',views.truckaccept),
    path('truckreject/<int:id>',views.truckreject),
    path('delivery/<int:id>',views.delivery),
    path('delivery/adddelivery/<int:id>',views.adddelivery),
    path('truckstatus',views.truckstatus),
    path('product',views.product),
    path('addproduct',views.addproduct),
    path('viewproduct',views.viewproduct),
    path('viewproduct_user',views.viewproduct_user),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('view_cart/addquantity/<int:id>', views.addquantity, name='addquantity'),
     path('view_cart/',views.view_cart),
     path('buy_all',views.buy_all, name='buy_all'),
     path('purchase',views.purchase, name='purchase'),
     path('viewuserrewards',views.viewuserrewards),
     path('viewreward',views.viewreward),
     path('allocated_charity',views.allocated_charity),
     path('vieworders',views.vieworders),
     path('vieworders_admin',views.vieworders_admin),
     path('vieworders_truck',views.vieworders_truck),
     path('vieworders_charity',views.vieworders_charity),
     path('viewallocatedtruck',views.viewallocatedtruck),
     path('addfeed',views.addfeed, name='addfeed'),
     path('view_feedbacks',views.view_feedbacks, name='view_feedbacks'),
     path('addcomplaint',views.addcomplaint, name='addcomplaint'),
     path('view_complaint',views.view_complaint, name='view_complaint'),
     path('reply/<int:id>',views.reply),
     path('reply/addrply/<int:id>',views.addrply),
     path('view_complaint_charity',views.view_complaint_charity),
     path('view_cart/remove_cart_item/<int:id>',views.remove_cart_item),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
