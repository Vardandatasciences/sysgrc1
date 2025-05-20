from django.core.management.base import BaseCommand
import time
import MySQLdb

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        self.stdout.write("Waiting for DB...")
        while True:
            try:
                conn = MySQLdb.connect(
                    host="db", user="root", passwd="root", db="vardaan"
                )
                break
            except Exception:
                self.stdout.write("DB not ready, waiting...")
                time.sleep(2)
        self.stdout.write(self.style.SUCCESS("DB ready!"))
