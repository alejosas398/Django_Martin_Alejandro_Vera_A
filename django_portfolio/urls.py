from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from portafolio import views

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('tasks/', views.tasks, name='tasks'),
    path('task/create/', views.create_task, name='create_task'),
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
    path('task/<int:task_id>/complete/', views.Complete_task, name='complete_task'),
    path('task/<int:task_id>/delete/', views.Delete_task, name='delete_task'),
    path('logout/', views.signout, name='signout'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)