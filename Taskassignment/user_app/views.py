from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from .forms import fileform
from .models import UserModel

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if UserModel.objects.filter(username=username):
            if UserModel.objects.filter(username=username).values_list('is_admin', flat=True).first():
                admin_password = UserModel.objects.filter(username=username).values_list('password', flat=True).first()
                unapproved_users = UserModel.objects.filter(is_approval="False")
                approved_users = UserModel.objects.filter(is_approval="True")
                reject_users = UserModel.objects.filter(is_approval="None")
                
                context = {
                            'unapproved_users': unapproved_users,
                            'approved_users' : approved_users,
                            'reject_users' : reject_users,
                        }
                
                if admin_password == password:
                    return render(request, 'approval.html', context) 
                else:
                    messages.warning(request, "Invalid Admin Password")
                    return redirect('/login')
                
            if UserModel.objects.filter(username=username).values_list('is_approval', flat=True).first() == "True":   
                model_password = UserModel.objects.filter(username=username).values_list('password', flat=True).first()
                if model_password == password:
                    user = UserModel.objects.get(username=username)
                    id = user.id                                                   
                    return redirect(f"/files/{id}")   
                else:
                    messages.warning(request, "Invalid Password")
                    return redirect('/login')
            else:
                print(UserModel.objects.filter(username=username).values_list('password', flat=True).first())
                messages.warning(request, "Your Not Approved by Admin! wait for Approval")
                return redirect('/login')
        else:
            messages.warning(request, "User Name does't exist")
            return redirect('/login')
    else:
        return render(request, 'login.html')
    


    
def register(request):
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        #phone = request.POST['phone']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if UserModel.objects.filter(username=username).exists():
                messages.warning(request, "Username already taken")
                return redirect('/')
            elif UserModel.objects.filter(email=email).exists():
                messages.warning(request, "Email already taken")
                return redirect('/')
            else:
                if first_name == "" or last_name == "" or username == "" or email == ""  or password == "" or password2 == "":
                    messages.warning(request, "Enter All the Fields")
                    return redirect('/')
                else:
                    new_user = UserModel()
                    new_user.fname = first_name
                    new_user.lname = last_name
                    new_user.username = username
                    new_user.email = email
                    new_user.password = password
                    new_user.password2 = password2
                    new_user.is_approval = "False" 
                    new_user.is_admin = False  
                    new_user.save()
                    messages.success(request, "Registration Successful")
                    return redirect('/login')
        else:
            messages.error(request, "Passwords didn't match")
            return redirect('/')
    else:
        return render(request, 'register.html')
    

def files(request, id):                                                        
    formfile = fileform()                                                    
    files = fileform(request.POST, request.FILES)                            
    if files.is_valid():                                                    
        user = UserModel.objects.get(id=id)
        user.image = request.FILES["user_image"]
        print(user.image)
        user.save()
        return redirect('/login')
    return render(request, "upload.html", {'formfile' : formfile, 'id': id})


def approve(request, id):
    user = UserModel.objects.get(id=id)
    user.is_approval = "True"
    user.save()

    unapproved_users = UserModel.objects.filter(is_approval="False")
    approved_users = UserModel.objects.filter(is_approval="True")
    reject_users = UserModel.objects.filter(is_approval="None")
                
    context = {
                'unapproved_users': unapproved_users,
                'approved_users' : approved_users,
                'reject_users' : reject_users,
            }
    return render(request, "approval.html",context)

def reject(request, id):
    user = UserModel.objects.get(id=id)
    user.is_approval = "None"
    user.save()

    unapproved_users = UserModel.objects.filter(is_approval="False")
    approved_users = UserModel.objects.filter(is_approval="True")
    reject_users = UserModel.objects.filter(is_approval="None")
                
    context = {
                'unapproved_users': unapproved_users,
                'approved_users' : approved_users,
                'reject_users' : reject_users,
            }
    return render(request, "approval.html",context)
