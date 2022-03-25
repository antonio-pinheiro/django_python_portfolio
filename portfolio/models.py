from django.db import models

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=320)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)
    #date = models.DateField(null=True)

    def __str__(self):
        return self.title
