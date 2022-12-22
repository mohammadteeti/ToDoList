from django import forms


class DeleteForm(forms.Form):
    answer=forms.CharField(max_length=100, required=False)