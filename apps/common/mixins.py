import os


class AutoAssignMixin:
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = os.urandom(16).hex()
        super().save(*args, **kwargs)