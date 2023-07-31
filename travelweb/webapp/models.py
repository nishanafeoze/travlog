from django.db import models

class place(models.Model):
    name = models.CharField(max_length=256)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    def __str__(self):
        return self.name
class TeamMember(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='pics')
    bio = models.TextField()


    def __str__(self):
        return self.name

# Create your models here.
