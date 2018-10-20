from django.contrib import admin
from .models import Category,Post
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('title','author','published','post_categories') # como queremos mostrar las categorias que son una relacion de muchos a muchos no importa si lo ponemos como categories, o categories__name dara error, así que creamos un metodo
    ordering = ('author','published')# ordenadas alfabeticamente por el autor, y luego por fecha de publicacion, como es una tupla toca dejar el segundo como ('author',) si no se va a usar segundo
    search_fields = ('title','content','author__username','categories__name')#buscador por titulo o contenido o 
    date_hierarchy = 'published' # para agregar un paginador de fechas en el admin
    list_filter = ('author__username','categories') # si ponemos categories__name sirve pero en el filtro dira por nombre, así que para que diga filtro por categorias al ser una relacion se puede dejar así y el detectara el atributo

    def post_categories(self, obj):# ejecutar algo para cada objeto, cada fila
        return ", ".join([c.name for c in obj.categories.all().order_by("name")]) # si queremos retornar un html en el curso video 41 hay un enlace donde se enseña
    post_categories.short_description = "Categorias"
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)