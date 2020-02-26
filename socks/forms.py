from django import forms 

class Sort(forms.Form):
    choice = forms.CharField(max_length=10)


class Choice(forms.Form):
    CHOICES = (('Option 1', 'Option 1'),('Option 2', 'Option 2'),)