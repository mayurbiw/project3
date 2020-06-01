from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Dinner_Platters, Salads, Pasta, Subs, Sicilian_Pizza,  Toppings, Regular_Pizza, placed_orders
from django.db import IntegrityError
from django.core.mail import send_mail
from pizza.settings import EMAIL_HOST_USER
import json
import os

# input -> Query set
# output -> JSON object
def convertintoJSON(NodeList):
    items_details_dict = dict()
    for i,item in enumerate(NodeList):
        print("Index = "+str(i))
        print("Item  = "+ str(item) + "\n" + "type of item = "+ str(type(item)))
        attributes =  item.getAttributes()
        a  = dict()
        for attribute in attributes:
            attribute = str(attribute)
            print("Attribute = "+ attribute)
            a[f"{attribute}"] =  str(getattr(item, attribute))
        items_details_dict[f"{i}"] = a
    return json.dumps(items_details_dict)

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
          return render(request, "orders/login.html", {"message": None})

    #For unit testing remove it
    if request.session['shoppingCart'] is None:
        request.session['shoppingCart'] = []
        request.session['numOfItemInShoppingCart'] = 0

    regular_piza_details = Regular_Pizza.objects.all()
    sicilian_pizza_details = Sicilian_Pizza.objects.all()
    Subs_details            = Subs.objects.all()
    Pasta_details = Pasta.objects.all()
    Salads_details = Salads.objects.all()
    Dinner_Platters_details  = Dinner_Platters.objects.all()

    print("Type of subs" + str(type(Subs_details)))

    # converting dict into json
    sicilian_pizza_details_json = convertintoJSON(sicilian_pizza_details)
    regular_piza_details_json = convertintoJSON(regular_piza_details)
    Subs_details_json = convertintoJSON(Subs_details)
    Pasta_details_json = convertintoJSON(Pasta_details)
    Salads_details_json = convertintoJSON(Salads_details)
    Dinner_Platters_json = convertintoJSON(Dinner_Platters_details)

    context = {
        "user": request.user,
        "Toppings":Toppings.objects.all(),
        "Regular_Pizza":regular_piza_details_json,
        "Sicilian_Pizza":sicilian_pizza_details_json,
        "Subs" :Subs_details_json,
        "Pasta":Pasta_details_json,
        "Salads":Salads_details_json,
        "Dinner_Platters" :Dinner_Platters_json,
        "numOfItemInShoppingCart":request.session['numOfItemInShoppingCart'],
        }
    return render(request, "orders/menu.html", context)

def login_view(request):
    username =  request.POST.get('username', False)
    password =  request.POST.get('password', False)
    if username and password:
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # session variables that will be used while adding/removing the items from the cart.
            request.session['shoppingCart'] = []
            request.session['numOfItemInShoppingCart'] = 0
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "orders/login.html", {"message": "Invalid credentials."})
    return render(request, "orders/login.html", {"message": ""})

def logout_view(request):
    
    logout(request)
    return render(request, "orders/login.html", {"message": "Logged out."})

def register_view(request):
    return render(request, "orders/register.html")

def after_register_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    email = request.POST["email"]
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    try:
        user = User.objects.create_user(username,email, password)
    except IntegrityError as e:
        return HttpResponse("User already exists " + str(e))
    user.first_name = first_name
    user.last_name = last_name
    user.save()
    return HttpResponseRedirect(reverse("index"))

def addintoshoppingcart(request,id,typeofItem,toppings):
    # finding some good way to shopping cart data that works for very item.
    request.session['numOfItemInShoppingCart'] = request.session['numOfItemInShoppingCart'] + 1

    # taking id and type of item
    #id  = request.GET.get("id")
    #typeofItem = request.GET.get("typeofItem")

    print("AJAX Request topping = "+ toppings)
    print("AJAX Request id = "+ id)
    print("AJAX request typeofItem = "+typeofItem)
    #declaring a item to store id and type of items
    item = dict()
    item["id"] = id
    item["typeofItem"] = typeofItem
    item["toppings"] = toppings.split(",")

    # adding a item into a cart
    request.session['shoppingCart'].append(item)

    # printing for unit testing
    print(json.dumps(request.session['shoppingCart']))
    return HttpResponse(request.session['numOfItemInShoppingCart'])

def removefromshoppingcart(request):
    pass

