from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


# Create your models here.

class Category(models.Model):
    name = models.CharField('Categoria', max_length=30)
    slug = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = "Categorias"


class Post(models.Model):
    title = models.CharField('Titulo', max_length=255)
    content = RichTextField('Contenido', blank=True)
    slug = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
