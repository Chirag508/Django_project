from django.shortcuts import render,redirect
# from django.contrib.auth.decorators import login_required
from .models import customer_data,news,product
from .forms import customer_form

#only for api development
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import productserializers

# Create your views here.
# @login_required
def show_home_page(request):
    return render(request,'home.html')

def show_hello(request):
    return render(request,'hello.html')


def customer_form_page(request):
    customers = customer_data.objects.all()
    # print(customers) #this is to print the customer data into html
    if request.method == 'POST':
        form = customer_form(request.POST)
        if form.is_valid():
            print("Form data saved!")
            form.save()
            return redirect('customer_form')
    else:
        form = customer_form()
        return render(request,'customer.html',{'customers': customers,'form':form})

def update_cutomeer_page(request,id):
    upd_customer = customer_data.objects.get(cust_id = id)
    customers = customer_data.objects.all()
    form = customer_form(instance=upd_customer)
    if request.method == 'POST':
        form = customer_form(request.POST,instance=upd_customer)
        if form.is_valid():
            form.save()
            return redirect('customer_form')
    else:
        return render(request,'customer.html',{'customers': customers,'form':form})

def delete_customer_data(request,id):
    del_customer = customer_data.objects.get( cust_id = id)
    del_customer.delete()
    return redirect('customer_form')


def show_news(request):
    news_data = news.objects.all()
    return render(request,'news.html',{'news_data':news_data})


def show_screen_one(request):
    if request.method=='POST':
        name = request.POST.get('username')
        request.session['session_name'] = name
        return redirect('screen_two')
    return render(request,'screen_one.html')

def show_screen_two(request):
    name = request.session.get('session_name')
    return render(request,'screen_two.html',{'name':name})


def show_shoping_page(request):
    fruits = ('Apple', 'Banana', 'Orange', 'Mango', 'Grapes', 'Strawberry', 'Blueberry', 'Pineapple',
    'Watermelon', 'Peach', 'Cherry', 'Lemon', 'Lime', 'Papaya', 'Guava', 'Pomegranate', 'Kiwi',
    'Raspberry', 'Blackberry', 'Cantaloupe', 'Honeydew', 'Fig', 'Coconut', 'Avocado', 'Dragon Fruit', 
    'Lychee', 'Passion Fruit', 'Star Fruit', 'Tangerine', 'Plum', 'Apricot', 'Nectarine', 'Cranberry', 
    'Gooseberry', 'Date', 'Jackfruit', 'Durian', 'Persimmon', 'Mulberry', 'Breadfruit', 'Pomelo', 
    'Custard Apple','Soursop', 'Quince', 'Elderberry', 'Cloudberry', 'Salak', 'Tamarind', 'Mangosteen', 
    'Rambutan', 'Longan')
    if request.method=='POST':
        selected_items = request.POST.getlist('select')
        print(selected_items)
        request.session['cart_item'] = selected_items

        #this is website counter that return the number how many time the page is rendered..
        counter = request.session.get('counter',1)
        counter += 1
        request.session['counter'] = counter
        
        return redirect('cart/')
    return render(request,'session_item.html',{'fruits':fruits})

def show_cart(request):
    items = request.session.get('cart_item')
    count = request.session.get('counter')
    return render(request,'session_cart.html',{'items':items,'count':count})

class productlist(APIView):

    def get(self,request):
        products = product.objects.all()
        serializer = productserializers(products,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = productserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)