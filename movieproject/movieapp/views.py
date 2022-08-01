from django.http import HttpResponse
from django.shortcuts import render, redirect

from movieapp.forms import MovieForms
from movieapp.models import movies
def addd(request):
    if request.method=='POST':
        name=request.POST.get('name')
        des = request.POST.get('description')
        year = request.POST.get('YOR')
        img=request.FILES['img']
        m1=movies(name=name,des=des,year=year,img=img)
        m1.save()
        return redirect('/')
    return render(request,"add.html")
def details(request,movie_id):
    # fetching method
    m=movies.objects.get(id=movie_id)
    return render(request,"detail.html",{"mv":m})
def index(request):
    muv=movies.objects.all()
    context={
        'movie_list':muv
    }
    return render(request,"index.html",context)
# Create your views here.
def update(request,id):
    movie=movies.objects.get(id=id)
    form=MovieForms(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'movie':movie,'form':form})

def delete(request,id):
    if request.method=='POST':
        movie=movies.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,"delete.html",)