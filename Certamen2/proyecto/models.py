from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Clientes(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50)
    email=models.EmailField(blank=True, null=True)
    tfno=models.CharField(max_length=7)

class Articulos(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)
    precio=models.IntegerField()

    def __str__(self):
        return 'El nombre es %s la seccion es %s y el precio es %s' % (self.nombre, self.seccion, self.precio)

class Pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()

class Categoria(models.Model):
    nombre = models.TextField()
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Comunicado(models.Model):


    NIVEL_CHOICES=[
        ("GEN", "General"),
        ("PRE", "Ciclo Preescolar"),
        ("BAS", "Ciclo Básico"),
        ("MED", "Ciclo Medio"),
    ]

    correlativo = models.AutoField(primary_key=True)
    titulo = models.TextField()
    detalle = models.TextField()
    nivel = models.CharField(max_length=3, choices=NIVEL_CHOICES)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_envio = models.DateTimeField(auto_now_add=True)
    fecha_ultima_modificacion = models.DateTimeField(auto_now=True)
    publicado_por = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.titulo

