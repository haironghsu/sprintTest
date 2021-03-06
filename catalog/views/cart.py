from django.conf import settings
from django_mako_plus import view_function, jscontext
from account import models as amod
from catalog import models as cmod
from django import forms
from django.http import HttpResponseRedirect

@view_function
def process_request(request):
   cart = request.user.get_shopping_cart()
   cart.recalculate()
   cart.save()
   saleitems = cmod.SaleItem.objects.filter(sale = cart, status = 'A')
   categories = cmod.Category.objects.all()
   context = {
       'categories': categories,
       'cart' : cart,
       'saleitems' : saleitems,
   }

   return request.dmp.render('cart.html', context)

@view_function
def remove(request, saleitem:cmod.SaleItem):
   saleitem.status = 'D'
   saleitem.save()

   return HttpResponseRedirect('/catalog/cart')