from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre")
    email = models.EmailField(blank=True, verbose_name="Email de contacto")
    phone = models.CharField(max_length=50, blank=True, verbose_name="Teléfono")
    address = models.TextField(blank=True, verbose_name="Dirección")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado el")

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"
        ordering = ['name']

    def __str__(self):
        return self.name


class Person(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Nombre")
    last_name = models.CharField(max_length=100, verbose_name="Apellido")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=50, blank=True, verbose_name="Teléfono")
    position = models.CharField(max_length=100, blank=True, verbose_name="Cargo")
    company = models.ForeignKey(
        Company,
        on_delete=models.PROTECT,
        related_name='people',
        verbose_name="Empresa"
    )
    hire_date = models.DateField(null=True, blank=True, verbose_name="Fecha de ingreso")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado el")

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"