from django import forms

from .apps import AuctorConfig as conf
from simplify.apps import SimplifyConfig as spf

import mimetypes

class ThumbAndBannerFormBase(forms.ModelForm):
    thumbnail_img = forms.FileField(required=False)
    thumbnail_mimetype = forms.CharField(required=False)
    banner_img = forms.FileField(required=False)
    banner_mimetype = forms.CharField(required=False)

    def clean(self):
        cleaned_data = super(ThumbAndBannerFormBase, self).clean()
        if self.check_contenttype('thumbnail', cleaned_data['thumbnail_img']) and self.check_size('thumbnail', cleaned_data['thumbnail_img']):
            cleaned_data['thumbnail_mimetype'] = cleaned_data['thumbnail_img'].content_type
            cleaned_data['thumbnail_img'] = cleaned_data['thumbnail_img'].read()
        if self.check_contenttype('banner', cleaned_data['banner_img']) and self.check_size('banner', cleaned_data['banner_img']):
            cleaned_data['banner_mimetype'] = cleaned_data['banner_img'].content_type
            cleaned_data['banner_img'] = cleaned_data['banner_img'].read()
        return cleaned_data

    def check_contenttype(self, typeimg, image):
        if image is not None:
            if image.content_type in getattr(conf.default, typeimg):
                if hasattr(image, 'read'):
                    return True
            else:
                self.add_error('%s_img' % typeimg, getattr(conf.error, 'mimetype_%s' % typeimg) % str(image.content_type))
        return False

    def check_size(self, typeimg, image):
        if image is not None:
            if image.size <= getattr(conf.default, '%s_size' % typeimg):
                return True
            else:
                self.add_error('%s_img' % typeimg, getattr(conf.error, 'size_%s' % typeimg) % (str(image.size), getattr(conf.default, '%s_size' % typeimg)))
        return False

    def save(self, commit=True):
        instance = super(ThumbAndBannerFormBase, self).save(commit=False)
        if self.cleaned_data['thumbnail_img'] is not None:
            instance.thumbnail = self.cleaned_data['thumbnail_img']
        if self.cleaned_data['banner_img'] is not None:
            instance.banner = self.cleaned_data['banner_img']
        if commit:
            instance.save()
        return instance

if conf.default.library_pil:
    class ThumbAndBannerForm(ThumbAndBannerFormBase):
        thumbnail_img = forms.ImageField(widget=forms.ClearableFileInput(), required=False)
        banner_img = forms.ImageField(widget=forms.ClearableFileInput(), required=False)
else:
    class ThumbAndBannerForm(ThumbAndBannerFormBase):
        pass        