from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Project,ProjectVideo,ProjectComment,ProjectPhoto

# here we are inheriting the user creating form that comes with Django, but we are adding the email field so 
# we can validate a user using their email
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']

# this will create a form that will allow a user to update their profile information
# a model form creates a form that is able to interact with a specific model
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['grade','image']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title','blurb','description']

class ProjectVideoForm(forms.ModelForm):
    class Meta:
        model = ProjectVideo
        fields = ['video']

class ProjectLinkForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_link']

class CommentForm(forms.ModelForm):
    class Meta:
        model = ProjectComment
        fields = ['content']

class ProjectPhotoForm(forms.ModelForm):
    class Meta:
        model = ProjectPhoto
        fields = ['image']