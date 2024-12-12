from unicodedata import category
from django import forms
from newsP import models
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm, UserChangeForm
from django.contrib.auth.models import User

class UpdateProfile(UserChangeForm):
    username = forms.CharField(max_length=250,help_text="Please fill the username field")
    email = forms.EmailField(max_length=250,help_text="Please fill the Email field")
    first_name = forms.CharField(max_length=250,help_text="Please fill the first name field")
    last_name = forms.CharField(max_length=250,help_text="Please fill the last name field")
    current_password = forms.CharField(max_length=250)

    class Meta:
        model = User
        fields = ('email', 'username','first_name', 'last_name')

    def clean_current_password(self):
        if not self.instance.check_password(self.cleaned_data['current_password']):
            raise forms.ValidationError(f"Password is incorrect")

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            user = User.objects.exclude(id=self.cleaned_data['id']).get(email = email)
        except Exception as e:
            return email
        raise forms.ValidationError(f"{user.email} mail already exists")

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            user = User.objects.exclude(id=self.cleaned_data['id']).get(username = username)
        except Exception as e:
            return username
        raise forms.ValidationError(f"{user.username} mail already exists")

class UpdatePasswords(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm rounded-0'}), label="Old Password")
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm rounded-0'}), label="New Password")
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm rounded-0'}), label="Confirm New Password")
    class Meta:
        model = User
        fields = ('old_password','new_password1', 'new_password2')

class savePost(forms.ModelForm):
    user = forms.CharField(max_length=30,label="Author")
    category = forms.CharField(max_length=30,label="Category")
    title = forms.CharField(max_length=250,label="Title")
    content = forms.Textarea()
    banner_path = forms.ImageField(label="Banner Image")
    status = forms.CharField(max_length=2)


    class Meta():
        model = models.Post
        fields = ('user', 'category', 'title', 'content', 'banner_path', 'status',)

    def clean_category(self):
        catID = self.cleaned_data['category']
        try:
            category = models.Category.objects.get(id = catID)
            return category
        except:
            raise forms.ValidationError('Selected Category is invalid')

    
    def clean_user(self):
        userID = self.cleaned_data['user']
        try:
            user = models.User.objects.get(id = userID)
            return user
        except:
            raise forms.ValidationError('Selected User is invalid')


class saveComment(forms.ModelForm):
    post = forms.CharField(max_length=30,label="Post")
    name = forms.CharField(max_length=250,label="Name")
    email = forms.CharField(max_length=250,label="Email")
    subject = forms.CharField(max_length=250,label="Subject")
    message = forms.Textarea()
    class Meta():
        model = models.Comment
        fields = ('post', 'name', 'email', 'subject', 'message',)

    def clean_post(self):
        postID = self.cleaned_data['post']
        try:
            post = models.Post.objects.get(id = postID)
            return post
        except:
            raise forms.ValidationError('Post ID is invalid')

    
