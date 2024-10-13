# core/management/commands/server_url.py
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Display the server URL and port'

    def handle(self, *args, **options):
        host = '127.0.0.1'  # Change to your host if different
        port = '8000'       # Default port for Django development server
        url = f"http://{host}:{port}/"

        self.stdout.write(self.style.SUCCESS(f"Your Django server is running at: {url}"))
