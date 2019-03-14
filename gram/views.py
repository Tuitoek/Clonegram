from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Image, Profile,User
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, CommentsForm, ProfileUpdateForm, UserUpdateForm,PhotoForm
from django.forms import modelformset_factory



# Create your views here.
def landing(request):
    return render(request, 'landing.html')


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user.form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'confirm your Snapgram Account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('<h3>We have sent a link to your email,please follow the link to confirm the signup')
    else:
        form = SignUpForm()
    return render(request, 'regsistration/signup.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_basee64(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueErrror, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_token.check_token(user, token):
        user.is_activate = True
        user.save()
        login(request, user)

        return HttpResponse('<h4>Thank you for your email confimation.To login to your  account,<a href="account/login"Click here')
    else:
        return HttpResponse('<h1 style="color:red">Activation link is invalid!</h1>')

@login_required(login_url='/accounts/login/')

def edit_dp(request):
    img = Image.objects.all()
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'editdp.html',context,{'img':img })

def profile(request):
    img = Image.objects.all()

    return render(request, 'profile.html',{'img':img })


def test_redirect(request):
    return redirect("admin/")

@login_required(login_url='/accounts/login/')
def home2(request):
    # images = Image.objects.all()
    # print(images)
    # if request.method == 'POST':
    #     comment_form = CommentsForm(request.POST)
    #     if  comment_form.is_valid():
    #         comment = comment_form.save(commit=False)
    #         comment.save()
    #         return render(request,'home2.html',{"comment":comment})
    # else:
    #     comment_form = CommentsForm()
    # context = {
    #     'comment_form': comment_form,
    # }
    img = Image.objects.all()
    return render(request, 'home2.html',{'img':img })
    #return render(request, 'home2.html',context, {"images": images, 'img':img })


def image_form_upload(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'home2.html')
    else:
        form = PhotoForm()
    return render(request, 'upload.html', {
        'form': form
    })


def searchresults(request):
    images_item = Image.objects.all()
    if 'users' in request.GET.get('users'):
        searched_item = request.GET.get("users")
        searched_users = Image.search_by_username(search_term)
        message = f"{search_term}"
        return render(request, 'search.html', {"message": message, "users": searched_users})
    else:
        message = "You haven't searched for any term"
    return render(request,'search.html', {"message": message,"images_item":images_item})


def login(request):
    return render(request, 'registration/login.html')


def signup(request):
    return render(request, 'registration/signup.html')


def logout(request):
    return render(request, 'landing.html')


def comments(request):
    comments = CommentsForm()
    return render(request, 'comments.html,{"comments":comments}')


def profile_form(request):
    return render(request, 'profile-form.html')
