from django.db import models

# Create your models here.


class Service(models.Model):
    title = models.CharField('Titulo', max_length=100, blank=False)
    description = models.CharField('Descripcion', max_length=100, blank=False)
    content = models.TextField('Contenido')
    image = models.ImageField(upload_to='static/images/services/', blank=True)
    is_active = models.BooleanField('Activo', blank=False, default=True)

    def __str__(self):
        return self.title
