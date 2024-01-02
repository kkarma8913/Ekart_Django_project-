from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

from .forms import *


# Create your views here.

# authentication

def sign_up(request):
    if request.method == 'POST':
        myform = CustomerRegistrationForm(request.POST)
        if myform.is_valid():
            myform.save()
            messages.success(request,"You are Successfully Registered")
            return redirect('log_in')
        else: 
            messages.error(request,"Something went wrong")   
            return render(request, 'sign_up.html',{'myform':myform})    
    else:
        myform = CustomerRegistrationForm()
        return render(request, 'sign_up.html',{'myform':myform})
    
#===============================================================================    

def log_in(request):
    if request.method == 'POST':
        myform = AuthenticationForm(data = request.POST)
        if myform.is_valid():
            uname = myform.cleaned_data['username']
            upass = myform.cleaned_data['password']

            user = authenticate(username=uname,password = upass)
            if user:
                login(request,user)

                request.session['uname'] = uname
              
                return redirect('home')
            else:
                return render(request, 'log_in.html',{'myform':myform})
        else:
            messages.error(request,"Invalid username or password")
            return render(request, 'log_in.html',{'myform':myform})    
    else:
        myform = AuthenticationForm()
        return render(request, 'log_in.html',{'myform':myform})
    
#====================================================================================    

def log_out(request):
    logout(request)
    return redirect('log_in')


#========================================================================================

def home(request):
    cat_data = Category.objects.all()
    return render(request,'base.html',{'cat_data':cat_data})

def show_products(request,id):
    cat_obj = Category.objects.get(id = id)
    product_data = Product.objects.filter(pro_category = cat_obj)
    cat_data = Category.objects.all()

    if request.method == 'POST':
        # product id
        pro_id = request.POST['pro_id']  # "c101"
        # product obj 
        pro_obj = Product.objects.get(pro_id = pro_id)
        # qty
        qty = request.POST['quantity']  # string
        

        # user data who is loged in
        user = request.user
        try:
            customer = Customer.objects.get(user = user)
            # total price
            total_price = int(pro_obj.pro_price) * int(qty)

            cart_obj = Cart(customer = customer, product = pro_obj, qty = qty, total_price=total_price)
            cart_obj.save()
            messages.success(request,"Successfully added to cart")
        except Exception as e:
            messages.error(request,"please resgister first")    
        return render(request,'show_product.html',{'cat_obj':cat_obj,'cat_data':cat_data,'product_data':product_data})
    else:
        return render(request,'show_product.html',{'cat_obj':cat_obj,'cat_data':cat_data,'product_data':product_data})


#===================================================================



def show_cart(request):
    cat_data = Category.objects.all()
    user = request.user
    customer = Customer.objects.get(user = user)
    cart_data = Cart.objects.filter(customer = customer)

    total_sum = 0
    quantity = 0

    for cart in cart_data:
        total_sum = total_sum + cart.total_price  # 0 + 90000 + 1600 =91600 
        quantity = quantity + cart.qty            # 0 + 4 +2 = 6




    return render(request,'show_cart.html',{"cart_data":cart_data,'cat_data':cat_data,'total_sum':total_sum,'quantity':quantity})

# ============================================================================

def cart_item_delete(request,id):

    cart_obj = Cart.objects.get(id = id)
    
    cart_obj.delete()

    return redirect('show_cart')

# ===============================================================================

# 


import datetime

def order(request):
    payment_mode = request.POST['pay']
    user = request.user
    customer = Customer.objects.get(user = user)   
    cart_data = Cart.objects.filter(customer = customer)
    order_date = datetime.date.today()

    for i in cart_data:

        order_obj = Order(customer = customer,product=i.product,qty = i.qty,payment_mode=payment_mode,total_price = i.total_price,order_date = order_date)
        order_obj.save()

        i.delete()



        
    return redirect('show_cart')


# ====================================================================================

def show_order(request):

    user = request.user
    customer = Customer.objects.get(user = user)
    order_data = Order.objects.filter(customer = customer)

    return render(request,'show_order.html',{'order_data':order_data})

#=========================================================================================

def add_customer(request):
    if request.method == 'POST':
        id = request.POST['id']   # ""
        user = request.user
        name = request.POST['name']
        mobile_no = request.POST['mobile_no']
        email = request.POST['email']
        gender = request.POST['gen']
        age    = request.POST['age']

        # Create
        if id == "":
            obj1 = Customer(user=user,name=name,mobile_no=mobile_no,email=email,gender=gender,age=age)
            obj1.save()
            
        # Update
        else:
            obj1 = Customer(id = id,user=user,name=name,mobile_no=mobile_no,email=email,gender=gender,age=age)
            obj1.save()  

        messages.success(request,"Customer Successfully Registered")
        return redirect("home")
    else:
        user = request.user     # yash
        customer = Customer.objects.filter(user = user).first()  # yash registered in customer table

        if customer:
            return render(request,'add_customer.html',{'data':customer})
        else:
           return render(request,'add_customer.html')
    
#===============================================================================================    
    


def sort_by(request):

    id = request.POST['cat']
    cat_obj = Category.objects.get(id = id)
    cat_data = Category.objects.all()

    try:
        data = request.POST['sort_by']
        
        if data == "lh":
            product_data = Product.objects.filter(pro_category = cat_obj).order_by('pro_price')
        elif data == "hl":
            product_data = Product.objects.filter(pro_category = cat_obj).order_by('-pro_price')   
        else:
            product_data = Product.objects.filter(pro_category = cat_obj) 
    except Exception as e:
           product_data = Product.objects.filter(pro_category = cat_obj)         
    return render(request,'show_product.html',{'cat_obj':cat_obj,'cat_data':cat_data,'product_data':product_data})

# ============================================================================

def search(request):
    cat_data = Category.objects.all()

    name = request.POST['name']

    product_data = Product.objects.filter(pro_title__contains = name) 
    
    return render(request,'show_product.html',{'cat_data':cat_data,'product_data':product_data})

      



