from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User ## contiene todos los usuarios registrados en el panel de administrador

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100,verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
        ordering = ['-created']

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=200,verbose_name="Titulo")
    content = models.TextField(verbose_name="contenido")
    published = models.DateTimeField(verbose_name="Fecha de publicación",default=timezone.now)
    image = models.ImageField(verbose_name="Imagen",upload_to="blog",blank=True, null=True)
    author = models.ForeignKey(User,verbose_name="Autor",on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category,verbose_name="Categorias",related_name="get_posts") # para no obtener los objetos category con la relacion many to many con category.post_set.all
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "entrada"
        verbose_name_plural = "entradas"
        ordering = ['-created']

    def __str__(self):
        return self.title
