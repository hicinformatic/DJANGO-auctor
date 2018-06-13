from django import forms

from .apps import AuctorConfig as conf
from simplify.apps import SimplifyConfig as spf

import mimetypes

class ThumbAndBannerFormBase(forms.ModelForm):
    def save(self, commit=True):
        instance = super(ThumbAndBannerFormBase, self).save(commit=False)
        instance.thumbnail = self.cleaned_data['thumbnail_img']
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
        thumbnail_img = forms.FileField(widget=forms.ClearableFileInput(), required=False)
        banner_img = forms.FileField(widget=forms.ClearableFileInput(), required=False)

        def clean(self):
            cleaned_data = super(ThumbAndBannerForm, self).clean()
            if self.check_contenttype('thumbnail', cleaned_data['thumbnail_img']) and self.check_size('thumbnail', cleaned_data['thumbnail_img']):
                cleaned_data['thumbnail_img'] = cleaned_data['thumbnail_img'].read()
            if self.check_contenttype('banner', cleaned_data['banner_img']) and self.check_size('banner', cleaned_data['banner_img']):
                cleaned_data['banner_img'] = cleaned_data['banner_img'].read()
            return cleaned_data

        def check_contenttype(self, typeimg, image):
            return True
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



        