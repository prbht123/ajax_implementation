from django.shortcuts import render
from .models import Profile,User
from .forms import UserRegister
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def home(request):
    return render(request,'getprofile.html')


def getProfile(request):
    profiles= Profile.objects.all()
    return JsonResponse({'profiles':list(profiles.values())})

def create(request):
    if request.method == "POST":
        user=request.POST['user']
        address=request.POST['address']
        contact=request.POST['contact']
        new_profile=Profile(user=user,address=address,contact=contact)
        new_profile.save()
        return HttpResponse("Successfully inserted data in db")


def UserregisterForm(request):
    form=UserRegister()
    users= User.objects.all()
    return render(request,'register.html',{'form':form,'users':users})


#@csrf_exempt
def save_data(request):
    if request.method == "POST":
        form=UserRegister(request.POST)
        if form.is_valid():
            name=request.POST['name']
            email=request.POST['email']
            password=request.POST['password']
            id=request.POST['sid']
            if id:
                msg="successfully updated the data of user : " + name
                user=User(id=id,name=name,email=email,password=password)
                
            else:
                msg="successfully added the data of user : " + name
                user=User(name=name,email=email,password=password)
            user.save()
            detail = User.objects.values()
            detail=list(detail)
            return JsonResponse({'status':'save','detail':detail,'msg':msg})
        else:
            return JsonResponse({'status':0})


def delete_data(request):
    print("oooooooooooooooooooo")
    if request.method == "POST":
        print("pppppppppppppppppppp")
        id=request.POST.get('sid')
        print(id)
        data=User.objects.get(pk=id)
        print(data)
        name=data.name
        data.delete()
        detail = User.objects.values()
        detail=list(detail)
        return JsonResponse({'status':'delete','detail':detail,'name':name})


def edit_data(request):
    print("oooooooooooooooooooo")
    if request.method == "POST":
        print("pppppppppppppppppppp")
        id=request.POST.get('sid')
        print(id)
        data=User.objects.get(pk=id)
        detail = {
            'name':data.name,
            'email':data.email,
            'password':data.password,
            'id':data.id
        }
        return JsonResponse({'status':'edit','detail':detail})



