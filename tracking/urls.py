from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('add/',views.add_cattle,name='add'),
    path('update/<str:pk>/',views.update_cattle,name='update'),
    path('viewfarmerlist/',views.view_farmerlist,name='viewfarmerlist'),
    path('delete/<str:pk>/',views.delete_cattle,name='delete'),
    path('addfarmer/',views.add_farmer,name='addfarmer'),
    path('updatefarmer/<str:pk>/',views.update_farmer,name='updatefarmer'),
    path('viewcattle/<str:pk>/',views.view_cattle,name='viewcattle'),
    path('deletefarmer/<str:pk>/',views.delete_farmer,name='deletefarmer'),
    path('login/',views.logInPage,name='login'),
    path('register/',views.registerPage,name='register'),
    path('logout/',views.logOutUser,name='logout'),
    # path('live_tracking/', views.live_tracking, name='live_tracking'),
    path('viewfarmer/<str:pk>/',views.viewfarmer,name='viewfarmer'),
    path('map/<str:pk>/', views.my_view, name='map'),
    path('cattleinfo/<str:pk>/',views.cattleinfo,name='cattleinfo'),
]

