from django.shortcuts import render
from .forms import UserRegistration
from django.contrib.auth.models import User
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST or None)
        check = User.objects.exclude(username='admin')
        print(check)
        print(form)
        if form.is_valid():

            new_user = form.save(commit=False)
            new_user.set_password(
                form.cleaned_data.get('password')
            )
            new_user.save()
            return render(request, 'register_done.html', {'user': check})
    else:

        # Create your views here.
        form = UserRegistration()
    context = {
        "form": form
    }
    return render(request, 'add/register.html', context=context)
#
# def index(request):
#     print(request.user)
#     return render(request, 'add/index.html')
# Create your views here.
def notloggedin(request):
    return render(request, 'edit/notloggedin.html')
