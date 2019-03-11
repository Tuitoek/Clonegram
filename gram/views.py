from django.shortcuts import render
from django.http import HttpResponse
from .models import Image,Profile
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm

@login_required(login_url='/accounts/login/')
# Create your views here.
def landing(request):
    return render(request,'landing.html')

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user.form.save(commit=False)
            user.is_active=False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'confirm your Snapgram Account.'
            message = render_to_string('acc_active_email.html',{
                'user':user,
                'domain':current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email=EmailMessage(
                mail_subject,message,to=[to_email]
            )
            email.send()
            return HttpResponse('<h3>We have sent a link to your email,please follow the link to confirm the signup')
    else:
        form = SignUpForm()
    return render(request,'regsistration/signup.html',{'form':form})

def activate(request,uidb64,token):
    try:
        uid = force_text(urlsafe_basee64(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError,ValueErrror,OverflowError,User.DoesNotExist):
        user=None
    if user is not None and account_token.check_token(user,token):
        user.is_activate = True
        user.save()
        login(request,user)

        return HttpResponse('<h4>Thank you for your email confimation.To login to your  account,<a href="account/login"Click here')
    else:
        return HttpResponse('<h1 style="color:red">Activation link is invalid!</h1>')




def profile(request):
    return render(request,'profile.html')

def home2(request):
    images=Image.objects.all()
    return render(request,'home2.html',{"images":images})

def searchresults(request):
    images_item=Image.objects.all()
    if 'users' in request.GET.get('users'):
        searched_item = request.GET.get("users")
        searched_users=Image.search_by_username(search_term)
        message = f"{search_term}"
        return render(request,'search.html',{"message":message,"users":searched_users})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def login(request):
    return render(request,'registration/login.html')

def signup(request):
    return render(request,'registration/signup.html')

def logout(request):
    return render(request,'landing.html') 
