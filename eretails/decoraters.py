from django.http import HttpResponse
from django.shortcuts import render , redirect

def userauthentic_register_login (view_func):
    def  wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('homepage')
        else:
            return view_func(request, *args, **kwargs)
        
    return wrapper_func
    
'''
def allowed_user(allowed_user = []):
    def decorator (view_function):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_user:
                return view_function(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page')
        return wrapper_func
    return decorator
'''

def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        
        if group == "customer":
            return redirect("userpage")
        
        if group == "admin":
            return view_func(request, *args, **kwargs)
        
        else:
            #return redirect('login')
            print (request.user.groups)
            return HttpResponse('Please map user with role in admin screen /n Contact Admin dept')

    return wrapper_func