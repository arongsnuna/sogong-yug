from django.contrib import admin
from django.urls import path, include
from snsapp import views
from accounts import views as accounts_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.main, name='main'),
    path('home/', views.home, name='home'),

    path('postcreate/', views.postcreate, name='postcreate'),
    path('detail/<int:post_id>', views.detail, name='detail'),
    path('remove/<int:post_id>', views.remove, name='remove'),
    path('edit/<int:post_id>', views.edit, name='edit'),

    path('login/', accounts_views.login, name='login'),
    path('logout/', accounts_views.logout, name='logout'),
    path('signup/', accounts_views.signup, name='signup'),
    
    path('accounts/', include('allauth.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)