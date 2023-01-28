from django import forms

class IndexForm(forms.Form):
    start_date = forms.DateField(widget=forms.DateInput(
        attrs={'class': "form-control", 'type': 'date'}))
    start_time = forms.TimeField(widget=forms.TimeInput(
        attrs={'class': "form-control", 'type': 'time'}))
    end_date = forms.DateField(widget=forms.DateInput(
        attrs={'class': "form-control", 'type': 'date'}))
    end_time = forms.TimeField(widget=forms.TimeInput(
        attrs={'class': "form-control", 'type': 'time'}))


