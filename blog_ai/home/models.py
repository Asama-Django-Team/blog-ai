from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=100)
    abstract = models.CharField(max_length=500)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="blog_posts")
    reading_time = models.TimeField()

    def __str__(self):
        return self.title


    



