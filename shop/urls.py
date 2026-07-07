from django.urls import path
from shop.views import index, about, contacts, product_list, product_detail, login_view, register_view, logout_view, cart, user_rents, user_profile, user_history, user_favorites, user_membership, user_wallet, user_settings


urlpatterns = [
    path("", index, name="home_page"),
    path("about/", about, name="about_page"),
    path("contacts/", contacts, name="contacts_page"),
    path("products/", product_list, name="products"),
    path("products/<int:pk>/", product_detail, name="product_detail"),
    path("login/", login_view, name="login_view"),
    path("register/", register_view, name="register_view"),
    path("logout/", logout_view, name="logout_view"),
    path("cart/", cart, name="cart_view"),

    #user
    path("user_cabinet/", user_profile, name="user_profile"),

    path("user_cabinet/rents", user_rents, name="user_rents"),
    path("user_cabinet/history", user_history, name="user_history"),
    path("user_cabinet/favorites", user_favorites, name="user_favorites"),
    path("user_cabinet/membership", user_membership, name="user_membership"),
    path("user_cabinet/wallet", user_wallet, name="user_wallet"),
    path("user_cabinet/settings", user_settings, name="user_settings"),

]
