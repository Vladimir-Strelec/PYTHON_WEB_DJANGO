from django.contrib import admin

from parallax.web.models import AbstractProduct


@admin.register(AbstractProduct)
class AbstractProductAdmin(admin.ModelAdmin):
    pass
