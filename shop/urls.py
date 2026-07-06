from django.urls import path
from shop.views import index, about, contacts, product_list, product_detail, login_view, register_view, logout_view, cart, user_cabinet


urlpatterns = [
    path("", index, name="home_page"),
    path("about/", about, name="about_page"),
    path("contacts/", contacts, name="contacts_page"),
    path("products/", product_list, name="products"),
    path("products/<int:pk>/", product_detail, name="product_detail"),
    path("login/", login_view, name="login_view"),
    path("register/", register_view, name="register_view"),
    path("user_cabinet/", user_cabinet, name="user_cabinet"),
    path("logout/", logout_view, name="logout_view"),
    path("cart/", cart, name="cart_view"),
]
