from django.shortcuts import render,redirect
from django.views import View
from .models import *
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse

# def home(request):
#  return render(request, 'app/home.html')

class ProductViews(View):
 def get(self,request):
  topwears=Product.objects.filter(category='TW')
  bottomwears=Product.objects.filter(category='BW')
  mobiles=Product.objects.filter(category='M')
  return render(request ,'app/home.html',{'topwears':topwears,'bottomwears':bottomwears,'mobiles':mobiles})


# def product_detail(request):
#  return render(request, 'app/productdetail.html')
class ProductDetailView(View):
  def get(self,request,id):
   product=Product.objects.get(id=id)
   return render(request,'app/productdetail.html',{'product':product})

def add_to_cart(request):
 user = request.user
 Product_id = request.GET.get('prod_id')
 product=Product.objects.get(id=Product_id)
 Cart(user=user,product=product).save()
 return redirect('/cart')

def show_cart(request):
  if request.user.is_authenticated:
   user = request.user
   cart = Cart.objects.filter(user=user)
   amount=0.0
   shipping_amount=70.0
  
   cart_product = [p for p in Cart.objects.all() if p.user == user ]

   if cart_product:
      for p in cart_product:
        tempamount = (p.quantity * p.product.discounted_price)
        amount += tempamount
        totalamount= amount+shipping_amount 
      return render(request, 'app/addtocart.html',{'carts':cart,'amount':amount,'totalamount':totalamount})
   else:
    bottomwears = Product.objects.filter(category='TW')
    M = Product.objects.filter(category='M')
    BW = Product.objects.filter(category='BW')
    return render(request,'app/emptycart.html',{'bottomwears':bottomwears,'M':M,'BW':BW})
   
def plus_cart(request):
 if request.method=='GET':
  prod_id = request.GET['prod_id']
  c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
  c.quantity+=1
  c.save()
  amount=0.0
  shipping_amount=70.0
  cart_product = [p for p in Cart.objects.all() if p.user ==request.user]
  for p in cart_product:
    tempamount = (p.quantity * p.product.discounted_price)
    amount += tempamount
    totalamount= amount+shipping_amount 
  data = {
   'quantity':c.quantity,
   'amount':amount,
  'totalamount':totalamount
  }
 return JsonResponse(data)

def minus_cart(request):
 if request.method=='GET':
  prod_id = request.GET['prod_id']
  c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
  c.quantity-=1
  c.save()
  amount=0.0
  shipping_amount=70.0
  cart_product = [p for p in Cart.objects.all() if p.user ==request.user]
  for p in cart_product:
    tempamount = (p.quantity * p.product.discounted_price)
    amount += tempamount
    totalamount= amount+shipping_amount 
  data = {
   'quantity':c.quantity,
   'amount':amount,
  'totalamount':totalamount
  }
 return JsonResponse(data)




def remove_item(request,id):
  Product =Cart.objects.get(id=id)
  Product.delete()
  return redirect('/cart')




def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 add= Customer.objects.filter(user=request.user)
 return render(request, 'app/address.html',{'add':add,'active':'btn-primary'})

def remove_address(request,id):
 add =  Customer.objects.get(id=id)
 add.delete()
 return redirect('/address')

def orders(request):
 op = Orderplaced.objects.filter(user=request.user)
 return render(request,'app/orders.html',{'order_paced':op})

# def change_password(request):
#  return render(request, 'app/changepassword.html')

def mobile(request,data=None):
 
 if data==None:
  mobiles=Product.objects.filter(category='M')
 elif data =='redmi' or data =='samsung':
    mobiles=Product.objects.filter(category='M').filter(brand=data)
 elif data=='below':
   mobiles=Product.objects.filter(category='M').filter(discounted_price__lt=10000)
 elif data=='above':
   mobiles=Product.objects.filter(category='M').filter(discounted_price__gt=10000)
 return render(request, 'app/mobile.html',{'mobiles':mobiles})

def top_wear(request):
 
 topwear=Product.objects.filter(category='TW')
 return render(request,'app/topwear.html',{'topwear':topwear})

def bottom_wear(request):
 
 bottom=Product.objects.filter(category='BW')
 return render(request,'app/bottomwear.html',{'bottom':bottom})
 

# def login(request):
#  return render(request, 'app/login.html')



# def customerregistration(request):
#  return render(request, 'app/customerregistration.html')

class CustomerRegistrationView(View):
 def get(self,request):
   form =CustomerRegistrationForm()
   return render(request,'app/customerregistration.html',{'form':form})
 

 def post(self,request):
  form =CustomerRegistrationForm(request.POST)
  if form.is_valid():
   messages.success(request,'congratulations!! registration successfully')
   form.save()
  return render(request,'app/customerregistration.html',{'form':form})


def checkout(request):
 user =request.user
 add = Customer.objects.filter(user=user)
 cart_items = Cart.objects.filter(user=user)
 amount=0.0
 shipping_amount=70.0 
 totalamount=0
 cart_product = [p for p in Cart.objects.all() if p.user ==request.user]
 if cart_product:
    for p in cart_product:
      tempamount = (p.quantity * p.product.discounted_price)
      amount += tempamount
    totalamount= amount+shipping_amount
 return render(request, 'app/checkout.html',{'add':add,'totalamount':totalamount,'cart_item':cart_items})
 
def payment_done(request):
  user  = request.user
  custid = request.GET.get('custid')
  customer = Customer.objects.get(id=custid)
  cart = Cart.objects.filter(user=user)
  for c in cart:
   Orderplaced(user=user,customer=customer, product=c.product, quentity=c.quantity).save()
   c.delete()
  return redirect("orders")

class ProfileView(View):
  def get(self,request):
   form= CustomerProfileForm()
   return render(request,'app/profile.html',{'form':form ,'active':'btn-primary'})
  def post(self,request):
   form= CustomerProfileForm(request.POST)
   if form.is_valid():
    usr=request.user
    name=form.cleaned_data['name']
    locality=form.cleaned_data['locality']    
    city=form.cleaned_data['city']    
    state=form.cleaned_data['state']    
    zipcode=form.cleaned_data['zipcode']    

    reg =  Customer(user=usr,name=name,locality=locality,city=city,state=state,zipcode=zipcode)
    reg.save()  
    messages.success(request,'congratulations!! profile updated')
   return render(request,'app/profile.html',{'form':form},)


def post(self,request):
   form = CustomerRegistrationForm(request.POST)
   if form.is_valid():
    messages.success(request,'congratulations!! Address is Added successfully')
    form.save()
    return render(request,'app/profile.html',{'form':form,'active':'btn-primary'})