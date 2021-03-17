from django.db import models
class Customer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=500)
    phone=models.IntegerField()

    def register(self):
        self.save()
    @staticmethod
    def get_customer_by_id(email):
        #if i use filter than get list of object
        #i use get than i get single object
        try:
            return Customer.objects.get(email=email)
        except:
            return False
    def isExits(self):
        if Customer.objects.filter(email=self.email):

            return True
        else:
            return False