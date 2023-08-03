from django.db import models


class Image(models.Model):
    img = models.ImageField(upload_to="static/media", blank=True,null=True)

    def __str__(self):
        return f"img: {self.img}"

