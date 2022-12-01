from django.urls import path
from . import views

urlpatterns = [
path('series/', views.index, name='series'),
path('series/del_ser/<int:id>',views.del_ser,name='del_ser'),
path('types/', views.list_type, name='types'),

path('series/update_ser/<int:id>', views.update_ser, name='update_ser'),
path('series/update_ser/update_ser_action/<int:id>',views.update_ser_action, name='update_ser_action'),

path('series/addSerie/', views.add, name='add'),
path('series/addSerie/add_ser/', views.add_ser, name='add_ser'),

path('users/', views.list_users, name='users'),
path('users/createUser/', views.create_compte, name='create_compte'),
path('users/createUser/add_user_action/', views.create_user_action,name='create_user_action'),

path('users/update_user/<int:id>', views.update_user,name='update_user'),
path('users/update_user/update_user_action/<int:id>',views.update_user_action, name='update_user_action'),

path('users/del_user/<int:id>', views.del_user, name='del_user'),

path('', views.connect, name='connect'),
path('login/', views.signIn, name='signIn'),
path('login/login/', views.signIn, name='signIn'),
path('disconnect/', views.signOut, name='disconnect'),
]