from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from user.tokens import account_activation_token
from .forms import *
from django.contrib.auth import login, authenticate
from .models import UserModel
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text


def log_in(request):
    log_in_form = LogInForm()
    sing_up_form = SignUpForm()
    if request.method == "POST":
        if "btn-login" in request.POST:
            log_in_form = LogInForm(request.POST)
            if log_in_form.is_valid():
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    user.is_active = True
                    return redirect("/profile")
        else:
            if request.method == 'POST':
                sing_up_form = SignUpForm(request.POST)
                if sing_up_form.is_valid():
                    user = sing_up_form.save(commit=False)
                    user.is_active = False
                    user.save()
                    current_site = get_current_site(request)
                    message = render_to_string('account_activation_email.html', {
                        'user': user,
                        'domain': current_site.domain,
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': account_activation_token.make_token(user),
                    })
                    mail_subject = 'Activate your account.'
                    to_email = sing_up_form.cleaned_data.get('email')
                    email = EmailMessage(mail_subject, message, to=[to_email])
                    email.send()
                    return HttpResponse('Please confirm your email address to complete the registration')
    return render(request, 'log_register.html', {'login_form': log_in_form, 'signup_form': sing_up_form})


def user_profile(request):
    return render(request, "user_profile.html")


def activate(self, request, uidb64, token, backend='django.contrib.auth.backends.ModelBackend'):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = UserModel.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user, backend)
        return HttpResponse('you can login')
    else:
        return HttpResponse('activation link is invalid!')
