from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.contrib.auth import get_user_model

class NewsStory(models.Model):
    slug = models.SlugField(null=False, unique=True)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    content = models.TextField()
    image = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name = "stories",
    )

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('story', kwargs={'slug':self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

# class Comment(models.Model):
#     post = models.ForeignKey(NewsStory,on_delete=models.CASCADE,related_name='comments')
#     name = models.CharField(max_length=80)
#     email = models.EmailField()
#     body = models.TextField()
#     created_on = models.DateTimeField(auto_now_add=True)
#     active = models.BooleanField(default=False)

#     class Meta:
#         ordering = ['created_on']

#     def __str__(self):
#         return 'Comment {} by {}'.format(self.body, self.name)