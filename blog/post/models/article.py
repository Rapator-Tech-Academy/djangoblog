from django.db import models

class Article(models.Model):
    author = models.CharField(
        max_length = 30, 
        verbose_name="Author of the post"
    )
    title = models.CharField(
        max_length=240, 
        verbose_name="title of the article"
    )
    body = models.TextField(
        verbose_name="Body of the article"
    )
    featured_image = models.ImageField()
    timestamp = models.DateTimeField()
    category = models.ForeignKey(
        "post.Category",
        on_delete=models.SET_NULL,
        related_name="articles",
        null=True
    )
    tags = models.ManyToManyField(
        "post.Tag",
        related_name="articles",
        null=True
    )
    view_count = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Blog article"
        verbose_name_plural = "Blog articles"

    def __str__(self):
        return self.title