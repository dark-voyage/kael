from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):

    status_choices = (
        (0, "Draft"),
        (1, "Publish")
    )

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    status = models.IntegerField(choices=status_choices, default=0)
    content = models.TextField()

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title
