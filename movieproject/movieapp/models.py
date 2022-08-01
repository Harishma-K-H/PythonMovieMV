from django.db import models
class movies(models.Model):
    name=models.CharField(max_length=220)
    des=models.TextField()
    year=models.IntegerField(blank=True)
    img=models.ImageField(upload_to="gallery")
# Create your models here.
    def __str__(self):
        return self.name