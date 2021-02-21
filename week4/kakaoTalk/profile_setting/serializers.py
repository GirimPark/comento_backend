from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ['user_name', 'status_message', 'photo', 'background',
                  'text_image', 'sticker_image', 'sound_image', 'calendar_image']
