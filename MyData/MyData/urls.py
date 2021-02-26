"""MyData URL Configuration

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
from django.contrib import admin
from django.urls import path
from getdata import views as getdata_views
from users import views as users_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', users_views.prueba),
    
    path('getdata/', getdata_views.Dashboard, name='Dashboard'),
    path('testAPI/getDailyReportTotals/', getdata_views.GetDailyReportsTotals, name = "test_getDailyReportTotals"),
    path('testAPI/GetLatestCountryDataBycode/', getdata_views.GetLatestCountryDataBycode, name = "test_GetLatestCountryDataBycode"),
    path('testAPI/GetDailyReportByCountryCode/', getdata_views.GetDailyReportByCountryCode, name = "test_GetDailyReportByCountryCode"),
    path('testAPI/getListOfCounties/', getdata_views.ListCountires, name="List_Countries" ),
    path('testAPI/GetTotalsWeek/', getdata_views.GetTotalsWeek, name="GetTotalsWeek" ),
    path('/GetCountries/', getdata_views.GetCountries, name="GetCountries" ),

    path('users/login/', users_views.login_view, name = 'login_view'),
    path('users/logout/', users_views.logout_view , name = 'logout_view'),
    path('users/singup/', users_views.singup_view, name = 'singup_view'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
 