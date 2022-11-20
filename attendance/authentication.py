from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render


# def Login(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         # Redirect to a success page.
#     else:
#         # Return an 'invalid login' error message.
#         ...
#     return render(request, "registration/login.html")
#
#
def Logout(request):
    return logout(request)
