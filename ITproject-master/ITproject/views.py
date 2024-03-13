from django.shortcuts import render


def index(request):

    return render(request, 'index.html')


def login(request):

    return render(request, 'login.html')

def profile(request):

    return render(request, 'profile.html')

def tour_details(request):

    return render(request, 'tour-details.html')
