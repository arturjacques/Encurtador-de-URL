from django.db import models
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

def post_user(nome,email,senha):
    user = User.objects.create_user(nome,email,senha)
    user.save()

def autenticacao(username,senha):
    user = authenticate(username=username, password=senha)
    return user