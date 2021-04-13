from django.contrib import admin
from .models import Order, Commission, Reference
admin.site.register([Order, Commission, Reference])
# Register your models here.


# from api.models import Order, Commission, Reference