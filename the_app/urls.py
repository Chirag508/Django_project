from django.urls import path
from . import views
from .views import productlist
# from .views import show_hello,customer_form_page,delete_customer_data,update_cutomeer_page
urlpatterns = [
    path('',views.show_home_page,name='home'),
    path('hello/',views.show_hello,name='helllo'),
    path('customer/',views.customer_form_page,name='customer_form'),
    path('customer/delete_customer/<int:id>',views.delete_customer_data,name='delete_customer'),
    path('customer/update_customer/<int:id>',views.update_cutomeer_page,name='update_customer'),
    path('news/',views.show_news,name='news'),
    path('screen_one/',views.show_screen_one,name='screen_one'),
    path('screen_two/',views.show_screen_two,name='screen_two'),
    path('sopping_page/',views.show_shoping_page,name='sopping_page'),
    path('sopping_page/cart/',views.show_cart,name='cart'),
    path('product/',productlist.as_view(),name='product-list'),
]
