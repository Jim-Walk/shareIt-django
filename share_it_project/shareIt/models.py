from django.db import models
from django.template.defaultfilters import slugify

class Image(models.Model):
    name = models.CharField(max_length=128, unique=True)
    image = models.ImageField(upload_to="user_images")
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Image, self).save(*args, **kwargs)

    def __unicode__(self):
       return self.name

