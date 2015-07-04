from rest_framework import serializers
from models import available_image_types

IMAGE_TYPE_CHOICES = ((image_type, available_image_types[image_type].user_friendly_type) for image_type in available_image_types)

def make_image_serializer(image_type):
    class HOP(serializers.ModelSerializer):
        class Meta:
            model = available_image_types[image_type]
        
class ImageSerializer(serializers.Serializer):
    type = serializers.ChoiceField(choices=IMAGE_TYPE_CHOICES)
    def validate(self, attrs):
        if not attrs['type'] in attrs:
            raise serializers.ValidationError("Data not provided for chosen image type")
        return attrs
    def restore_object(self,attrs,instance=None):
        return getattr(self,attrs['type']).restore_object(attrs['referenced'],instance=instance)

for image_type,image_model in available_image_types.iteritems():
    setattr(ImageSerializer,image_type,make_image_serializer(image_type)(required=False))
