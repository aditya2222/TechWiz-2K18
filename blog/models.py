from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=256)

    def __str__(self):
        return  self.title


class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def get_absolute_url(self):
            return reverse("post_detail",kwargs={'pk':self.pk})

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post',related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment=True
        self.save()

    def get_absolute_url(self):
        return reverse("post_list")

    def __str__(self):
        return self.text


class Rule(models.Model):
    author = models.ForeignKey('blog.Event',on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def get_absolute_url(self):
            return reverse("rule_detail",kwargs={'pk':self.pk})

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return self.title


class Registration(models.Model):
    event = models.ForeignKey('blog.Event',on_delete=models.CASCADE,)
    firstName = models.CharField(max_length=256,)
    secondName = models.CharField(max_length=256)
    paynow=models.BooleanField(default=False)
    rollNumber=models.IntegerField()

    def get_absolute_url(self):
        if self.paynow==True:
            return reverse('pay-now')
        else:
            return reverse('about')

    def __str__(self):
        return self.firstName