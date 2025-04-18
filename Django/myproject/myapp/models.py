from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    image_data = models.BinaryField(default=None)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title