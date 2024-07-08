from django.contrib import admin
from django.urls import path
from django.conf import settings


from miapp import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = "index"),
    path('inicio/', views.index, name = "inicio"),
    path('saludo/',views.saludo, name = "saludo"),
    path('rango/',views.rango,name="rango"),
    path('rango2/',views.rango2,name="rango2"),
path('rango2/<int:a>',views.rango2,name="rango2"),
path('rango2/<int:a>/<int:b>',views.rango2,name="rango2"),
path('crear-articulo/<str:titulo>/<str:contenido>/<str:publicado>',views.crear_articulo,name="crear_articulo"),
    
path('buscar-articulo', views.buscar_articulo, name="buscar_articulo"),
path('editar-articulo/<int:id>',views.editar_articulo,name="editar_articulo"),
path('listar-articulos/',views.listar_articulos,name="listar_articulos"),
path('eliminar-articulo/<int:id>',views.eliminar_articulo, name='eliminar_articulo')
path('save-articulo/',views.save_articulo, name='save_articulo'),
path('create-articulo/',views.create_articulo, name='create_articulo'),
path('create-full-articulo/',views.create_full_articulo, name='create_full_articulo'),
    path('create-full-articulo/',views.create_full_articulo, name="create_full_articulo"),
]


# Configuración para cargar imágenes
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
