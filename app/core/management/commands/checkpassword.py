from django.contrib.auth.hashers import check_password
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Check if the password is correct or not'

    def handle(self, *args, **options):
        hashed_password = 'pbkdf2_sha256$260000$Ut3uXN8EIfbbjJ4A4K060c$QW2qY1Poh5TdTpIjGLRuPOuDyNiONrzIbAXxpFyWPhM='
        password_to_check = 'example2000'  # The password you want to verify

        is_correct = check_password(password_to_check, hashed_password)

        if is_correct:
            self.stdout.write(self.style.SUCCESS("Password is correct!"))
        else:
            self.stdout.write(self.style.ERROR("Password is incorrect!"))
