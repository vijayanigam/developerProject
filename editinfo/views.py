from django.shortcuts import render
from django.contrib.auth.models import User
# from .models import DeveloperRepository, Technology, Domain
from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import render,redirect
from editinfo.models import Developer, Q_A, Technology, Domain, Blog,Project
from editinfo import forms
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
#

def delete(request):
    id = request.POST.get('ID')
    print(id)
    data = Developer.objects.get(id=id)
    data.delete()
    developer = Developer.objects.all()
    return render(request, 'add/index.html', {'data': developer})


# @login_required(login_url='/auth/notloggedin/')
def search(request):
    if request.method == 'POST':
        try:
            tech = request.POST.get('technology')
            domain_ = request.POST.get('domain')
            location = request.POST.get('location')
            domain = Domain.objects.get(name=domain_)
            technology = Technology.objects.get(name=tech)
            dav = Developer.objects.filter(technology=technology,location=location)
            dav1 = Developer.objects.filter(technology=technology, location=location)
            loc = Developer.objects.filter(location=location)
            dom = Developer.objects.filter(domain=domain,location=location)
            print(dav1)
        except:
            return render(request, 'add/index2.html', {'val':'no_search'})
        else:
            dav = dav|loc|dom
            print(technology, dav.distinct())
            dav = dav.distinct()
            return render(request, 'edit/searched_data.html', {'data': dav, 'tech': tech, 'domain':domain_,'loc':location})
    return render(request, 'edit/search.html')

# @login_required(login_url='/auth/notloggedin/')
def get_weightage(request):
    if request.method == 'POST':
        project = int(request.POST.get('project'))
        blog = int(request.POST.get('blog'))
        qa = int(request.POST.get('qa'))
        data = pass_score_values(qa, blog, project)
        return render(request, 'add/index.html', {'data': data})
    return render(request, 'edit/weightage.html')


def pass_score_values(q=25, b=25, p=50):
    developer = Developer.objects.all()
    for i in developer:
        data = Developer.objects.get(id=i.id)
        # print('%%%%%%%%%%%%',i.id)
        final_score = score(i.id, q, b, p)
        data.score = (final_score * 100) / 5
        # print(data.score)
        data.save()
    data = Developer.objects.all()
    return data


def score(id,t=25,b=25,p=50):
    ps, ts, bs, c = 0, 0, 0, 0
    data = Developer.objects.get(id=id)
    tech = data.q_a.all()
    blog = data.blog.all()
    project = data.project.all()
    for i in project:
        ps = ps+i.rating
        c = c+1
    # print('okp',ps, c)
    ps = ((ps/c)*(p/100))
    c = 0
    # print('okp', ps, c,'okayau',p)
    for i in tech:
        ts=ts+i.rating
        c=c+1
    ts=((ts/c)*(t/100))
    c=0
    for i in blog:
        bs=bs+i.rating
        c=c+1
    bs=((bs/c)*(b/100))
    c=0
    # print(bs+ts+ps,bs,ts,ps)
    return bs+ts+ps


# @login_required
# @login_required(login_url='/auth/notloggedin/')
def show_data(request):
    data = pass_score_values()
    return render(request, 'add/index.html', {'data': data})


# @login_required(login_url='/auth/login/')
def edit(request):
    form = forms.DeveloperForm()
    # print(request.user)
    # if request.user:
    #     print('true')
    if request.method == 'POST':
        form = forms.DeveloperForm(request.POST)
        if form.is_valid():
            mail = form.cleaned_data['email']
            name = form.cleaned_data['name']
            obj = list(Developer.objects.filter(email=mail))
            obj1 = list(Developer.objects.filter(name=name))
            print(obj)
            if len(obj)<1 and len(obj1)<1:
                print(obj)
                print("Inside ")
                form.save()
                a = form.cleaned_data
                print('aaaaaaaaaaaaaaaa', a)
                form = forms.DeveloperForm()
                #######################
                data = pass_score_values()
                print("developer added")

                return render(request, 'add/index.html', {'data':data})
                # return render(request, 'add/index.html', {'x': a})
            else:
                return render(request, 'add/index2.html', {'form': form, 'val': 'user_exist'})

    return render(request, 'edit/userform.html', {'form': form, 'val': 'add'})


# @login_required(login_url='/auth/login/')
def editdata(request):
    id = request.POST.get('ID')
    print(id)
    instance = Developer.objects.get(id=id)
    print(instance)
    if request.method == "POST":
        form = forms.DeveloperForm(request.POST,instance=instance)
        if form.is_valid():
            # print(id, 'inside')
            form.save()
            data = Developer.objects.get(id=id)
            # print('%%%%%%%%%%%%', id)
            final_score = score(id)
            data.score = (final_score * 100) / 5
            # print(data.score)
            data.save()
            developer = Developer.objects.all()
            return render(request,'add/index.html',{'data':developer})

    form = forms.DeveloperForm(instance=instance)
    return render(request, "edit/userform.html", {'form':form ,'id_':id, 'val': 'edit'})

# user = {}
    # print(request.user)
    # user_name = str(request.POST.get('username'))
    # user_ = User.objects.all()
    # # user = User.objects.filter(username=user_name)
    # for i in user_:
    #     if i.username == user_name:
    # #         user = i
    # print("----------------------------------------", user)
    # return render(request, 'edit/userform.html', {"band": user})

# def user_form(request):
#     username = request.POST.get('username')
#     email = request.POST.get('email')
#     experience = request.POST.get('experience')
#     technology = request.POST.get('technology')
#     domain = request.POST.get('domain')
#     t = Technology(technology=technology)
#     d = Domain(domain=domain)
#     d.save()
#     t.save()
#     m=DeveloperRepository(first_name=first_name,last_name=last_name,username=username,email=email,experience=experience,domain=domain,technology=technology)
#
#     m.save()
#     print(u)
#     return render(request, 'add/index.html')
# def user_form2(request):
#     user={}
#     return render(request, 'home.html')
#
# def update_record(request,id):
#     if request.method == 'POST':
#         pi = emp_details.objects.get(id=id)
#         fm=employeeRegistration(request.POST,instance=pi)
#         if fm.is_valid():
#             fm.save()
#
#     else:
#         pi = emp_details.objects.get(id=id)
#         fm = employeeRegistration(instance=pi)
#     return render(request,'update.html',{'id':id,'form':fm})




