from models import available_image_types
from django import forms
from formfield import FormField
from django.forms.models import modelform_factory
from django.utils.translation import ugettext_lazy as _

IMAGE_TYPE_CHOICES = (('initial',_(u'Choisissez un type d\'image...')),) + tuple((image_type, available_image_types[image_type].user_friendly_type) for image_type in available_image_types)

def make_image_form():
    class HOP(forms.Form):
        type = forms.ChoiceField(choices=IMAGE_TYPE_CHOICES,initial='referenced',label='a')
        referenced = FormField(modelform_factory(available_image_types['referenced']),required=False,label='b')
        stored = FormField(modelform_factory(available_image_types['stored']),required=False,label='c')
        class Media:
            js = ('form2js.js','imaging/imageform.js?',)
#    for image_type,image_model in available_image_types.iteritems():
#        setattr(HOP,image_type,FormField(modelform_factory(image_model),required=False,label=''))
    return HOP

ImageForm = make_image_form()