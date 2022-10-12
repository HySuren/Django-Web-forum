from django.db import models

class User(models.Model):
    __tablename__ = 'User'
    id = models.IntegerField('id', primary_key=True,null=False,unique=True)
    login = models.CharField('Login',unique=True,max_length=35)
    password = models.CharField('password',max_length=255)
    create_date = models.DateTimeField('Дата создания акаунта')
