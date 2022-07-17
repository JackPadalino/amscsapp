from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
#from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',include('main.urls')),
    path('classroom/',include('classroom.urls')),
    path('users/',include('users.urls')),
    #path('users/',include('users.urls')),
    #path('users/login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='users-login'),
    #path('users/logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='users-logout'),
    #path('users/password-reset/',auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),name='password_reset'),    #path('users/password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'),
    #path('users/password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),
    #path('users/password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='password_reset_complete'),
    #path('users/register/',user_views.register,name='users-register'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)