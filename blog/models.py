from email import message
from sqlite3 import Timestamp
from django.db import models

class Blog(models.Model):

    title = models.CharField(max_length = 200)
    description = models.TextField()


    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name="blog_comment", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.blog.title + "  " + self.message


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name