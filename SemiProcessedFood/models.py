from django.db import models
from django.utils.html import format_html

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='类别')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=100, verbose_name='菜名')
    image_location = models.ImageField(verbose_name='图片', upload_to='images/%Y/%m/%d', blank=True)
    description = models.TextField(verbose_name='描述')
    active = models.BooleanField(default=True)
    category = models.ForeignKey('Category', verbose_name='类别', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    def image(self):
        if self.image_location:
            return format_html(
                '<img src="/media/{}" width="156px" height="98px"/>',
                self.image_location,
            )
        else:
            return format_html(
                '<img src="/media/images/no_image.png" width="156px" height="98px"/>',
            )
    image.short_description = '图片'