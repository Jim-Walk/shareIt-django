from django import forms
from shareIt.models import Image

class ImageForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter an image name")
    image = forms.ImageField()
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Image
        fields = ('name', 'image')