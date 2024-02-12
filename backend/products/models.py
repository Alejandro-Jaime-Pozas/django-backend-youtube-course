from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)

    @property # this @property decorator creates an attribute to the model which is not instantiated nor is a function, but when called upon does whatever is needed. good for something like when product on sale
    def sale_price(self):
        return f"{float(self.price) * 0.8:.2f}"
    
    def get_discount(self):
        return '122'

    def __repr__(self):
        return f'<{self.title}| {self.content}| price: ${self.price}>'