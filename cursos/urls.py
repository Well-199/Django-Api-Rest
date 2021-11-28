from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # api/ recebe todas os endpoints do meu projeto
    path('api/', include('api.urls')),

    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls'))
]
