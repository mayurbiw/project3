from django.db import models

# Create your models here.

class Regular_Pizza(models.Model):
    # Either 1 , 2 or 3 toppings
    chTopings = (
    (0,'Cheese'),
    (1,'1'),
    (2,'2'),
    (3,'3'),
    (5,'Special'),
    )
    TYPE = (
        ('S', 'Small'),
        ('L', 'Large'),
    )
    # number of toppings
    numToppings = models.IntegerField(choices = chTopings)
    type = models.CharField(max_length = 1, choices = TYPE )
    price = models.DecimalField(decimal_places=2,max_digits=4)

    def __str__(self):
        return f"{self.get_numToppings_display()} | {self.get_type_display()} | {self.price}"

    def getAttributes(self):
        attributes = []
        attributes.append("id")
        attributes.append("numToppings")
        attributes.append("type")
        attributes.append("price")
        return attributes


    class Meta:
        unique_together = ('numToppings', 'type',)

class Sicilian_Pizza(models.Model):
    # Either 1 , 2 or 3 toppings
    chTopings = (
    (0,'Cheese'),
    (1,'1'),
    (2,'2'),
    (3,'3'),
    (5,'Special'),
    )
    TYPE = (
        ('S', 'Small'),
        ('L', 'Large'),
    )
    # number of toppings
    numToppings = models.IntegerField(choices = chTopings)
    type = models.CharField(max_length = 1, choices = TYPE )
    price = models.DecimalField(decimal_places=2,max_digits=4)

    def __str__(self):
        return f"{self.get_numToppings_display()} | {self.get_type_display()} | {self.price}"

    class Meta:
        unique_together = ('numToppings', 'type',)

    def getAttributes(self):
        attributes = []
        attributes.append("id")
        attributes.append("numToppings")
        attributes.append("type")
        attributes.append("price")
        return attributes

class Toppings(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        unique_together = ('name',)

    def getAttributes(self):
        attributes = []
        attributes.append("id")
        attributes.append("name")
        return attributes

class Subs(models.Model):
    options =  (
    ('Cheese','Cheese'),
    ('Italian','Italian'),
    ('Ham + Cheese','Ham + Cheese'),
    ('Meatball','Meatball'),
    ('Tuna','Tuna'),
    ('Turkey','Turkey'),
    ('Chicken Parmigiana','Chicken Parmigiana'),
    ('Eggplant Parmigiana','Eggplant Parmigiana'),
    ('Steak','Steak'),
    ('Steak + Cheese','Steak + Cheese'),
    ('Steak + Cheese + Mushrooms','Steak + Cheese + Mushrooms'),
    ('Steak + Cheese + Mushrooms + Green Peppers','Steak + Cheese + Mushrooms + Green Peppers'),
    ('Steak + Cheese + Mushrooms + Green Peppers + Onions','Steak + Cheese + Mushrooms + Green Peppers + Onions'),
    ('Sausage, Peppers & Onions','Sausage, Peppers & Onions'),
    ('Hamburger','Hamburger'),
    ('Cheeseburger','Cheeseburger'),
    ('Fried Chicken','Fried Chicken'),
    ('Veggies','Veggies'),
    )
    name = models.CharField(max_length = 128,choices = options)
    TYPE = (
        ('S', 'Small'),
        ('L', 'Large'),
    )
    type = models.CharField(max_length = 1, choices = TYPE )
    price = models.DecimalField(decimal_places=2,max_digits=4)


    def __str__(self):
        return f"{self.name} | {self.get_type_display()} | {self.price} "

    class Meta:
        unique_together = ('name', 'type',)

    def getAttributes(self):
        attributes = []
        attributes.append("id")
        attributes.append("name")
        attributes.append("type")
        attributes.append("price")
        return attributes

class Pasta(models.Model):
    options = (
        ('Baked Ziti w/Mozzarella','Baked Ziti w/Mozzarella'),
        ('Baked Ziti w/Meatballs','Baked Ziti w/Meatballs'),
        ('Baked Ziti w/Chicken','Baked Ziti w/Chicken'),
    )
    name = models.CharField(max_length = 128, choices = options)
    price = models.DecimalField(decimal_places=2,max_digits=4)

    def __str__(self):
        return f"{self.get_name_display()} | {self.price}"

    def getAttributes(self):
        attributes = []
        attributes.append("id")
        attributes.append("name")
        attributes.append("price")
        return attributes

    class Meta:
        unique_together = ('name',)

class Salads(models.Model):
    options =  (
    ('Garden Salad','Garden Salad'),
    ('Greek Salad','Greek Salad'),
    ('Antipasto','Antipasto'),
    ('Salad w/Tuna','Salad w/Tuna'),
    )
    name = models.CharField(max_length = 128, choices = options)
    price = models.DecimalField(decimal_places=2,max_digits=4)

    def __str__(self):
        return f"{self.get_name_display()} | {self.price}"

    def getAttributes(self):
        attributes = []
        attributes.append("id")
        attributes.append("name")
        attributes.append("price")
        return attributes

    class Meta:
        unique_together = ('name',)

class Dinner_Platters(models.Model):
    options =  (
    ('Garden Salad','Garden Salad'),
    ('Greek Salad','Greek Salad'),
    ('Antipasto','Antipasto'),
    ('Baked Ziti','Baked Ziti'),
    ('Meatball Parm','Meatball Parm'),
    ('Chicken Parm','Chicken Parm'),
    )
    name = models.CharField(max_length = 128, choices = options)
    TYPE = (
        ('S', 'Small'),
        ('L', 'Large'),
    )
    type = models.CharField(max_length = 128, choices = TYPE)
    price = models.DecimalField(decimal_places=2,max_digits=4)

    def __str__(self):
        return f"{self.get_name_display()} | {self.get_type_display()}  | {self.price}"

    def getAttributes(self):
        attributes = []
        attributes.append("id")
        attributes.append("name")
        attributes.append("type")
        attributes.append("price")
        return attributes

    class Meta:
        unique_together = ('name', 'type',)

class placed_orders(models.Model):

    # username of the user who has order
    username = models.CharField(max_length = 128,null = False)

    # to get all other information related to any item item
    itemtype = models.CharField(max_length = 128)
    item_id = models.IntegerField()

    # for pizzas
    topping1 = models.ForeignKey(Toppings,on_delete=models.CASCADE,null =True,blank=True,related_name = "one_topping")
    topping2 = models.ForeignKey(Toppings,on_delete=models.CASCADE,null =True,blank=True,related_name = "two_topping")
    topping3 = models.ForeignKey(Toppings,on_delete=models.CASCADE,null =True,blank=True,related_name = "three_topping")

    # for subs
    extra_cheese = models.BooleanField(null =True)

    #field to mark order completed
    completed = models.BooleanField(null =True)

    class Meta:
        verbose_name_plural = 'Placed orders'
        app_label = 'orders'
