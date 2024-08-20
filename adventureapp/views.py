from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request,'adventureapp/homepage.html')

def rigthpath(request):
    return render(request, 'adventureapp/rightpath.html')

def leftpath(request):
    return render(request, 'adventureapp/leftpath.html')

def blue(request):
    return render(request,'adventureapp/blue.html')

def green(request):
    return render(request,'adventureapp/green.html')

def safe(request):
    return render(request,'adventureapp/safe.html')

def open(request):
    return render(request,'adventureapp/open.html')

def close(request):
    return render(request,'adventureapp/close.html')

def forest(request):
    return render(request,'adventureapp/forest.html')

def park(request):
    return render(request,'adventureapp/park.html')

def safeopen(request):
    return render(request,'adventureapp/safeopen.html')

def safepark(request):
    return render(request,'adventureapp/safepark.html')

def bad(request):
    return render(request,'adventureapp/bad.html')

def line(request):
    return render(request,'adventureapp/line.html')

def go(request):
    return render(request,'adventureapp/go.html')

def going(request):
    return render(request,'adventureapp/going.html')

def neck(request):
    return render(request,'adventureapp/neck.html')

def back(request):
    return render(request,'adventureapp/back.html')

def love(request):
    return render(request,'adventureapp/love.html')

def win(request):
    return render(request,'adventureapp/win.html')
