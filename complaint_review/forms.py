from django import forms

class ComplaintForm(forms.Form):
    nama_hotel = forms.CharField(label = "Nama Hotel")
    cabang_hotel = forms.CharField(label = "Cabang Hotel")
    description = forms.CharField(widget=forms.Textarea,)


class ReviewForm(forms.Form):
    rating = forms.IntegerField(widget=forms.NumberInput(attrs={'id': 'rating_field'}))
    review = forms.CharField(widget=forms.Textarea(attrs={'id' : 'review_field'}))