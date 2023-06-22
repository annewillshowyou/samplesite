from django.contrib import admin
from bboard.views import index
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bboard/', include('bboard.urls'))
]