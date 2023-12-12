from django import forms

class AddFasilitasForm(forms.Form):
    nama_fasilitas = forms.CharField(widget = forms.Textarea)