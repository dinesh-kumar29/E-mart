from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
# Create your views here.
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        error_message = None
        value = {'first_name': first_name, 'last_name': last_name, 'email': email, 'phone': phone}

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            email=email,
                            password=password,
                            phone=phone, )

        # validation
        error_message = self.validateCustomer(customer)

        # saving
        if (not error_message):
            customer.password = make_password(customer.password)

            customer.register()
            # return render(request,'index.html')
            # return redirect('http:/localhost:8000')
            return redirect('homepage')

        else:
            data = {'error': error_message, 'values': value}

            return render(request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None

        if (not customer.first_name):
            error_message = "first name required"
        elif len(customer.first_name) < 4:
            error_message = "first name should be 4 and more charecter"
        if (not customer.last_name):
            error_message = "last name required"
        elif len(customer.last_name) < 4:
            error_message = "last name should be 4 and more char long"
        if (not customer.email):
            error_message = "email required"
        elif len(customer.email) < 4:
            error_message = "email should be 4 and more charecter"
        if (not customer.password):
            error_message = "password  required"
        elif len(customer.password) < 4:
            error_message = "password should be 4 and more char long"
        if (not customer.phone):
            error_message = "phone number  required"
        elif len(customer.phone) < 4:
            error_message = "phone number should be 4 and more char long"
        elif customer.isExits():
            error_message = 'user already registered'
        return error_message
