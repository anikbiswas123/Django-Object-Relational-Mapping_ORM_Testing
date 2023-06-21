
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',include('app.url')),
    # path('',include('app1.url')),
    # path('',include('app3.url')),
    # path('',include('app4.url')),
    path('',include('M_T_M.url')),
 
]
