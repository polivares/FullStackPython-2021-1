from django.db import models

# Create your models here.


class Usuario(models.Model):
    email = models.EmailField()
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    user_level = models.IntegerField()

class Mensaje(models.Model):
    usuario_origen = models.ForeignKey(Usuario, 
                                       related_name="mensajes_enviados", 
                                       on_delete = models.CASCADE )
    usuario_destino = models.ForeignKey(Usuario,
                                        related_name = "mensajes_recibidos",
                                        on_delete= models.CASCADE)
    mensaje = models.TextField(blank=True)

class Comentario(models.Model):
    mensaje = models.ForeignKey(Mensaje,
                                related_name="comentarios",
                                on_delete=models.CASCADE)
                                           