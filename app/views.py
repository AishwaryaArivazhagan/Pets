from django.shortcuts import render,redirect
from .models import *
import sweetify
from django.shortcuts import get_object_or_404


def home(request):
    if 'name' in request.session:
        q=Products.objects.all()
        c=Categories.objects.all()
        return render(request,'home.html',{'Data':q,'a':c,'session':request.session['name']})
    else:
        q=Products.objects.all()
        c=Categories.objects.all()
        return render(request,'home.html',{'Data':q,'a':c,'session':None})

def register(request):
    if request.method=='POST':
        n=request.POST.get('name')
        nu=request.POST.get('num')
        em=request.POST.get('email')
        pd=request.POST.get('pass')
        print(n,nu,em,pd)

        obj=signup()
        obj.nam=n
        obj.numb=nu
        obj.ema=em
        obj.pwd=pd
        obj.save()
        return redirect('home')
    return render(request,'register.html')

def login(request):
    if request.method=="POST":
        n=request.POST.get('name')
        p=request.POST.get('pass')
        print(n,p)

        a=signup.objects.get(nam=n)
        if a.pwd==p:
            request.session["name"]=n
            sweetify.success(request,"Successfully logged in!",button='Done')
            return redirect('home')
        else:
            sweetify.error(request,"Username or Password incorrect",button='Try again')
            return render(request,'login.html')
    return render(request,'login.html')

def logout(request):
    if 'name' in request.session:
        del request.session['name']
        return redirect('home')
     
def product(request,id):
    if 'name' in request.session:
        pr=Products.objects.filter(category_id=id)
        c=Categories.objects.all()
        return render(request,'product.html',{'product':pr,'a':c,'session':request.session['name']})
    else:
        pr=Products.objects.filter(category_id=id)
        c=Categories.objects.all()
        return render(request,'product.html',{'product':pr,'a':c,'session':None})

def shop_detail(request,id):
    p=Products.objects.filter(pid=id)   
    if 'name' in request.session:
        u=signup.objects.get(nam=request.session['name'])
        uid=u.id
        quan=1
      
        # c=Cart.objects.get(user_id=uid,products_id=id)
        # quan=c.quantity
   
        return render(request,'shop_details.html',{'shop':p,'quantity':quan})
    else:
        return redirect('login')

def cart(request,id):
    if 'name' in request.session:
        u=signup.objects.get(nam=request.session['name'])
        ca=Cart.objects.all().filter(user_id=u.id)
        if request.method=="POST":
             u=signup.objects.get(nam=request.session['name'])
             uid=u.id
             product=Products.objects.get(pid=id)
             quantity=request.POST.get('quan')
             q=int(quantity)
             total_price=product.price*q
             cr=[]
             c=Cart.objects.all().filter(user_id=uid)
             for i in c:
                 cr.append(i.products.name)
             if product.name in cr:
                 Cart.objects.filter(user_id=uid,products_id=id).update(quantity=quantity,total=total_price)
             else:
                 a=Cart(user_id=uid,products_id=id,quantity=quantity,total=total_price)
                 a.save()
        return redirect('viewcart')
    else:
        return redirect('login')


def view_cart(request):
    if 'name' in request.session:
        try:
            user=signup.objects.get(nam=request.session['name'])
            cart_items=Cart.objects.filter(user_id=user.id)
            total_price = sum(item.total for item in cart_items)
            return render(request,'cart.html',{'session':request.session['name'],'carts':cart_items,'total_price':total_price})
        except signup.DoesNotExist:
            return render(request,'cart.html',{'session':None,'Error':'User not found'})
        except Cart.DoesNotExist:
            return render(request,'cart.html',{'session':request.session['name'],Exception:'Your cart is empty'})

    else:
        return render(request,'cart.html',{'session':None})
    

def incre(request,id):
    prod=get_object_or_404(Products, name=id)
    try:
        cart_item=Cart.objects.get(products=prod.pid)
        cart_item.quantity+=1
        cart_item.total = cart_item.quantity * cart_item.products.price
        cart_item.save()
    except Cart.DoesNotExist:
        return redirect('viewcart',{'Error':'Cart item not found'})
    return redirect('viewcart')
def decre(request,id):
    prod=get_object_or_404(Products,name=id)
    try:
        cart_item=Cart.objects.get(products=prod.pid)
        cart_item.quantity-=1
        cart_item.total=cart_item.quantity * cart_item.products.price
        cart_item.save()
    except Cart.DoesNotExist:
        return redirect('viewcart',{'Error':'Cart item is not found'})
    return redirect('viewcart')

def beagle(request):
    return render(request,'beagle.html')
