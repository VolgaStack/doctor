from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^doctor/', include('doctor.urls', namespace="doctor-app")),
    url(r'^admin/', include(admin.site.urls)),
    ]
