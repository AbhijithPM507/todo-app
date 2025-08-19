from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',views.signup),
    path('',views.signup),
    path('loginn/',views.loginn),
    path('todo/',views.todo),
    path('signout/',views.signout,name='signout'),
    path('edit_todo/<int:srno>',views.edit_todo,name='edit-todo'),
    path('delete_todo/<int:srno>',views.delete_todo),
]
