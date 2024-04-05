from django.db import models

# Create your models here.


class Company(models.Model):
    commercial_name = models.CharField("Nombre Empresa", max_length=100, blank=False)
    legal_name = models.CharField("Nombre Legal", max_length=100, blank=False)
    email = models.EmailField("Correo Electrónico", max_length=70, blank=False)
    phone = models.CharField("Teléfono Fijo", max_length=10, blank=False)
    mobile_phone = models.CharField("Teléfono Movil", max_length=10, blank=True)
    web_site = models.CharField("Página Web", max_length=100, blank=True)
    address = models.CharField("Dirección", max_length=50, blank=True)
    country = models.CharField("País", max_length=50, blank=False)
    location = models.CharField("Localidad", max_length=50, blank=False)
    taxes = models.DecimalField("Impuesto", decimal_places=2, max_digits=5, blank=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.commercial_name

    def save(self, *args, **kwargs):
        self.commercial_name = self.commercial_name.title()
        self.legal_name = self.legal_name.title()
        self.email = self.email.lower()
        self.web_site = self.web_site.lower()
        super(Company, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"


class Contact(models.Model):
    name = models.CharField("Nombre", max_length=100, blank=False)
    email = models.EmailField("Email", blank=False, max_length=50)
    phone = models.CharField("Telefono", blank=True, max_length=9)
    message = models.TextField("Mensaje", blank=False)
    term = models.BooleanField("Terminos y Condiciones", blank=False)

    def __str__(self):
        return self.name
