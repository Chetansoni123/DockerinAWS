from django.shortcuts import render
from firstApp.models import UserModel
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        username = request.POST.get('username', False) 
        email = request.POST.get('email', False)
        mobile = request.POST.get('mobile', False)
        user = UserModel(username=username, email=email, mobile=mobile)
        user.save()
        messages.success(request, 'Your data has been saved')
        return render(request, 'firstApp/index.html')

    else:
        return render(request, 'firstApp/index.html')
def userdata(request):
    if request.method == "GET":
        username = request.GET.get('username')
        user = UserModel.objects.get(username=username)
        return render(request, 'firstApp/index.html', {'user':user})