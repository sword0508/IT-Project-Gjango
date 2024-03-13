from django.shortcuts import render


def index(request):

    return render(request, 'index.html')


def login(request):

    return render(request, 'login.html')

def profile(request):

    return render(request, 'profile.html')

def tour_details(request):

    return render(request, 'tour-details.html')
def des(request):

    return render(request, 'destination.html')
def tours(request):

    return render(request, 'tour.html')
def tes(request):

    return render(request, 'tes.html')

def faq(request):

    return render(request, 'faq.html')

def about(request):

    return render(request, 'about.html')

def blog(request):

    return render(request, 'blog.html')

def bd(request):

    return render(request, 'bd.html')
def cont(request):

    return render(request, 'cont.html')