from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    """ home page """
    if request.method == 'POST':
        user_search = request.POST.get("research")
        return redirect("search", user_search)
    else:
        return render(request, 'favorites/index.html')


def legal(request):
    """ redirect legal notice"""
    return render(request, 'favorites/legal.html')