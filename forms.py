from django import forms

from .apps import AuctorConfig as conf

class ThumbAndBannerForm(forms.ModelForm):
    thumbnail_img = forms.FileField(required=False)
    banner_img = forms.FileField(required=False)

    def clean(self):
        cleaned_data = super(ThumbAndBannerForm, self).clean()
        if hasattr(cleaned_data['thumbnail_img'], 'read'):
            cleaned_data['thumbnail_img'] = cleaned_data['thumbnail_img'].read()
        if hasattr(cleaned_data['banner_img'], 'read'):
            cleaned_data['banner_img'] = cleaned_data['banner_img'].read()
        return cleaned_data

    def save(self, commit=True):
        instance = super(ThumbAndBannerForm, self).save(commit=False)
        instance.thumbnail = self.cleaned_data['thumbnail_img']
        instance.banner = self.cleaned_data['banner_img']
        if commit:
            instance.save()
        return instance