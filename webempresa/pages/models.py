from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Page(models.Model):
    title = models.CharField(verbose_name="Titulo",max_length=200)
    content = RichTextField(verbose_name="Contenido")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    order = models.SmallIntegerField(verbose_name="Orden",default=0) # para tener un orden definido creamos el atributo en el modelo y en el Meta lo añadimos al array ordering

    class Meta:
        verbose_name = "página"
        verbose_name_plural = "páginas"
        ordering = ['order','title']

    def __str__(self):
        return self.title

# Recordar que siempre despues de cada cambio a los modelos debemos aplicar nuevamente las migraciones
    