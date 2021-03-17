from django.shortcuts import render ,redirect

# Create your views here.
from django.http import HttpResponse
from store.models.product import Product
from store.models.category import Category
from django.views import View



# from store.models.customer import Customer
# from django.views import View

class Index(View):
    def get(self,request):
        cart=request.session.get('cart')
        if not cart:
            request.session['cart']={}
        products = None
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        # categoryID = request.GET['category']

        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)
        else:
            products = Product.get_all_products()
        data = {}
        data['products'] = products
        data['categories'] = categories
        print(request.session.get('email'))

        return render(request, 'index.html', data)
    def post(self,request):
        product=request.POST.get('product')
        remove=request.POST.get('remove')
        cart=request.session.get('cart')
        if cart:
            quantity=cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1

            else:
                cart[product] = 1
        else:
            cart={}
            cart[product]=1
        request.session['cart']=cart

        print(request.session['cart'])
        return redirect('homepage')

# def index(request):
#     products = None
#     categories = Category.get_all_categories()
#     categoryID = request.GET.get('category')
#     # categoryID = request.GET['category']
#
#     if categoryID:
#         products = Product.get_all_products_by_categoryid(categoryID)
#     else:
#         products = Product.get_all_products()
#     data = {}
#     data['products'] = products
#     data['categories'] = categories
#     print(request.session.get('email'))
#
#     return render(request, 'index.html', data)

# def validateCustomer(customer):
#     error_message=None
#     if (not customer.first_name):
#         error_message = "first name required"
#     elif len(customer.first_name) < 4:
#         error_message = "first name should be 4 and more charecter"
#     if (not customer.last_name):
#         error_message = "last name required"
#     elif len(customer.last_name) < 4:
#         error_message = "last name should be 4 and more char long"
#     if (not customer.email):
#         error_message = "email required"
#     elif len(customer.email) < 4:
#         error_message = "email should be 4 and more charecter"
#     if (not customer.password):
#         error_message = "password  required"
#     elif len(customer.password) < 4:
#         error_message = "password should be 4 and more char long"
#     if (not customer.phone):
#         error_message = "phone number  required"
#     elif len(customer.phone) < 4:
#         error_message = "phone number should be 4 and more char long"
#     elif customer.isExits():
#         error_message = 'user already registered'
#     return error_message
#
# def registeruser(request):
#     first_name = request.POST.get('firstname')
#     last_name = request.POST.get('lastname')
#     email = request.POST.get('email')
#     password = request.POST.get('password')
#     phone = request.POST.get('phone')
#     error_message = None
#     value = {'first_name': first_name, 'last_name': last_name, 'email': email, 'phone': phone}
#
#     customer = Customer(first_name=first_name,
#                         last_name=last_name,
#                         email=email,
#                         password=password,
#                         phone=phone, )
#
#     # validation
#     error_message = validateCustomer(customer)
#
#     # saving
#     if (not error_message):
#         customer.password = make_password(customer.password)
#
#         customer.register()
#         # return render(request,'index.html')
#         # return redirect('http:/localhost:8000')
#         return redirect('homepage')
#
#     else:
#         data = {'error': error_message, 'values': value}
#
#         return render(request, 'signup.html', data)


# using method view

# def signup(request):
#     if(request.method=='GET'):
#         return render(request, 'signup.html')
#
#     else:
#         return registeruser(request)


# using funtion view
#   def login(request):
#     if(request.method=='GET'):
#         return render(request, 'login.html')
#     else:
#         email=request.POST.get('email')
#         password=request.POST.get('password')
#         customer=Customer.get_customer_by_id(email)
#         error_message=None
#         if customer:
#             flag=check_password(password,customer.password)
#             if flag:
#                 return redirect(request,'homepage')
#             else:
#                 error_message='password is incorrect!!'
#         else:
#             error_message="email is incorrect"
#         return render(request,'login.html',{'error':error_message})
