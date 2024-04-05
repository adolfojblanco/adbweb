from django.db import models
from django.utils.text import slugify

# Create your models here.


class Service(models.Model):
    title = models.CharField("Titulo", max_length=100, blank=False)
    slug = models.SlugField(max_length=150, blank=True)
    description = models.CharField("Descripcion", max_length=100, blank=False)
    content = models.TextField("Contenido")
    image = models.ImageField(upload_to="static/images/services/", blank=True)
    is_active = models.BooleanField("Activo", blank=False, default=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Service, self).save(*args, **kwargs)
    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
