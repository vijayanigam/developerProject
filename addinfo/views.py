from django.shortcuts import render
# Create your views here.
def pagenotfound(request,pk):
    return render(request, 'add/index2.html', {'val': 'pagenotfound'})


def add(request):
    return render(request, 'add/register.html')
def home(request):
    return render(request, 'home.html')