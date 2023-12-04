from django.contrib import admin
from django.urls import path, include
from accounts.views import custom_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/logout/', custom_logout, name='account_logout'),  # Override the allauth logout URL
    path('accounts/', include('allauth.urls')),
    path('', include('app.urls')),
]
