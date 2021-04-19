from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=512, null=True, blank=True)
    price = models.PositiveIntegerField(default=0)
    category = models.ManyToManyField("Category", related_name="category")
    image = models.ForeignKey("Image", null=True, blank=True, related_name="product_image", on_delete = models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=128, null=True, blank=True)
    image = models.ManyToManyField("Image", related_name="category_image")


class Image(models.Model):

    def where_to_upload(instance, filename):
        return f"Images/{instance.name}" 

    name = models.CharField(max_length=128, null=True, blank=True)
    file = models.ImageField(upload_to=where_to_upload, blank=True, null=True)

    def __str__(self):
        return self.file.url
