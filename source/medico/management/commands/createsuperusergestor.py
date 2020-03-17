from django.contrib.auth.management.commands import createsuperuser
from django.core.management.base import BaseCommand
from django.core.management import CommandError
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Crate a superuser, and allow password to be provided'

  
    def handle(self, *args, **options):
        UserModel = get_user_model()
        password = '1@345678'
        username = 'gestor'
        email = 'teste@test.com'
        database = options.get('database')

        user, criado = UserModel.objects.get_or_create(username=username, email=email)
        if criado :
            user.set_password(password)
            user.save()