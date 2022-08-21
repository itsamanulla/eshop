from django import forms
from django.core import validators
from .models import Product,Customers,Address
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

# class LoginForm(forms.ModelForm):
# 	class Meta:
# 		model=Customer
# 		fields=['email','password']
# 		widgets={'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Your Email'}),
# 		'password':forms.PasswordInput(attrs={'class':'form-control',
#         'placeholder':'Enter Your Password'}),
		
# 		}
		
	
# class RegisterForm(forms.ModelForm):
	
# 	class Meta:
# 		model=Customer
# 		fields=['first_name','last_name','mobile','email','password','retype_password']
# 		labels={'retype_password':'Password(again)'}
# 		help_text={'first_name':'Enter Your Name'}
# 		widgets={'first_name':forms.TextInput(attrs={'class':'form-control form-control-sm',
# 		'placeholder':'First Name'}),
# 		'last_name':forms.TextInput(attrs={'class':'form-control form-control-sm',
# 		'placeholder':'Last Name'}),
# 		'mobile':forms.TextInput(attrs={'class':'form-control form-control-sm',
# 		'placeholder':'Mobile No'}),
# 		'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Your Email'}),
# 		'password':forms.PasswordInput(attrs={'class':'form-control form-control-sm',
#         'placeholder':'Enter Your Password'}),
# 		'retype_password':forms.PasswordInput(attrs={'class':'form-control form-control-sm',
#         'placeholder':'Enter Your Password again'})
# 		}
	
# 	def clean(self):
# 		cleaned_data=super().clean()
# 		val1=self.cleaned_data['password']
# 		val2=self.cleaned_data['retype_password']
# 		if val1!=val2:
# 			raise forms.ValidationError('Password not matched')
	
	

class RegisterForm(UserCreationForm):
	password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm','placeholder':'Enter Your Password'}))
	password2=forms.CharField(label='Password(again)',widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm','placeholder':'Enter Your Password Again'}))
	
	class Meta:
		model=User
		fields=['username','first_name','last_name','email']
		labels={'email':'Email'}
		widgets={'username':forms.TextInput(attrs={'class':'form-control form-control-sm',
        'placeholder':'Enter Your UserName'}),
		'first_name':forms.TextInput(attrs={'class':'form-control form-control-sm',
 		'placeholder':'First Name'}),
 		'last_name':forms.TextInput(attrs={'class':'form-control form-control-sm',
 		'placeholder':'Last Name'}),
 		'mobile':forms.TextInput(attrs={'class':'form-control form-control-sm',
 		'placeholder':'Mobile No'}),
 		'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Your Email'}),
 		}
        
class LoginForm(forms.Form):
	username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm',
        'placeholder':'Enter Your UserName'}))
	password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm',
        'placeholder':'Enter Your Password'}))


class Profile(forms.ModelForm):
	class Meta:
		model=Customers
		fields=['mobile','state','city','pincode']
		widgets={'mobile':forms.NumberInput(attrs={'class':'form-control form-control-sm',
		'placeholder':'Mobile no'}),
        
		'state':forms.Select(attrs={'class':'form-control form-control-sm'}),
		'city':forms.TextInput(attrs={'class':'form-control form-control-sm',
		'placeholder':'City'}),
		'pincode':forms.NumberInput(attrs={'class':'form-control form-control-sm',
		'placeholder':'Pincode'}),
        }

class VendorForm(forms.ModelForm):
	
	class Meta:
		model=Product
		fields='__all__'
		widgets={'name':forms.TextInput(attrs={'class':'form-control form-control-sm',
		'placeholder':'Product Name'}),
		
		'price':forms.TextInput(attrs={'class':'form-control form-control-sm',
		'placeholder':'Price'}),
		'dis_price':forms.TextInput(attrs={'class':'form-control form-control-sm',
		'placeholder':'Price'}),
		'desc':forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Description'}),
		
		}

class AddressForm(forms.ModelForm):
	class Meta:
		model=Address
		fields=['address']
		widgets={'address':forms.TextInput(attrs={'class':'form-control form-control-sm',
		'placeholder':'Address'})}