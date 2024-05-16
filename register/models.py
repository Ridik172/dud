from django.db import models

from django.db import models

from django.db import models

class Users(models.Model):
    iduser = models.AutoField(primary_key=True)
    Phone = models.CharField(max_length=11, unique=True)
    Password = models.CharField(max_length=20)
    birthdate = models.DateField()
    Firstname = models.CharField(max_length=15)
    Lastname = models.CharField(max_length=15)
    Middlename = models.CharField(max_length=15, blank=True, null=True)
    Email = models.EmailField(unique=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(Phone__isnull=False) & ~models.Q(Phone=''),
                name='check_phone'
            ),
            models.CheckConstraint(
                check=models.Q(birthdate__isnull=False) & (models.Q(birthdate__lte='2008-01-01') | models.Q(birthdate__gte='2008-01-01')),
                name='check_birthdate'
            )
        ]

class CategoriesTypes(models.Model):
    idcategories_types = models.AutoField(primary_key=True)
    description = models.CharField(max_length=33)

class ServiceTypes(models.Model):
    idservice_types = models.AutoField(primary_key=True)
    idcategories_types = models.ForeignKey(CategoriesTypes, on_delete=models.CASCADE)
    description = models.CharField(max_length=33)

class Tag(models.Model):
    idtag = models.AutoField(primary_key=True)
    description = models.CharField(max_length=33, default='Для:')

class IdCategoriesTypesIdTag(models.Model):
    idcategories = models.ForeignKey(CategoriesTypes, on_delete=models.CASCADE)
    idtag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['idcategories', 'idtag'], name='unique_idcategories_idtag')
        ]

class Ads(models.Model):
    idad = models.AutoField(primary_key=True)
    iduser = models.ForeignKey(Users, on_delete=models.CASCADE)
    idcategories_types = models.ForeignKey(CategoriesTypes, on_delete=models.CASCADE)
    Address = models.CharField(max_length=50)
    Description = models.CharField(max_length=99, default='Занимаюсь:')
    Telephone = models.CharField(max_length=11)

class Comment(models.Model):
    idcom = models.AutoField(primary_key=True)
    userid = models.ForeignKey(Users, on_delete=models.CASCADE)
    adid = models.ForeignKey(Ads, on_delete=models.CASCADE)
    Textcom = models.CharField(max_length=99, default='да, он хорош')