from django.db import models
from django.db.models import Q
from django.conf import settings


User = settings.AUTH_USER_MODEL # string to default django auth.User model, preferred method

class ProductQuerySet(models.QuerySet):
    # check if product is set as public or private
    def is_public(self):
        return self.filter(public=True)

    # allows user to search any query they want and return a result query if search is found or None
    def search(self, query, user=None):
        lookup = Q(title__icontains=query) | Q(content__icontains=query) # specify here that the lookup values in the user search query can be either like the title OR like the content fields
        qs = self.filter(lookup) # this to filter this specific queryset result with the input query string or value ie title icontains 'hello world'
        if user is not None:
            qs = qs.filter(user=user)
        return qs 


class ProductManager(models.Manager):
    def get_queryset(self, *args,**kwargs): # overriding the default get_queryset 
        return ProductQuerySet(self.model, using=self._db) # use the model attached to this manager, 'using' references this database, but can potentially reference other databases as well
    
    def search(self, query, user=None):
        return self.get_queryset.is_public().search(query, user=user) # instead of Product.objects.filter(), models.Manager allows you to take queryset from models.QuerySet and get that object with get_queryset, so you can reference your own queryset like the above ProductQuerySet class; pass in the user


# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL) # to reference user's products other relationship, do user.<model_name>_set.all(); this to set the foreign key to user; will show in admin site as well; if User deleted, Products for that user are maintained, but their user is set to None/null
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)
    public = models.BooleanField(default=True) # should be False by default if want to keep things safe    

    @property # this @property decorator creates an attribute to the model which is not instantiated nor is a function, but when called upon does whatever is needed. good for something like when product on sale
    def sale_price(self):
        return f"{float(self.price) * 0.8:.2f}"
    
    def get_discount(self):
        return '122'

    def __repr__(self):
        return f'<{self.title}| {self.content}| price: ${self.price}>'