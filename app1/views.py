from django.shortcuts import render

# Create your views here.
def wish(request):
    d={'name':'Ram','age':22}
    return render(request,'wish.html',context=d)