from django.contrib import admin
from .models import (
    Car,
    Owner,
)

# Register your models here.
admin.site.register(Car)
admin.site.register(Owner)
