# -*- coding: utf-8 -*-
from django.db import models
from model_utils.managers import InheritanceManager
from django.utils.translation import ugettext as _
from django.conf import settings
from urlparse import urlsplit

# A model of an image, which can be either externally linked or locally saved.
class Image(models.Model):
    # associated image caption
    caption = models.CharField(max_length=200,default='',blank=True)
    # inheritance manager
    objects = InheritanceManager()

class StoredImage(Image):
    user_friendly_type = _(u'Télécharger une image')
    image = models.ImageField(upload_to='imaging/', default='default_avatar.jpg')
    @property
    def url(self):
        return self.image.url
    @url.setter
    def url(self,value):
        self.image.url = value
    def get_thumbnail_url(self):
        return  '/imaging/thumbnail/medium/' + settings.SERVER_URL + self.image.url

class ReferencedImage(Image):
    user_friendly_type = _(u'Lien vers une image externe')
    url = models.URLField()
    thumburl = models.URLField(blank=True,default='')
    def get_thumbnail_url(self):
        if self.thumburl:
            return settings.MEDIA_URL + self.thumburl
        else:
            pr=urlsplit(self.url)
            return '/imaging/thumbnail/medium/' + pr.netloc + pr.path

available_image_types = {
                         'stored': StoredImage, 
                         'referenced': ReferencedImage, 
                         } 