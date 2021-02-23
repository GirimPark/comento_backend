from django.conf import settings
from django.db import models
from django.utils import timezone


class Profile(models.Model):
    user_name = models.CharField(max_length=30, default="익명")
    status_message = models.CharField(max_length=30, default="")
    photo = models.URLField()
    background = models.URLField()
    text_image = models.URLField()
    sticker_image = models.URLField()
    sound_image = models.URLField()
    calendar_image = models.URLField()

    def __str__(self):
        return self.name

class PhotoInfo(models.Model):
    # profile_id = Forigen key
    # photo_url = models.ImageField() # option 찾아보시고 추가하면 좋을 것 같습니다.
    # created_at = models.DataTimeField()
    # is_deleted = models.BooleanField(dafault=False)
