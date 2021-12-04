from django.contrib import admin
from .models import registro
# Register your models here.
"""
usuario:nahomi
pass: S3gu0P41e459
"""


class regis(admin.ModelAdmin):
    list_display = ('matricula','equipo','comentario','ipequipo','salon')
    pass

admin.site.register(registro,regis)