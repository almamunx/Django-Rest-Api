from django.db import models

# Create your models here.

class Post(models.Model):

    STATUS = (
        ('draft', 'draft'),
        ('published', 'published'),)

    title = models.CharField(max_length=80, unique=True, db_index=True)
    body = models.TextField(default = "draft")
    status = models.CharField(max_length=10, null=False, choices=STATUS)
    publish_date = models.DateField(
        auto_now_add=True)  # auto_now_add will set the timezone.now() only when the instance is created
    update_date = models.DateField(auto_now=True,
                                   null=False)  # auto_now will update the field everytime the save method is called

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['publish_date']

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("post_details", kwargs={"slug": self.title})
