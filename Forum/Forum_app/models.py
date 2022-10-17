from django.db import models

class User(models.Model):
    __tablename__ = 'User'
    id = models.AutoField(primary_key=True)
    login = models.CharField('Login',unique=True,max_length=35)
    password = models.CharField('password',max_length=255)
    create_date = models.DateTimeField('Дата создания акаунта',auto_now_add=True)


class Post(models.Model):
    __tablename__ = 'Post'
    id = models.AutoField(primary_key=True)
    user_login = models.ForeignKey('Forum_app.User', on_delete=models.CASCADE)
    title = models.CharField('Заголовок',max_length=70)
    descriphons = models.CharField('Описание',max_length=2000)
    create_date = models.DateTimeField('Дата создания акаунта',auto_now_add=True)
    post_url = models.URLField(max_length=255)
