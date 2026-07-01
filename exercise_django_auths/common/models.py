from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    is_published = models.BooleanField(default=False)

    class Meta:
        permissions = [
            ('can_edit_article', 'Can make corrections inside the article'),
            ('can_delete_article', 'Can delete article')
        ]