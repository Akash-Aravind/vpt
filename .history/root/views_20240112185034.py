from django.shortcuts import render
from django.http import HttpResponse
from .models import DICT
from django.contrib.postgres.search import SearchVector,SearchQuery

#This function is for the path"/" i.e for the home page
def home(request):
    return render(request,"index.html")

def search_results(request):
    q=request.POST['txtinp']
    objs=DICT.objects.filter(key__icontains=q)
    secondobjs=DICT.objects.filter(values__icontains=q)
    return render(request,"searchresult.html",{"objs":objs,"secondobjs":secondobjs})
































    #This is more efficient way of querying from table but since the language is tamil we faced a lot of issues using vectors
    # q=request.POST['txtinp'];
    # vector=SearchVector("key")
    # query=SearchQuery(q, config='tamil')

    # objs=DICT.objects.annotate(search=vector).filter(key__icontains=query)
    # for i in objs:
    #     print(i)
    # return render(request,"searchresult.html",{"objs":objs})