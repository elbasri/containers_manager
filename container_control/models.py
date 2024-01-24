from django.db import models

class Container(models.Model):
    container_name = models.CharField(max_length=255, unique=True)
    update_status = models.IntegerField()
    restart = models.BooleanField(default=False)
    modules =  models.TextField(default='')

    def __str__(self):
        return self.container_name

    def get_modules_list(self):
        # Convert the string back to a list
        if self.modules:
            return self.modules.split(',')
        return []
