from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from  django.core.files.storage import FileSystemStorage
from urllib.parse import urlencode
from .models import *
from django.db.models import Q

from django.shortcuts import render
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect

def first(request):
    return render(request, 'index.html')
   
def index(request):
    return render(request,"index.html")
def reg(request):
    return render(request,"userregister.html")

def userreg(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        gender=request.POST.get('gender')
        phone=request.POST.get('phone')
        password=request.POST.get('password')
       
        cus=userregtbl(name=name,email=email,address=address,gender=gender,phone=phone,password=password)
        cus.save()
    return render(request,"index.html", {'message':'Succesfully Registered'})
    

def login(request):
    return render(request,'login.html')

def addlogin(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    if email == 'admin@gmail.com' and password =='admin':
        request.session['admin'] = 'admin'
        return redirect(index)

    elif userregtbl.objects.filter(email=email,password=password).exists():
        userdetails=userregtbl.objects.get(email=request.POST['email'], password=password)
        if userdetails.password == request.POST['password']:
            request.session['uid'] = userdetails.id
            request.session['uname'] = userdetails.name
            return redirect(index)
        
    elif trucktbl.objects.filter(email=email,password=password).exists():
        userdetails=trucktbl.objects.get(email=request.POST['email'], password=password)
        if userdetails.password == request.POST['password']:
            request.session['tid'] = userdetails.id
            request.session['tname'] = userdetails.tname
            return redirect(index)
        
    elif charitytbl.objects.filter(email=email,password=password,status='accepted').exists():
        userdetails=charitytbl.objects.get(email=request.POST['email'], password=password)
        if userdetails.password == request.POST['password']:
            request.session['cid'] = userdetails.id
            request.session['cname'] = userdetails.cname
            return redirect(index)    
    
    else:
        return render(request, 'login.html', {'message':'Invalid Email or Password'})
    
def logout(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return redirect(first)



def truck(request):
    return render(request,"addtruck.html")

def addtruck(request):
    if request.method=="POST":
        tname=request.POST.get('tname')
        no_plate=request.POST.get('no_plate')
        license_no=request.POST.get('license_no')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cus=trucktbl(tname=tname,no_plate=no_plate,license_no=license_no,email=email,password=password,status='available')
        cus.save()
    return render(request,"index.html", {'truck':'Succesfully Registered'})

def viewtruck(request):
    if 'admin' not in request.session: 
        return render(request, 'login.html', {'message1':'Login Required'})
    else:
        a=trucktbl.objects.all()
        return render(request,"viewtruck.html",{'result':a})

def truckprofile(request):
    if 'tid' not in request.session: 
        return render(request, 'login.html', {'message1':'Login Required'})
    else:
        id = request.session['tid']
        a=trucktbl.objects.get(id=id)
        return render (request,'truckprofile.html',{'result':a})

def viewuser(request):
    if 'admin' not in request.session: 
        return render(request, 'login.html', {'message1':'Login Required'})
    else:
        a=userregtbl.objects.all()
        return render(request,"viewuser.html",{'result':a})

def userprofile(request):
    if 'uid' not in request.session: 
        return render(request, 'login.html', {'message1':'Login Required'})
    else:
        id = request.session['uid']
        a=userregtbl.objects.get(id=id)
        return render (request,'userprofile.html',{'result':a})


def category(request):
    if 'admin' not in request.session: 
        return render(request, 'login.html', {'message1':'Login Required'})
    else:
        return render(request, 'addcategory.html')

def addcategory(request):
    if 'admin' not in request.session: 
        return render(request, 'login.html', {'message1':'Login Required'})
    elif request.method=="POST":
        name=request.POST.get('name')
        if categorytbl.objects.filter(name=name).exists():
            return render(request,"index.html",{'category':'Already Exist'})
            
        cus=categorytbl(name=name)
        cus.save()
    return render(request,"index.html",{'category':'Added Succesfully '})

def food(request):
    if 'uid' not in request.session: 
        return render(request, 'login.html', {'message1':'Login Required'})
    else:
        a=categorytbl.objects.all()
        b=request.session['uid']
        c=request.session['uname']
        return render(request,"addfood.html",{'res':a,'result':b,'resu':c})

'''def addfood(request):
    if request.method=="POST":
        uname=request.POST.get('uname')
        uid=request.POST.get('uid')
        food_name=request.POST.get('food_name')
        category=request.POST.get('category')
        district=request.POST.get('district')
        city=request.POST.get('city')
        quantity=request.POST.get('quantity')
        type=request.POST.get('type')
        p_date=request.POST.get('p_date')
        cus=foodtbl(uname=uname,uid=uid,food_name=food_name,category=category,type=type,
                        district=district,city=city,quantity=quantity,p_date=p_date,status='pending')
        cus.save()
        
        uid=request.session['uid']
        uname=request.session['uname']
        a=rewardtbl(uid=uid,uname=uname,point=100)
        a.save()
    return render(request,"addfood.html",{'msg':'Added Succesfully'})'''

from .models import rewardtbl

def addfood(request):
    if request.method == "POST":
        uname = request.POST.get('uname')
        uid = request.POST.get('uid')
        food_name = request.POST.get('food_name')
        category = request.POST.get('category')
        district = request.POST.get('district')
        city = request.POST.get('city')
        quantity = request.POST.get('quantity')
        type = request.POST.get('type')
        p_date = request.POST.get('p_date')
        
        # Save the food entry
        cus = foodtbl(uname=uname, uid=uid, food_name=food_name, category=category, type=type,
                      district=district, city=city, quantity=quantity, p_date=p_date, status='pending')
        cus.save()
        
        # Check if the user already has a reward point
        if 'uid' in request.session and 'uname' in request.session:
            uid = request.session['uid']
            uname = request.session['uname']
            try:
                # Fetch existing reward record for the user
                reward_record = rewardtbl.objects.get(uid=uid)
                # Update the existing reward point
                reward_record.point = str(int(float(reward_record.point)) + 100) # Assuming 100 is the next reward point
                reward_record.save()
            except rewardtbl.DoesNotExist:
                # If no existing record found, create a new one
                reward_record = rewardtbl(uid=uid, uname=uname, point=100)
                reward_record.save()
        
    return render(request, "index.html", {'msg4': 'Added Successfully'})


def viewfood(request):
    if 'admin' not in request.session: 
        return render(request, 'login.html', {'message1':'Login Required'})
    else:
        a=foodtbl.objects.all()
        return render(request,"viewfood.html",{'result':a})


def charity(request):
    return render(request,"addcharity.html")

def addcharity(request):
    if request.method=="POST":
        cname=request.POST.get('cname')
        c_license_no=request.POST.get('c_license_no')
        member=request.POST.get('member')
       
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cus=charitytbl(cname=cname,c_license_no=c_license_no,member=member,email=email,
                       address=address,phone=phone,password=password,status='pending')
        cus.save()
    return render(request,"index.html", {'message':'Succesfully Registered'})

def viewcharity(request):
    if 'admin' not in request.session: 
        return render(request, 'login.html', {'message1':'Login Required'})
    else:
        a=charitytbl.objects.all()
        return render(request,"viewcharity.html",{'result':a})

def charityprofile(request):
    if 'cid' not in request.session: 
        return render(request, 'login.html', {'message1':'Login Required'})
    else:
        id = request.session['cid']
        a=charitytbl.objects.get(id=id)
        return render (request,'charityprofile.html',{'result':a})

def viewfood_truck(request):
    a=foodtbl.objects.all()
    return render(request,"viewfood_truck.html",{'result':a})

def charityaccept(request,id):
    if 'admin' not in request.session: 
        return render(request, 'index.html', {'message3':'Login Required'})
    else:
        sel=charitytbl.objects.get(id=id)
        sel.status='accepted'
        sel.save()  
        return redirect(viewcharity)

def charityreject(request,id):
    if 'admin' not in request.session: 
        return render(request, 'index.html', {'message3':'Login Required'})
    else:
        sel=charitytbl.objects.get(id=id)
        sel.status='rejected'
        sel.save()  
        return redirect(viewcharity)

def viewfood_charity(request):
    if 'cid' not in request.session: 
        return render(request, 'login.html', {'message1':'Login Required'})
    else:
        a=foodtbl.objects.filter(status='pending')
        return render(request,"viewfood_charity.html",{'result':a})

def foodreqtoadmin(request,id):
    if 'cid' not in request.session: 
        return render(request, 'index.html', {'message3':'Login Required'})
    else:
        user=foodtbl.objects.get(id=id)
        return render(request,'foodreqtoadmin.html',{'result':user})

def addfoodreq(request,id):
    if request.method=="POST":
        cid=request.session['cid']
        cname=request.session['cname']
        uname=request.POST.get('uname')
        uid=request.POST.get('uid')
        food_name=request.POST.get('food_name')
        food_id=request.POST.get('food_id')
        date=request.POST.get('date')
        foodreq=get_object_or_404(foodtbl,id=id)
        foodreq.status = 'requested'
        foodreq.save()
        cus=foodreqtbl(cname=cname,cid=cid,uname=uname,uid=uid,food_name=food_name,food_id=food_id,date=date,status='requested')
        cus.save()
    return render(request,"index.html", {'message3':'Request has sent '})


def viewreqfood(request):
    if 'admin' not in request.session: 
        return render(request, 'login.html', {'message1':'Login Required'})
    else:
        a=foodreqtbl.objects.all()
        return render(request,"viewreqfood.html",{'result':a})

from django.http import Http404
from .models import foodreqtbl, foodtbl

def foodaccept(request, id):
    if 'admin' not in request.session: 
        return render(request, 'index.html', {'message3':'Login Required'})
    else:
        try:
            # Get the food request object
            sel = foodreqtbl.objects.get(id=id)
            sel.status = 'accepted'
            sel.save() 
            
            # Get the corresponding food object and delete it
            ''' food_id = sel.food_id
            food_obj = foodtbl.objects.get(id=food_id)
            food_obj.delete()'''
            
            return redirect(viewreqfood)
        
        except foodreqtbl.DoesNotExist:
            raise Http404("Food request does not exist.")
        except foodtbl.DoesNotExist:
            raise Http404("Food does not exist.")


def foodreject(request,id):
    if 'admin' not in request.session: 
        return render(request, 'index.html', {'message3':'Login Required'})
    else:
        sel=foodreqtbl.objects.get(id=id)
        sel.status='rejected'
        sel.save()
        fooddet=get_object_or_404(foodtbl,id=sel.food_id) 
        fooddet.status = 'pending'
        fooddet.save() 
        return redirect(viewreqfood)

def assigntruck(request,id):
    if 'admin' not in request.session: 
        return render(request, 'index.html', {'message3':'Login Required'})
    else:
        food=foodreqtbl.objects.get(id=id)
        truck=trucktbl.objects.filter(status='available')
        '''for i in pick:
            for j in worker:
                if str(i.uid)==str(j.id):
                    i.uid=j.name'''
        return render (request,'assigntruck.html',{'result':food,'res':truck})

def assignwork(request,id):
    if request.method=="POST":
        a=request.POST.get('tname')
        b=request.POST.get('cname')
        c=request.POST.get('cid')
        d=request.POST.get('food_name')
        e=request.POST.get('food_id')
        cus=assigntbl(fdreq_id=id,tname=a,cname=b,cid=c,food_name=d,food_id=e,status='pending')
        cus.save()
        food_request = get_object_or_404(foodreqtbl, id=id)
        food_request.status = 'assigned'
        food_request.save()
    return render(request,"index.html",{'assign':'Request has been sent'})

from django.core.exceptions import ObjectDoesNotExist

def viewrequest(request):
    if 'tid' not in request.session: 
        return render(request, 'login.html', {'message1':'Login Required'})
    else:
        try:
            id = request.session['tname']
            cus = assigntbl.objects.filter(tname=id)
            
            return render(request, 'viewrequest.html', {'result': cus })
        except ObjectDoesNotExist:
            return render(request, 'viewrequest.html', {'result': None})
        
def truckaccept(request,id):
    if 'tid' not in request.session: 
        return render(request, 'index.html', {'message3':'Login Required'})
    else:
        sel=assigntbl.objects.get(id=id)
        sel.status='accepted'
        sel.save()  
    
        '''a=foodreqtbl.objects.get(id=id)
        a.delete()'''
        return redirect(viewrequest)

def truckreject(request,id):
    if 'tid' not in request.session: 
        return render(request, 'index.html', {'message3':'Login Required'})
    else:
        sel=assigntbl.objects.get(id=id)
        sel.status='rejected'
        sel.save()
        food_request = get_object_or_404(foodreqtbl, id=sel.fdreq_id)
        food_request.status = 'accepted'
        food_request.save()  
        return redirect(viewrequest)

def delivery(request,id):
    if 'tid' not in request.session: 
        return render(request, 'index.html', {'message3':'Login Required'})
    else:
        a=assigntbl.objects.get(id=id)
        return render(request,'adddelivery.html',{'result':a})

def adddelivery(request,id):
    if request.method=="POST":
        a=request.POST.get('tname')
        b=request.POST.get('cname')
        c=request.POST.get('cid')
        d=request.POST.get('food_name')
        e=request.POST.get('food_id')
        cus=delivertbl(tname=a,cname=b,cid=c,food_name=d,food_id=e,status='delivered',id=id)
        abc=assigntbl.objects.get(id=id)
        abc.status='delivered'
        abc.save()
        asd=foodtbl.objects.get(id=e)
        asd.status='delivered'
        asd.save()
        cus.save()
        food_obj = foodreqtbl.objects.get(id=abc.fdreq_id)
        food_obj.status = 'Delivered'
        food_obj.save()
    return render(request,"index.html", {'delivery':'Succesfully Delivered'})

def truckstatus(request):
    if 'admin' not in request.session: 
        return render(request, 'login.html', {'message1':'Login Required'})
    else:
        a=assigntbl.objects.all()
        return render(request,'viewtruckstatus.html',{'result':a})

def product(request): 
    if 'admin' not in request.session: 
        return render(request, 'login.html', {'message1':'Login Required'})
    else:
        return render(request,'addproduct.html')

def addproduct(request):
    if 'admin' not in request.session: 
        return render(request, 'login.html', {'message1':'Login Required'})
    elif request.method=="POST":
   
        name=request.POST.get('name')
        quantity=request.POST.get('quantity')
        price=request.POST.get('price')
        description=request.POST.get('description')
        myfile=request.FILES['image']
        fs= FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        cus=products(name=name,quantity=quantity,price=price,description=description,image=filename)
        cus.save()
        return render(request,"index.html", {'product':' Added Succesfully'})
    else:
        return render(request,"addproduct.html")
    
def viewproduct(request):
    if 'admin' not in request.session: 
        return render(request, 'login.html', {'message1':'Login Required'})
    else:
        a=products.objects.all()
        return render(request,'viewproduct.html',{'result':a})

def viewproduct_user(request):
    if 'uid' not in request.session: 
        return render(request, 'login.html', {'message1':'Login Required'})
    else:
        a=products.objects.all()
        return render(request,'viewproduct_user.html',{'result':a})


def add_to_cart(request, product_id):
    if 'uid' not in request.session: 
        return render(request, 'index.html', {'message3':'Login Required'})
    else:
        userr = request.session.get('uid')

        existing_item = cartitems.objects.filter(user=userr, product_id=product_id).first()

        if existing_item:
            return render(request, 'index.html', {'message': 'Product Already Exists in the Cart'})
        else:
            cart_item = cartitems(user=userr, product_id=product_id, quantity=1)
            cart_item.save()

            return redirect(view_cart)

def view_cart(request):
    if 'uid' not in request.session: 
        return render(request, 'login.html', {'message1':'Login Required'})
    else:
        userr = request.session.get('uid')

        # Assuming product_id is stored in cartitems as product_id
        cart_items = cartitems.objects.filter(user=userr)

        # Calculate subtotal for each product in the cart
        subtotal_per_product = []
        total_price = 0
        total_items = 0 
        cart_item_details = [] 
        for item in cart_items:
            product = products.objects.get(id=item.product_id)
            subtotal = float(product.price) * item.quantity
            subtotal_per_product.append({'product': product, 'subtotal': subtotal,'quantity': item.quantity,'item_id':item.id})
            total_price += subtotal
            total_items += item.quantity
            cart_item_details.append({'name': product.name, 'quantity': item.quantity})
            

        return render(request, 'cart.html', {'subtotal_per_product': subtotal_per_product, 'total_price': total_price, 'total_items': total_items,'cart_item_details': cart_item_details})

def remove_cart_item(request,id):
    if 'uid' not in request.session: 
        return render(request, 'index.html', {'message3':'Login Required'})
    else:
        a=cartitems.objects.get(id=id)
        a.delete()
        return redirect(view_cart)

def addquantity(request, id):
    if 'uid' not in request.session: 
        return render(request, 'index.html', {'message3':'Login Required'})
    else:
        item = get_object_or_404(cartitems, id=id)

        if request.method == "POST":
            qnty = request.POST.get('quantity')

            item.quantity = qnty
            item.save()

        return redirect(view_cart)


from django.shortcuts import render
from .models import rewardtbl

def buy_all(request):
    if 'uid' not in request.session: 
        return render(request, 'login.html', {'message1':'Login Required'})
    else:
        id = request.session['uid']
        user_reward = rewardtbl.objects.get(uid=id)
        user_points = float(user_reward.point)  # Convert to float
        total_items = request.GET.get('total_items', 0)
        total_price = request.GET.get('total_price', 0)

        # Calculate subtotal after deducting points
        sub_total = max(float(total_price) - user_points, 0)

        # Get a list of dictionaries containing product names and quantities
        cart_item_details = [
            {
                'name': request.GET.get(f'cart_item_{i}_name', 'Unknown Product'),
                'quantity': request.GET.get(f'cart_item_{i}_quantity', 0)
            }
            for i in range(int(total_items))
        ]

        # Filter out items with unknown names or quantities
        cart_item_details = [item for item in cart_item_details if item['name'] != 'Unknown Product' and item['quantity'] != '0']
        product_names = [item['name'] for item in cart_item_details]

        # Update reward points after purchase
        # Assuming you have a function to deduct points from the user's rewardtbl object
        # Example: user_reward.deduct_points(points_to_deduct)
        # You need to replace 'points_to_deduct' with the appropriate value based on the purchase
        

        # Render the buy_all.html template with the relevant data
        return render(request, 'buy_all.html', {'total_items': total_items,'total_price':total_price, 'sub_total': sub_total, 'cart_item_details': cart_item_details, 'product_names': product_names})


def purchase(request):
    if request.method == "POST":
        userr = request.session.get('uid')
        product = request.POST.get('product')
        total_item = request.POST.get('total_item')
        total_price = request.POST.get('total_price')
        sub_total = request.POST.get('sub_total')
        card_name = request.POST.get('card_name','Reward')
        card_number = request.POST.get('card_number',0)
        cvv = request.POST.get('cvv',0)
        id = request.session['uid']
        user_reward = rewardtbl.objects.get(uid=id)
        user_points = float(user_reward.point)
        points_to_deduct = 0
        if user_points > float(total_price):
            points_to_deduct = float(user_points) - float(total_price)
        elif user_points <= float(total_price):
            points_to_deduct = float(total_price)
    # Deduct points from the user's reward points
        user_reward.point = str(max(float(user_reward.point) - points_to_deduct, 0))
        user_reward.save()  
        cus = purchases(
            userr=userr,
            product=product,
            total_item=total_item,
            total_price=sub_total,
            card_name=card_name,
            card_number=card_number,
            cvv=cvv,
            status='Confirmed'
        )
        cus.save()

        cartitems.objects.filter(user=userr).delete()

        return render(request, "index.html", {'message': 'Successfully Purchased'})

    return render(request, "index.html", {'message': 'Invalid Request'})

def viewuserrewards(request):
    if 'admin' not in request.session: 
        return render(request, 'login.html', {'message1':'Login Required'})
    else:
        a=rewardtbl.objects.all()
        return render(request,'viewuserrewards.html',{'result':a})

from django.core.exceptions import ObjectDoesNotExist

def viewreward(request):
    if 'uid' not in request.session: 
        return render(request, 'login.html', {'message1':'Login Required'})
    else:
        try:
            id = request.session['uid']
            a = rewardtbl.objects.get(uid=id)
            return render(request, 'viewreward.html', {'result': a})
        except ObjectDoesNotExist:
            return render(request, 'viewreward.html', {'msg': 'No reward found for the current user'})


from django.core.exceptions import ObjectDoesNotExist

def allocated_charity(request):
    if 'uid' not in request.session: 
        return render(request, 'login.html', {'message1':'Login Required'})
    else:
        try:
            id = request.session['uid']
            a = foodreqtbl.objects.filter(uid=id)
            
            if a.exists():
                return render(request, 'allocated_charity.html', {'result': a})
            else:
                return render(request, 'allocated_charity_none.html', {'result': None})
        except ObjectDoesNotExist:
            return render(request, 'allocated_charity_none.html', {'result': None})


def vieworders(request):
    if 'uid' not in request.session: 
        return render(request, 'login.html', {'message1':'Login Required'})
    else:
        try:
            id = request.session['uid']
            user = userregtbl.objects.get(id=id)
            fd = purchases.objects.filter(userr=user.id)
            
            for item in fd:
                item.userr = user.name
        
            return render(request, 'vieworders.html', {'result': fd})
        except KeyError:
            # Handle the case where 'uid' is not set in the session
            return HttpResponse("Session variable 'uid' is not set.", status=400)
        except userregtbl.DoesNotExist:
            # Handle the case where user with given 'uid' doesn't exist
            return HttpResponse("User with given 'uid' doesn't exist.", status=404)
        except Exception as e:
            # Handle any other unexpected errors
            return HttpResponse("An error occurred while processing your request.", status=500)

def vieworders_admin(request):
    if 'admin' not in request.session: 
        return render(request, 'login.html', {'message1':'Login Required'})
    else:
        fd = purchases.objects.all()
        user3 = userregtbl.objects.all()
        
        for item in fd:
            for user in user3:
                if str(item.userr) == str(user.id):
                    item.userr = user.name
        
        return render(request, 'vieworders.html', {'result': fd})

def vieworders_truck(request):
    if 'tid' not in request.session: 
        return render(request, 'login.html', {'message1':'Login Required'})
    else:
        id = request.session['tname']
        fd = delivertbl.objects.filter(tname=id)
        return render(request, 'vieworders_truck.html', {'result': fd})

def vieworders_charity(request):
    if 'cid' not in request.session: 
        return render(request, 'login.html', {'message1':'Login Required'})
    else:
        id = request.session['cid']
        fd = foodreqtbl.objects.filter(cid=id)
        return render(request, 'vieworders_charity.html', {'result': fd})


def viewallocatedtruck(request):
    if 'cid' not in request.session: 
        return render(request, 'login.html', {'message1':'Login Required'})
    else:
        id = request.session['cid']
        fd = delivertbl.objects.filter(cid=id)
        return render(request, 'viewallocatedtruck.html', {'result': fd})


def addfeed(request):
    if 'cid' not in request.session: 
        return render(request, 'login.html', {'message1':'Login Required'})
    elif request.method=="POST":
        cname=request.session['cname'] 
        feedback=request.POST.get('feedback')
       
        cus=feedbacktbl(cname=cname,feedback=feedback)
        cus.save()
        return render(request,"index.html", {'message1':'Succesfully Added You Feedback'})
    else:
        return render(request,"feedback.html")

def view_feedbacks(request):
    if 'admin' not in request.session: 
        return render(request, 'login.html', {'message1':'Login Required'})
    else:
        fd=feedbacktbl.objects.all()
        return render(request,'view_feedbacks.html',{'result':fd})

def addcomplaint(request):
    if 'cid' not in request.session: 
        return render(request, 'login.html', {'message1':'Login Required'})
    elif request.method=="POST":
        cname=request.session['cname'] 
        msg=request.POST.get('msg')       
        cus=complainttbl(cname=cname,msg=msg)
        cus.save()
        return render(request,"index.html", {'message2':'Succesfully Added You Complaint'})
    else:
        return render(request,"complaint.html")

def view_complaint(request):
    if 'admin' not in request.session: 
        return render(request, 'login.html', {'message1':'Login Required'})
    else:
        fd=complainttbl.objects.all()
        return render(request,'view_complaint.html',{'result':fd})

def reply(request,id):
    if 'admin' not in request.session: 
        return render(request, 'index.html', {'message3':'Login Required'})
    else:
        sel=complainttbl.objects.get(id=id)
        return render(request,'reply.html',{'result':sel})

def addrply(request,id):
    if request.method == 'POST':
        cname=request.POST['cname']
        l=request.POST['msg']
        m=request.POST['reply']
        data = complainttbl(cname=cname,msg=l,reply=m,id=id)
        data.save()
        return redirect(view_complaint)
    
def view_complaint_charity(request):
    if 'cid' not in request.session: 
        return render(request, 'login.html', {'message1':'Login Required'})
    else:
        fd=complainttbl.objects.all()
        return render(request,'view_complaint_charity.html',{'result':fd})

