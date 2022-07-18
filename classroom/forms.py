from django import forms

# form for students to join a new class
class JoinClassForm(forms.Form):
    join_code = forms.CharField(label='Join code',max_length=10)