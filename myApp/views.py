from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    context={
        'name':'Dora',
        'age':24,
        'nationality':'Indian'
    }
    return render(request,'index.html',context)

