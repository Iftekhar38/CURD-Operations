from django import forms



class InsertForm(forms.Form):
    name = forms.CharField(max_length=30)
    rollno = forms.IntegerField()
    school = forms.CharField(max_length=70)
    address = forms.CharField(max_length=60)