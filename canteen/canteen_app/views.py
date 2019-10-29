from django.shortcuts import render,redirect
from django.http import HttpResponse
from canteen_app.forms import LoginForm
from canteen_app.models import Student,Orders

def view_menu(request):
   return render(request, "view_menu.html")

def signup(request):
	return render(request,"signup.html")

def student(request):
	return render(request,"student.html")

def index(request):
	return render(request,"index.html")

def indexstu(request):
	return render(request,"indexstu.html")

def placeorder(request):
	return render(request,"placeorder.html")

def nextpage(request):
	return render(request,"nextpage.html")

def wallet(request):
	student = Student.objects.get(roll = '2016103022')
	balance = student.wallet
	return render(request,"wallet.html",{"balance":balance})

def yourorder(request):
	return render(request,"yourorder.html")

def login_req(request):
    user= request.GET['username']
    psw = request.GET['psw']
    if(user == 'office' and psw == 'hello'):
       return redirect(nextpage)
    return redirect(index)

def order_req(request):
	oid = request.GET['oid']
	oid_int = int(oid)
	order = Orders.objects.get(order_id =oid_int)
	total = order.total
	order_id = oid_int
	desc = order.desc
	return render(request,"yourorder.html",{"total":total,"order_id":order_id,"desc":desc})

def place_req(request):
    total = request.GET['totalvaln']
    return HttpResponse(total)

def add_money(request):
	roll1  = request.GET['username_a']
	amnt = int(request.GET['amnt_a'])
	student = Student.objects.get(roll = roll1)
	amount = student.wallet
	amount=amount+amnt
	student.wallet = amount
	student.save()
	student1 = Student.objects.get(roll = roll1)
	amt = str(student1.wallet)
	wallet1 = "Amount added to the wallet current balance is "+amt
	return render(request,"nextpage.html",{"wallet1":wallet1})

def remove_money(request):
	roll1  = request.GET['username_r']
	amnt = int(request.GET['amnt_r'])
	student = Student.objects.get(roll = roll1)
	amount = student.wallet
	amount=amount-amnt
	student.wallet = amount
	student.save()
	student1 = Student.objects.get(roll = roll1)
	amt = str(student1.wallet)
	wallet2 = "Amount reduced from the wallet current balance is "+amt
	return render(request,"nextpage.html",{"wallet2":wallet2})

def show_order(request):
	roll1 = request.GET['username']
	order = Orders.objects.filter(roll = roll1)
	return render(request,"nextpage.html",{"roll_no":roll1,"order":order})

def remove_ord(request):
	oid=int(request.GET['ordid'])
	order =  Orders.objects.get(order_id = oid)
	order.delete()
	text = "successfully updated"
	return render(request,"nextpage.html",{"success":text})