from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'basic_app/index.html',{'text':'Hello world','num':100})
def other(request):
    return render(request,'basic_app/other.html')
def relative(request):
    return render(request,'basic_app/relative_url_templates.html')