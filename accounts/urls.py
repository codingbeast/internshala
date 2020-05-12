from django.urls import path,include
from accounts import views
urlpatterns = [
    path('login/',views.login, name="login"),
	path('dashboard/',views.dashboard, name='dashboard'),
	path('personal_details/',views.personal_details,name='personal_details'),
]