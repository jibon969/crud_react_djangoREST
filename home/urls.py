from django.urls import path, include


urlpatterns = [
    path('', include('home.api.urls')),
    path('api/', include('home.api.urls'))
]