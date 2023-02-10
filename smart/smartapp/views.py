import re
from urllib import response
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import memberform, postform
from .models import member, Comment, MemberList
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate , login
import csv
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required
def member_csv(request):
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition'] ='attachment; filename=member.csv'
    members=member.objects.all()

    writer=csv.writer(response)

    writer.writerow(['firstname', 'lastname','others','gender', 'phone number', 'address', 'profession' ])

    # lines=['this is my world']
    lines=[]

    for mem in members:
        writer.writerow([mem.Firstname, mem.Lastname,mem.others,mem.gender, mem.phone,mem.address, mem.profession])

    
    return response


@login_required
def member_text(request):
    response=HttpResponse(content_type='text/plain')
    response['Content-Disposition'] ='attachment; filename=member.txt'
    members=member.objects.all()

    # lines=['this is my world']
    lines=[]

    for mem in members:
        lines.append(f'{mem.fname}\n {mem.lname} \n {mem.phone} ')

    response.writelines(lines)
    return response

def home(request):
    if request.method=="POST":
        postedform=postform(request.POST)
        if postedform.is_valid():
            postedform.save()
            return redirect('home')
        
    else:
        postedform=postform

    post=Comment.objects.all()
    return render(request, 'home.html', {'postedform':postedform, 'post':post} )


def about(request):
    members=MemberList.objects.all()
    context={'members':members}
    return render(request, 'about.html', context)


def events(request):
    return render(request, 'events.html')

def projects(request):
    return render(request, 'projects.html')

def addmember(request):
    submitted=False
    if request.method=="POST":
        form=memberform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/addmember/?submitted=True')

    else:
        form=memberform
        
        if 'submitted' in request.GET:
            submitted=True

    return render(request, 'addmember.html', {'form':form, 'submitted':submitted})

def drug(request):
    return render(request, 'drug.html' )


def advocacy(request):
    return render(request, 'advocacy.html')

def pall(request):
    return render(request, 'pall.html')

def ust(request):
    return render(request, 'ust.html')

def environ(request):
    return render(request, 'environ.html')

def others(request):
    return render(request, 'others.html')


def contact(request):
    return render(request, 'contact.html')



def search(request):
    if request.method=="POST":
        searched=request.POST['searched']
        serviced=member.objects.filter(Firstname__contains=searched)
        return render(request, 'search.html', {'searched':searched, 'serviced':serviced})
    else:
        return render(request, 'search.html')



def sershow(request, showid):
    show=member.objects.get(pk=showid)
    return render(request, 'memshow.html', {'show':show})


def article(request):
    return render(request, 'article.html')


def signin(request):
    if request.method=="POST":
        
        username=request.POST['username']
        
        password=request.POST['login-password']
        user=authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            
            return render(request, 'home.html' )
        else:
            
            return redirect('login')
            
    return render(request, 'login.html')




def api(request):
    return render(request, 'api.html')