from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

movies = [
    {
        "id": 1,
        "title": "Pulp Fiction",
        "year": 1994,
        "price": 79,
        "description": "A nonlinear crime story about intersecting lives of criminals in Los Angeles.",
        "rating": 8.5,
        "isInStock": True
    },
    {
        "id": 2,
        "title": "Kill Bill: Vol. 1",
        "year": 2003,
        "price": 69,
        "description": "A revenge-driven assassin embarks on a brutal mission against her former team.",
        "rating": 6.2,
        "isInStock": False
    },
    {
        "id": 3,
        "title": "The Hateful Eight",
        "year": 2015,
        "price": 89,
        "description": "Strangers trapped in a cabin during a blizzard reveal hidden motives and tensions.",
        "rating": 8.8,
        "isInStock": True
    },
    {
        "id": 4,
        "title": "Inglourious Basterds",
        "year": 2009,
        "price": 89,
        "description": "A group of Jewish-American soldiers plans to assassinate Nazi leaders in WWII France.",
        "rating": 10.0,
        "isInStock": True
    },
    {
        "id": 5,
        "title": "Django Unchained",
        "year": 2012,
        "price": 99,
        "description": "A freed slave teams up with a bounty hunter to rescue his wife from a plantation owner.",
        "rating": 9.5,
        "isInStock": True
    }
]

def index(request):
    return render(request, "shop/home.html")

def about(request):
    return render(request, "shop/about.html")

def contacts(request):
    return render(request, "shop/contacts.html")

def product_list(request):
    context = {
        "movies": movies
        }
    return render(request, 'shop/products.html', context)

def product_detail(request, pk):
    for m in movies:
        if m['id'] == pk:
            return HttpResponse(f"The movie title: {m["title"]} <br> The year: {m['year']} <br> The price for renting: {m['price']} <br> {m['id']}")
    return HttpResponse("<h1>Movie not found!</h1>")

def login_view(request):
    return render(request, "shop/login.html")

def register_view(request):
    return render(request, "shop/registration.html")

def logout_view(request):
    return HttpResponse("<h1>Here will be LOGOUT PAGE</h1>")

def cart(request):
    return render(request, "shop/cart.html")

def user_cabinet(request):
    return render(request, "shop/user_cabinet.html")