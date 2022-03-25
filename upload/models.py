import uuid
from django.db import models


class UploadModel(models.Model):

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return '%s' % self.image

    def get_image(self):
        if self.image:
            return self.image.url
        return ''
