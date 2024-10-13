from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.core.exceptions import FieldError

class Command(BaseCommand):
    help = 'List all active superusers and their hashed passwords'

    def handle(self, *args, **kwargs):
        User = get_user_model()  # This refers to 'core.User' in your case.
        try:
            # Filter superusers who are staff and active
            superusers = User.objects.filter(is_staff=True, is_superuser=True, is_active=True)
            for user in superusers:
                # Print the username and the hashed password
                self.stdout.write(f'Username: {user.email}, Email: {user.email}, Password (hashed): {user.password}')
        except FieldError as e:
            self.stdout.write(self.style.ERROR(f'FieldError: {e}'))
