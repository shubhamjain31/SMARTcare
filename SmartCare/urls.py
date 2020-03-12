"""SmartCare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from SmartCareApp import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.smartcare,name="smartcare"),
    # path('login/',views.login,name="login"),
    # path('logging/',views.logging,name="logging"),
    path('logout/',views.logout,name="logout"),
    # path('test/',views.test,name="test"),
    # path('check/',views.check,name="check"),
    path('smartcare/',views.smartcare,name="smartcare"),
    path('callcentre/',views.callcentre,name="callcentre"),
    path('callregister/',views.callregister,name="callregister"),
    # path('callsave/',views.callsave,name="callsave"),
    path('search/',views.search,name="search"),
    path('ordershow/<str:so>',views.ordershow,name="ordershow"),
    
    # path('searchorder/',views.searchorder,name="searchorder"),
    # path('searchloc/',views.searchloc,name="searchloc"),
    # path('searchmob/',views.searchmob,name="searchmob"),
    # path('searchname/',views.searchname,name="searchname"),
    path('order/<str:lno>',views.order,name="order"),
    path('newcalls/',views.newcalls,name="newcalls"),
    path('freecalls/',views.freecalls,name="freecalls"),
    path('blankcalls/',views.blankcalls,name="blankcalls"),
    path('pendingcalls/',views.pendingcalls,name="pendingcalls"),
    path('servicecentre/',views.servicecentre,name="servicecentre"),
    # path('callallot/',views.callallot,name="callallot"),
    path('callplanning/',views.callplanning,name="callplanning"),
    path('callupdate/',views.callupdate,name="callupdate"),
    # path('callupdateshow/',views.callupdateshow,name="callupdateshow"),
    # path('callupdation/',views.callupdation,name="callupdation"),
    path('vieworder/<str:so>',views.vieworder,name="vieworder"),
    # path('appdetailsadd/<str:lno>',views.appdetailsadd,name="appdetailsadd"),
    path('appdetails/<str:lno>',views.appdetails,name="appdetails"),
    path('viewdetail/<str:loc>',views.viewdetail,name="viewdetail"),
    path('calldetailsave/<str:sno>',views.calldetailsave,name="calldetailsave"),
    path('orderdetailsave/',views.orderdetailsave,name="orderdetailsave"),
    path('callplan/',views.callplan,name="callplan"),
    path('viewplan/',views.viewplan,name="viewplan"),
    path('viewvisit/',views.viewvisit,name="viewvisit"),
    path('contract/',views.contract,name="contract"),
    # path('contractform/',views.contractform,name="contractform"),
    path('contractsave/',views.contractsave,name="contractsave"),
    # path('contractbooksave/',views.contractbooksave,name="contractbooksave"),
    path('contractbook/',views.contractbook,name="contractbook"),
    path('visit/<str:so>',views.visit,name="visit"),
    path('visitsave/',views.visitsave,name="visitsave"),
    path('viewplanning/<str:sod>',views.viewplanning,name="viewplanning"),
    path('displayvisit/<str:sod>',views.displayvisit,name="displayvisit"),
    path('rating/',views.rating,name="rating"),
    path('feedback/',views.feedback,name="feedback"),
    # path('feedbacksave/',views.feedbacksave,name="feedbacksave"),
    path('royalty/<str:so>',views.royalty,name="royalty"),
    path('viewroyalty/<str:so>',views.viewroyalty,name="viewroyalty"),
    path('royaltysave/',views.royaltysave,name="royaltysave"),
    # path('contractresult/',views.contractresult,name="contractresult"),
    path('custdetail/',views.custdetail,name="custdetail"),
    # path('detailsupdate/',views.detailsupdate,name="detailsupdate"),
    path('custdetailsave/',views.custdetailsave,name="custdetailsave"),
    path('callclose/<str:so>',views.callclose,name="callclose"),
    # path('closesave/',views.closesave,name="closesave"),
    path('plainsummery/',views.plainsummery,name="plainsummery"),
    # path('plainsummarydownload/',views.plainsummarydownload,name="plainsummarydownload"),
    path('reports/',views.reports,name="reports"),
    path('visitreport/',views.visitreport,name="visitreport"),
    path('csvfile/',views.csvfile,name="csvfile"),
    path('report/',views.report,name="report"),
    # path('visitreportdwnld/',views.visitreportdwnld,name="visitreportdwnld"),

]
