from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

movies = [
    {
        "id": 1,
        "title": "Pulp Fiction",
        "year": 1994,
        "price": 79
    },
    {
        "id": 2,
        "title": "Kill Bill: Vol. 1",
        "year": 2003,
        "price": 69
    },
    {
        "id": 3,
        "title": "The Hateful Eight",
        "year": 2015,
        "price": 89
    },
    {
        "id": 4,
        "title": "Inglourious Basterds",
        "year": 2009,
        "price": 89
    },
    {
        "id": 5,
        "title": "Django Unchained",
        "year": 2012,
        "price": 99
    }
]

def index(request):
    return HttpResponse("<h1>Here will be THE MAIN PAGE</h1>")

def about(request):
    return HttpResponse("<h1>Here will be ABOUT PAGE</h1>")

def contact(request):
    return HttpResponse("<h1>Here will be CONTACT PAGE</h1>")

def product_list(request):
    text = f"<h1>The movies you can rent:</h1> <br>"
    for m in movies:
        text += f"{m['title']}: {m['price']} CZK <br>"
    return HttpResponse(text)

def product_detail(request, pk):
    for m in movies:
        if m['id'] == pk:
            return HttpResponse(f"The movie title: {m["title"]} <br> The year: {m['year']} <br> The price for renting: {m['price']} <br> {m['id']}")
    return HttpResponse("<h1>Movie not found!</h1>")

def login_view(request):
    return HttpResponse("<h1>Here will be LOGIN FORM</h1>")

def register_view(request):
    return HttpResponse("<h1>Here will be REGISTRATION FORM</h1>")

def logout_view(request):
    return HttpResponse("<h1>Here will be LOGOUT PAGE</h1>")