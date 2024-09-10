from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from allauth.account.utils import send_email_confirmation
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Education
from .forms import EmailForm, ProfileForm, ChildInfoForm, EducationForm

def profile_view(request, username=None):
    context = {}
    if username:
        profile = get_object_or_404(User, username=username).profile
    else:
        try:
            profile = request.user.profile
            info = request.user.profile.childinfo
            education = Education.objects.filter(profile=request.user.profile).all()

            
            context = {
                'profile': profile,
                'info': info,
                'education': education
            }
        except:
            profile = request.user.profile
            context = {
                'profile': profile
            }

    return render(request, 'a_users/profile.html', context)


@login_required
def profile_edit_view(request):
    form = ProfileForm(instance=request.user.profile)  
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
        
    if request.path == reverse('profile-onboarding'):
        onboarding = True
    else:
        onboarding = False

    return render(request, 'a_users/profile_edit.html', { 'form':form, 'onboarding':onboarding })

def childinfo_edit_view(request):
    form = ChildInfoForm(instance=request.user.profile.childinfo)

    if request.method == 'POST':
        form = ChildInfoForm(request.POST, instance=request.user.profile.info)
        if form.is_valid():
            form.save()
            return redirect('edit_education')#switch to education edit view
        
    #change the template name to child info edit
    return render(request, 'a_user/childinfo_edit.html', {'form': form})


@login_required
def education_edit_view(request, id):
    obj = get_object_or_404(Education, id=id)
    form = EducationForm(instance=obj)
    if request.method == 'POST':
        form = EducationForm(request.POST, instance=obj)

        if form.is_valid():
            form.save()
        redirect('profile')

    return render(request, 'a_users/education_edit.html', {'form': form})


@login_required
def profile_settings_view(request):
    return render(request, 'a_users/profile_settings.html')


@login_required
def profile_emailchange(request):
    
    if request.htmx:
        form = EmailForm(instance=request.user)
        return render(request, 'partials/email_form.html', {'form':form})
    
    if request.method == 'POST':
        form = EmailForm(request.POST, instance=request.user)

        if form.is_valid():
            
            # Check if the email already exists
            email = form.cleaned_data['email']
            if User.objects.filter(email=email).exclude(id=request.user.id).exists():
                messages.warning(request, f'{email} is already in use.')
                return redirect('profile-settings')
            
            form.save() 
            
            # Then Signal updates emailaddress and set verified to False
            
            # Then send confirmation email 
            send_email_confirmation(request, request.user)
            
            return redirect('profile-settings')
        else:
            messages.warning(request, 'Form not valid')
            return redirect('profile-settings')
        
    return redirect('home')


@login_required
def profile_emailverify(request):
    send_email_confirmation(request, request.user)
    return redirect('profile-settings')


@login_required
def profile_delete_view(request):
    user = request.user
    if request.method == "POST":
        logout(request)
        user.delete()
        messages.success(request, 'Account deleted, what a pity')
        return redirect('home')
    
    return render(request, 'a_users/profile_delete.html')