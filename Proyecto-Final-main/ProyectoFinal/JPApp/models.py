from django.db import models

# Create your models here.

class investigations(models.Model):

    def __str__(self):
        return f'{self.investigation_owner} creó {self.investigation_name}'

    domain_name = models.CharField('Nombre del dominio', max_length=40)
    investigation_owner = models.CharField('Creador',max_length=40)
    investigation_name = models.CharField('Nombre de la investigación', max_length=40)
    investigation_date = models.DateField('Fecha de investigación')
    investigation_overview = models.CharField('Resumen de la investigación', max_length= 500)
    investigation_media = models.FileField('Archivo de la investigación', upload_to = "Investigaciones")
    investigation_link = models.URLField('Link de la investigación', null = True, blank = True)

class bugs(models.Model):

    def __str__(self):
        return f'{self.bugs_date} {self.bugs_owner} creó {self.bugs_name}'

    bugs_domain = models.CharField('Nombre del Dominio', max_length= 20)
    bugs_date = models.DateField('Fecha')
    bugs_owner = models.CharField('Nombre del colaborador', max_length= 40)
    bugs_name = models.CharField('Nombre o codigo del error', max_length=40)
    bugs_description = models.CharField('Descripción del error', max_length= 500)
    bugs_blocking = models.BooleanField('¿El error es bloqueante?', default=False)
    bugs_media = models.FileField('Video del error', upload_to = "Videos o archivos errores", null = True, blank = True)
    bugs_image = models.ImageField('Imagen del error', upload_to = "Errores", null = True, blank = True)

class tips(models.Model):

    def __str__(self):
        return f'{self.tips_owner} creó {self.tips_name}'

    tips_owner = models.CharField('Creador del refuerzo', max_length= 40)
    tips_name = models.CharField('Nombre del refuerzo', max_length= 250)
    tips_description = models.CharField('Descripción del refuerzo', max_length= 500)
    tips_date = models.DateField('Fecha')
    tips_email = models.EmailField('Email')
    tips_media = models.FileField('Archivo del Refuerzo', upload_to = "Refuerzos", null = True, blank = True)
    tips_link = models.URLField('Link del Refuerzo', null = True, blank = True)