def shoppingcartview(request):
    Regular_Pizz_items = []
    Sicilian_Pizza_items = []
    Subs_items = []
    Dinner_Platters_items = []
    Pasta_items = []
    Salads_items = []
    total_price = 0
    for item in request.session['shoppingCart']:
        if(item["typeofItem"] == "Regular_Pizza"):
            a = Regular_Pizza.objects.get(pk=item["id"])
            b = dict()
            b["id"]  = a.id
            b["numToppings"] = a.numToppings
            if (a.type=='S'):
                b["type"] = 'Small'
            else:
                b["type"] = 'Large'
            b["price"] = a.price
            total_price = total_price + a.price
            b["toppings"] = item["toppings"]
            Regular_Pizz_items.append(b)
            print(b)
        if(item["typeofItem"] == "Sicilian_Pizza"):
            a = Sicilian_Pizza.objects.get(pk=item["id"])
            b = dict()
            b["id"]  = a.id
            b["numToppings"] = a.numToppings
            if (a.type=='S'):
                b["type"] = 'Small'
            else:
                b["type"] = 'Large'
            b["price"] = a.price
            total_price = total_price + a.price
            b["toppings"] = item["toppings"]
            Sicilian_Pizza_items.append(b)
            print(b)
        if(item["typeofItem"]=="Subs"):
             a = Subs.objects.get(pk=item["id"])
             b = dict()
             b["id"]  = a.id
             num = len(item["toppings"])
             for num in range(num,3):
                 item["toppings"].append(None)
             if item["toppings"][1] is not None:
                 b["extra_cheese"] = 'with extra cheese'
                 b["price"] = float(a.price) + 0.5
             else:
                 b["price"] = a.price
             if (a.type=='S'):
                 b["type"] = 'Small'
             else:
                 b["type"] = 'Large'

             total_price = total_price + a.price
             b["name"] = a.name
             Subs_items.append(b)
             print(b)
        if(item["typeofItem"]=="Dinner_Platters"):
             a = Dinner_Platters.objects.get(pk=item["id"])
             b = dict()
             b["id"]  = a.id
             if(a.type=='S'):
                b["type"] = 'Small'
             else:
                b["type"] = 'Large'
             b["price"] = a.price
             total_price = total_price + a.price
             b["name"] = a.name
             Dinner_Platters_items.append(b)
             print(b)
        if(item["typeofItem"]=="Pasta"):
             a = Pasta.objects.get(pk=item["id"])
             b = dict()
             b["id"]  = a.id
            #b["type"] = a.type
             b["price"] = a.price
             total_price = total_price + a.price
             b["name"] = a.name
             Pasta_items.append(b)
             print(b)
        if(item["typeofItem"]=="Salads"):
             a = Salads.objects.get(pk=item["id"])
             b = dict()
             b["id"]  = a.id
             #b["type"] = a.type
             b["price"] = a.price
             total_price = total_price + a.price
             b["name"] = a.name
             Salads_items.append(b)
             print(b)
    request.session['total_price'] = str(total_price)
    context = {
        "Regular_Pizz_items": Regular_Pizz_items,
        "Sicilian_Pizza_items":Sicilian_Pizza_items,
        "Subs_items":Subs_items,
        "Dinner_Platters_items":Dinner_Platters_items,
        "Pasta_items" : Pasta_items,
        "Salads_items" : Salads_items,
        "total_price" :str(total_price),
        "user": request.user,
        "numOfItemInShoppingCart":request.session['numOfItemInShoppingCart']
        }
    return render(request, "orders/shoppingcart.html", context)



