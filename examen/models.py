# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Proyecto(models.Model):
    id = models.AutoField(primary_key=True)  # This field type is a guess.
    nombre = models.TextField(null=False)
    descripcion = models.TextField(null=False)
    url = models.TextField(db_column='URL', null=False)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'proyecto'
