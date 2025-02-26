from django.urls import path, include
from django.contrib import admin
from users.views import home  # Import from users app
from django.http import JsonResponse

def health_check_view(request):
    return JsonResponse({'status': 'ok'})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('health/', health_check_view),
    path('api/courses/', include('courses.urls')),
    path('', home, name='root-home'),
]