def placeorder(request):
    #Add items in a models for the admin
    for item in request.session['shoppingCart']:
        if(item["typeofItem"] == "Regular_Pizza"):
            a = Regular_Pizza.objects.get(pk=item["id"])
            b = dict()
            b["id"]  = a.id
            b["numToppings"] = a.numToppings
            b["type"] = a.type
            b["toppings"] = item["toppings"]
            print(item["toppings"])

            num = len(item["toppings"])

            for num in range(num,3):
                item["toppings"].append(None)

            if item["toppings"][0] is not None:
                t1 = Toppings.objects.get(name=item["toppings"][0])
            else:
                t1 = None

            if item["toppings"][1] is not None:
                t2 = Toppings.objects.get(name=item["toppings"][1])
            else:
                t2 = None

            if item["toppings"][2] is not None:
                t3 = Toppings.objects.get(name=item["toppings"][2])
            else:
                t3 = None

            # create a regular pizza order
            order = placed_orders(username = request.user.username,itemtype = 'Regular Pizza' ,item_id=a.id,topping1=t1,topping2=t2,topping3 = t3)
            order.save()
        if(item["typeofItem"] == "Sicilian_Pizza"):
            a = Sicilian_Pizza.objects.get(pk=item["id"])
            b = dict()
            b["id"]  = a.id
            b["numToppings"] = a.numToppings
            b["type"] = a.type
            b["toppings"] = item["toppings"]

            num = len(item["toppings"])
            print(item["toppings"])

            for num in range(num,3):
                item["toppings"].append(None)

            if item["toppings"][0] is not None:
                t1 = Toppings.objects.get(name=item["toppings"][0])
            else:
                t1 = None

            if item["toppings"][1] is not None:
                t2 = Toppings.objects.get(name=item["toppings"][1])
            else:
                t2 = None

            if item["toppings"][2] is not None:
                t3 = Toppings.objects.get(name=item["toppings"][2])
            else:
                t3 = None

            # create a order
            order = placed_orders(username = request.user.username,itemtype = 'Sicilian Pizza' ,item_id=a.id,topping1=t1,topping2=t2,topping3 = t3)
            order.save()

        if(item["typeofItem"] == "Subs"):
                a = Subs.objects.get(pk=item["id"])
                b = dict()
                b["id"]  = a.id
                b["type"] = a.type
                b["toppings"] = item["toppings"]

                num = len(item["toppings"])
                print(item["toppings"])

                for num in range(num,3):
                    item["toppings"].append(None)

                if (item["toppings"][1] == "extra_cheese_sub" ):
                    extra_cheese = True
                else:
                    extra_cheese = False

                # create a order
                order = placed_orders(username = request.user.username,itemtype = 'Subs' ,item_id=a.id,extra_cheese=extra_cheese)
                order.save()

        if(item["typeofItem"] == "Dinner_Platters"):
                a = Dinner_Platters.objects.get(pk=item["id"])
                b = dict()
                b["id"]  = a.id
                b["type"] = a.type

                # create a order
                order = placed_orders(username = request.user.username,itemtype = 'Dinner Platters' ,item_id=a.id)
                order.save()

        if(item["typeofItem"] == "Pastas"):
                a = Pastas.objects.get(pk=item["id"])
                b = dict()
                b["id"]  = a.id


                # create a order
                order = placed_orders(username = request.user.username,itemtype = 'Pastas' ,item_id=a.id)
                order.save()

        if(item["typeofItem"] == "Salads"):
                a = Salads.objects.get(pk=item["id"])
                b = dict()
                b["id"]  = a.id

                # create a order
                order = placed_orders(username = request.user.username,itemtype = 'Salads' ,item_id=a.id)
                order.save()
    request.session['shoppingCart'] = None
    request.session['numOfItemInShoppingCart'] = 0
    reciever_email_add = request.user.email
    msg = "Your order has been placed. Thank you"
    if(os.environ.get("pass") is None):
        return HttpResponse("Environment variable for password is not set")

    send_mail("Pizza order",
            msg, EMAIL_HOST_USER, [reciever_email_add], fail_silently = False)

    return HttpResponseRedirect(reverse("afterorderplaced"))

def afterorderplaced(request):
    context = {
        "user": request.user,
        "numOfItemInShoppingCart":request.session['numOfItemInShoppingCart']
        }
    return render(request, "orders/afterorderplaced.html", context)


def resetcart(request):
    request.session['shoppingCart'] = None
    request.session['numOfItemInShoppingCart'] = 0
    context = {
        "user": request.user,
        "numOfItemInShoppingCart":request.session['numOfItemInShoppingCart']
        }
    return render(request, "orders/shoppingcart.html", context)


def vieworders(request):
    items = placed_orders.objects.all()
    context  = {
    "items":items,
    "user": request.user,
    "numOfItemInShoppingCart":request.session['numOfItemInShoppingCart']
    }
    return render(request, "orders/placedorders.html", context)

def markcompleted(request,orderid):
    print("order id")
    item = placed_orders.objects.get(pk=orderid)
    item.completed = True
    item.save()
    data = {
    "success":True
    }
    return HttpResponse(json.dumps(data))
