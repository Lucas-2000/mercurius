from django.contrib import admin

from pages.models import Employer, Neighborhood, Transaction

# Register your models here.
admin.site.register(Neighborhood)
admin.site.register(Employer)
admin.site.register(Transaction)
