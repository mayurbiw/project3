from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register",views.register_view, name="register"),
    path("after_register",views.after_register_view, name="after_register"),
    path("addintoshoppingcart/<id>/<typeofItem>/<toppings>",views.addintoshoppingcart, name="addintoshoppingcart"),
    path("shoppingcart",views.shoppingcartview,name="shoppingcart"),
    path("placeorder",views.placeorder,name="placeorder"),
    path("afterorderplaced",views.afterorderplaced,name="afterorderplaced"),
    path("resetcart",views.resetcart,name="resetcart"),
    path("markcompleted/<orderid>",views.markcompleted,name="markcompleted"),
    
]
