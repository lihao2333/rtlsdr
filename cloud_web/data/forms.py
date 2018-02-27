from django import forms
class DataUploadForm(forms.Form):
    loc_x = forms.FloatField()
    loc_y = forms.FloatField()
    fs = forms.FloatField()
    dt = forms.FloatField()
    fc = forms.FloatField()
    agc = forms.FloatField()
    psd = forms.ImageField()
    data = forms.FileField()
    time = forms.DateTimeField()
