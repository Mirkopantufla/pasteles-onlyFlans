from django.db import models
import uuid

# Create your models here.
class Flan(models.Model):
    flan_uuid = models.UUIDField()
    name = models.CharField(max_length=64)
    description = models.TextField()
    preparation = models.TextField()
    ingredients = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField()
    is_private = models.BooleanField()

    #Permite que al mostrarse la informacion en el panel de administrador, apareza el nombre directamente y no 'object'
    def __str__(self) -> str:
        return f'{self.name}'

    
class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False) #No se podra modificar de ninguna manera
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()

    def __str__(self):
        return f"{self.customer_email} - Mensaje: {self.message}"