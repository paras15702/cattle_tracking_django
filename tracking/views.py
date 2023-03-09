from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from .models import Cattle,Farmer
from .forms import CattleForm,FarmerForm,CreateUserForm
from .filters import CattleFilter,FarmerFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decoraters import unauthenticated_user,allowed_users
from .utils import get_location_data
from django.db.models import Count


@login_required(login_url='login')
def index(request):
   return render(request,'tracking/index.html')


@login_required(login_url='login')
def view_farmerlist(request):
    farmer= Farmer.objects.all()
    myFilter=FarmerFilter(request.GET , queryset=farmer)
    farmer=myFilter.qs
    context= {'farmer':farmer,'myFilter':myFilter}
    return render(request, 'tracking/view_farmerlist.html',context)


@login_required(login_url='login')
@allowed_users(allowed_rules=['admin'])
def add_cattle(request):

    form= CattleForm()
    context={'form':form}
    if request.method =='POST':
        #print("Printing POST:",request.POST)
        form = CattleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'tracking/cattleform.html',context)    


@login_required(login_url='login')
@allowed_users(allowed_rules=['admin'])
def update_cattle(request,pk):
    cattle=Cattle.objects.get(id=pk)
    form=CattleForm(instance=cattle)
    context = {'form':form}
    if request.method =='POST':
        #print("Printing POST:",request.POST)
        form = CattleForm(request.POST,instance=cattle)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'tracking/cattleform.html',context)


@login_required(login_url='login')
@allowed_users(allowed_rules=['admin'])
def delete_cattle(request,pk):
    cattle=Cattle.objects.get(id=pk)
    if request.method =='POST':
        cattle.delete()
        return redirect('/')
    context={'cattle':cattle}
    return render(request,'tracking/delete.html',context)


@login_required(login_url='login')

def view_cattle(request,pk):
    farmer1=Farmer.objects.all()
    farmer = Farmer.objects.get(id=pk)
    cattle=farmer.cattle_set.all()
    cattle_count=cattle.count()
    
    pregnant_count = cattle.filter(pregnant=True).aggregate(Count('id'))['id__count']
    lost_count=cattle.filter(lost_status=True).aggregate(Count('id'))['id__count']
    myFilter=CattleFilter(request.GET , queryset=cattle)
    
    cattle=myFilter.qs
    context= {'farmer':farmer,'cattle':cattle,'farmer1':farmer1,'myFilter':myFilter,'cattle_count':cattle_count ,'pregnant_count':pregnant_count,'lost_count':lost_count}
    return render(request,'tracking/view_cattles.html',context)


@login_required(login_url='login')
@allowed_users(allowed_rules=['admin'])
def add_farmer(request):
    
    form1= FarmerForm()
    context={'form1':form1}
    if request.method =='POST':
        #print("Printing POST:",request.POST)
        form1 = FarmerForm(request.POST , request.FILES)
        if form1.is_valid():
            form1.save()
            return redirect('/')
    return render(request, 'tracking/farmerform.html',context)   


@login_required(login_url='login')
@allowed_users(allowed_rules=['admin'])
def update_farmer(request,pk):
    farmer=Farmer.objects.get(id=pk)
    form1=FarmerForm(instance=farmer)
    
    
    context = {'form1':form1}
    if request.method =='POST':
        #print("Printing POST:",request.POST)
        form1 = FarmerForm(request.POST,request.FILES,instance=farmer )
        if form1.is_valid():
            form1.save()
            return redirect('/')
    return render(request,'tracking/farmerform.html',context)      


@login_required(login_url='login')
@allowed_users(allowed_rules=['admin'])
def delete_farmer(request,pk):
    farmer=Farmer.objects.get(id=pk)
    if request.method =='POST':
        farmer.delete()
        return redirect('/') 
    context={'farmer':farmer}
    return render(request,'tracking/deletefarmer.html',context)    

@unauthenticated_user
def registerPage(request):

        form=CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('login')
        context={'form':form}
        return render(request,'tracking/register.html',context)    


@unauthenticated_user
def logInPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    else:
        if request.method=="POST" :
            username= request.POST.get('username')
            password=request.POST.get("password")

            user = authenticate(request,username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.info(request,'USERNAME OR PASSWORD INVALID')
                return render(request,'tracking/login.html') 
        context={}
        return render(request,'tracking/login.html',context)    


def logOutUser(request):
    logout(request)
    return redirect('login')    



def live_tracking(request):
    return render(request, 'tracking/live_tracking.html')


# def live_tracking(request):
    gpsd.connect()
    packet = gpsd.get_current()
    GPSData.objects.create(latitude=packet.lat, longitude=packet.lon)
    return render(request, 'live_tracking.html', {'latitude': packet.lat, 'longitude': packet.lon})


@login_required(login_url='login')
def viewfarmer(request,pk):
    
    farmer=Farmer.objects.get(id=pk)
    context={'farmer':farmer}
    return render(request,'tracking/viewfarmer.html',context)


# def live_tracking(request):
#     return render(request,'tracking/live_tracking.html')    

# def status(request,pk):
   
#     return render(request,'tracking/view_cattles.html',context)

@login_required(login_url='login')
def my_view(request,pk):
    cattle = Cattle.objects.get(id=pk)
    address=cattle.location
    location = get_location_data(address)
    return render(request, 'tracking/live_tracking.html', {'location': location})


@login_required(login_url='login')
def cattleinfo(request,pk):
    
    cattle=Cattle.objects.get(id=pk)
    context={'cattle':cattle}
    return render(request,'tracking/cattleinfo.html',context)