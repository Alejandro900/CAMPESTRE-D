from django.shortcuts import render, redirect

def inicio(request):
    return render(request, 'home.html')



