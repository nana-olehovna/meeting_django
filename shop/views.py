from django.shortcuts import render
from django.http import HttpResponse
from .contexts import home_context, top_movies, about_info, directors, contacts_info, movies, user

# Create your views here.



def index(request):
    context = {
        "home": home_context,
        "top_movies": top_movies
    }
    return render(request, "shop/home.html", context)

def about(request):
    context = {
        "about": about_info,
        "directors": directors
    }
    return render(request, "shop/about.html", context)

def contacts(request):
    context = {
        "contacts": contacts_info
    }
    return render(request, "shop/contacts.html", context)

def product_list(request):
    context = {"movies": movies}
    return render(request, 'shop/products.html', context)

def product_detail(request, pk):
    for m in movies:
        if m["id"] == pk:
            context = {"movie" : m}
            return render(request, "shop/product_detail.html", context)
    return HttpResponse("<h1>Movie not found!</h1>")

def login_view(request):
    return render(request, "shop/login.html")

def register_view(request):
    return render(request, "shop/registration.html")

def logout_view(request):
    return HttpResponse("<h1>Here will be LOGOUT PAGE</h1>")

def cart(request):
    return render(request, "shop/cart.html")


#USER

def user_cabinet(request):
    context = {"user" : user}
    return render(request, "user_personal/user_cabinet.html", context)

def user_profile(request):
    context = {"user" : user}
    return render(request, "user_personal/user_profile.html", context)

def user_rents(request):
    context = {"user" : user}
    return render(request, "user_personal/user_rents.html", context)

def user_history(request):
    context = {"user" : user}
    return render(request, "user_personal/user_history.html", context)

def user_favorites(request):
    context = {"user" : user}
    return render(request, "user_personal/user_favorites.html", context)

def user_membership(request):
    context = {"user" : user}
    return render(request, "user_personal/user_membership.html", context)

def user_wallet(request):
    context = {"user" : user}
    return render(request, "user_personal/user_wallet.html", context)

def user_settings(request):
    context = {"user" : user}
    return render(request, "user_personal/user_settings.html", context)

