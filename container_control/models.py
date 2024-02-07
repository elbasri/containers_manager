from django.db import models

class Container(models.Model):
    container_name = models.CharField(max_length=255, unique=True)
    update_status = models.IntegerField()
    restart = models.BooleanField(default=False)
    modules = models.ManyToManyField('ModulesList', blank=True)  # Use quotes around ModulesList

    def __str__(self):
        return self.container_name

    def get_modules_list(self):
        # Get the list of module names
        return list(self.modules.all().values_list('module_name', flat=True))


class ModulesList(models.Model):
    module_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.module_name
