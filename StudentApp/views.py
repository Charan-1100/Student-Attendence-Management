from django.shortcuts import render


# Create your views here.
def StudentInterface(request):
    return render(request,'StudentInterface.html')

