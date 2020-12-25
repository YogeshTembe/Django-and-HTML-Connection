from django.shortcuts import render
from subprocess import run,PIPE
import sys

def output(request):
    data="Yogi"
    print("Yogesh")
    return render(request,'page2.html',{'data':data})

def button(request):
    return render(request,'page2.html')

def external(request):
    inp=request.POST.get("param")
    out=run([sys.executable,'C:\\Users\\Rakesh Tembe\\Desktop\\PyExternalScript.py',inp],shell=False,stdout=PIPE)
    print(out)
    return render(request,'page2.html',{'data1':out.stdout})