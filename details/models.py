from django.contrib.gis.db import models
from cloudinary.models import CloudinaryField
from django.db.models.signals import pre_delete
import cloudinary
import cloudinary.uploader
from django.dispatch import receiver
from user.models import UserModel
from django.utils.translation import ugettext_lazy as _


class DetailModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    title = models.CharField(_("title"), max_length=64)
    description = models.TextField(_("description"))
    classification = models.CharField(_('classification'), max_length=30)
    image = CloudinaryField(_('image'))
    point = models.PointField(null=True, blank=True)
    date = models.DateTimeField()
    author = models.CharField(_("author"), max_length=30, null=False, blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("detail")
        verbose_name_plural = _("details")


@receiver(pre_delete, sender=DetailModel)
def photo_delete(sender, instance, **kwargs):
    cloudinary.uploader.destroy(instance.image.public_id)


# @receiver(pre_save, sender=DetailModel)
# def add_watermark(sender, instance, **kwargs):
#     image = CloudinaryResource(instance.image)
#     cloudinary.CloudinaryImage(image).image(overlay="static/images/200-star.jpg",  width=100)
