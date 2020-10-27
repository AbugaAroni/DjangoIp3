from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.home, name='Welcome'),
    re_path('authorprofile/(\d+)', views.view_user, name='view_userprofile'),
    path('new/project', views.new_project, name='new_project'),
    re_path('viewproject/(\d+)', views.view_project, name='view_project'),
    path('accounts/profile/', views.profile, name='user_profile'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
