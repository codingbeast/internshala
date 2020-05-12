
from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("intern.urls"),name="intern"),
    path('student/',include("accounts.urls"),name="accounts"),
    path('accounts/',include('allauth.urls')),
]
