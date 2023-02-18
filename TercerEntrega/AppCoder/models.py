from django.db import models

class Product(models.Model): 
    name = models.CharField(max_length=40)
    price = models.IntegerField()
    added = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self): 
        return self.name

class User(models.Model): 
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=154)

    def __str__(self): 
        return f"{self.name}"
    
class Review(models.Model): 
    text = models.CharField(max_length=150)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_positive = models.BooleanField(default=True)


    def __str__(self): 
        return f"{self.name} {self.text[0:20]}..."