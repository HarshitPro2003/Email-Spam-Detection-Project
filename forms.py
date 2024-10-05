from django import forms 

class MessageForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your message here...'}))