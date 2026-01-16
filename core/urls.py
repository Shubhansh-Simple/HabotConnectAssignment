# django
from django.contrib import admin
from django.urls import path, include

# simplejwt
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    # for admin site
    path('admin/', admin.site.urls),

    # for login
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    # for employees
    path('api/', include('employees.apis.urls')),
]
