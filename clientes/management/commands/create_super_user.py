from django.contrib.auth.management.commands import createsuperuser
from django.core.management import CommandError

class Command(createsuperuser.Command):
    help = 'Create a superuser with email as the unique identifier.'

    def handle(self, *args, **options):
        email = options.get('email')
        username = options.get('username')

        if not email and not username:
            raise CommandError("You must provide either an email or a username.")

        if email:
            options['username'] = email

        return super().handle(*args, **options)
