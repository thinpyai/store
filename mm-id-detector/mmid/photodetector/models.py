from django.db import models

class IdCard(models.Model):
    poi = models.CharField(max_length=50)
    card_img = models.ImageField(upload_to='id-images/')

    def __str__(self):
        return self.poi
