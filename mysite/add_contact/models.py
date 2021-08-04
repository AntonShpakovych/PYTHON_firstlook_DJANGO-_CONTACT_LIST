from django.db import models


class Contact(models.Model):
    name = models.CharField('name', max_length=50)
    sur_name = models.CharField('surname', max_length=50)
    email = models.EmailField('email')
    phone = models.IntegerField('phone')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Contacts'
        verbose_name_plural = 'Contacts'
