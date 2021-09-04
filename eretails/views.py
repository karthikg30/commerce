from django.shortcuts import render, redirect # basic render and redirect
from django.http import HttpResponse # to render as comment code
from .models import * # tables models
from .forms import * # fields taken 
from .filters import OrderFilter # making filters
from django.contrib.auth.forms import UserCreationForm # creating register page 
from django.contrib import messages #flash messages in the screen
from django.contrib.auth import authenticate, login, logout #for login and logut authentication
from django.contrib.auth.decorators import login_required #checking login before accessing pages
from .decoraters import userauthentic_register_login, admin_only
from django.contrib.auth.models import Group

# Create your views here.

@userauthentic_register_login
def register(request):
    creation_form = CreateUserForm()

    if request.method == "POST":
        save_form = CreateUserForm(request.POST)
        if save_form.is_valid():
            user = save_form.save()
            username = save_form.cleaned_data.get('username')
            group_set = Group.objects.get(name = "customer")
            user.groups.add(group_set)

            customer.objects.create(user=user, name=user.username,)

            messages.success(request, 'User has been created with username ' + username)
            return redirect('login')

    context = {'creation_form':creation_form}
    return render (request,'eretails/register.html', context)

@userauthentic_register_login
def loginpage(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect ('/')
        else:
            messages.info(request,'Username or Password is incorrect')

    return render (request, 'eretails/login.html')
    #return HttpResponse(request, 'login')

def logoutpage(request):
    logout(request)
    return redirect('login')

@login_required(login_url= 'login')
@admin_only
def home(request):
    orders = order.objects.all()
    Pending = order.objects.filter(status = "Pending").count()
    Total_orders = order.objects.count()
    orders_delivered = orders.filter(status= "Delivered").count()
    customers_list = customer.objects.all()

    return render (request,'eretails/dashboard.html', {'Pending': Pending, 'Total': Total_orders, 
    'orders_delivered': orders_delivered, 'orders':orders , 'customers_list': customers_list})

@login_required(login_url= 'login')
def product(request):
    product_list = products.objects.all()
    return render (request,'eretails/product.html', {'products':product_list})

@login_required(login_url= 'login')
def customer_vw (request, pk_test):
    customers = customer.objects.get(cust_id = pk_test)
    orders_list = customers.order_set.all()
    #order_count = orders_list.count() 
    #myFilter = OrderFilter()
    myFilter = OrderFilter(request.POST, queryset = orders_list )
    orders_list = myFilter.qs
    order_count = orders_list.count()
    
    context_cust = {'order_list': orders_list,'cust_in':customers, 'order_count':order_count, 'myFilter':myFilter }
    
    return render(request,'eretails/customer.html', context_cust)

@login_required(login_url= 'login')
def create_cust(request):
    custform = CustomerForm()

    if request.method == "POST":
        create_cust = CustomerForm(request.POST)

        if create_cust.is_valid():
            create_cust.save()
            return redirect ('/')

    context = {'custform': custform}
    return render (request, 'eretails/create_cust.html', context)

@login_required(login_url= 'login')
def update_cust(request, pk_up):
    
    update_cust = customer.objects.get(cust_id = pk_up)
    custform = CustomerForm(instance = update_cust) # form has been pre-filled

    if request.method == "POST":
        form = CustomerForm(request.POST, instance = update_cust)

        if form.is_valid():
            form.save()
            return redirect ('/')

    context = {'custform': custform}
    return render (request, 'eretails/create_cust.html', context)
    
@login_required(login_url= 'login')
def create_order(request, pk):

    customers = customer.objects.get(cust_id= pk)
    forms_ord = OrderForm(initial={'customers': customers})

    if request.method == "POST":
        form = OrderForm(request.POST)

        if form.is_valid():
            form.save()
            
            return redirect ("/")

    context = {'forms_ord': forms_ord}
    return render (request, 'eretails/orders_form.html', context)

@login_required(login_url= 'login')
def update_order(request, pk):

    orders_up = order.objects.get(id=pk)
    forms_up = OrderForm(instance = orders_up)

    if request.method == "POST":
        form = OrderForm(request.POST, instance=orders_up)
        if form.is_valid():
            form.save()
            
            return redirect ("/")

    context = {'forms_ord': forms_up}
    return render (request, 'eretails/orders_form.html', context)

@login_required(login_url= 'login')
def delete_order(request, pk_del):
    order_del = order.objects.get(id = pk_del)
    
    if request.method == "POST":
        order_del.delete()
        return redirect ("/")
    
    context = {'item': order_del}
    return render (request, 'eretails/delete_customer.html', context)

@login_required(login_url= 'login')
def userpage(request):
    orders = request.user.customer.order_set.all()
    Total = orders.count()
    orders_delivered = orders.filter(status='Delivered').count()
    Pending = orders.filter(status='Pending').count()

    context = {'orders':orders, 'Total': Total, 'orders_delivered':orders_delivered, 'Pending':Pending }

    return render (request, 'eretails/userpage.html', context)


'''
@login_required(login_url= 'Home')
def create_product(request):
    product_list = product.objects.all()
    pass
'''