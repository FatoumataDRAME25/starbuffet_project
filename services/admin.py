from django.contrib import admin

# Register your models here.

from services.models import Traiteur
#admin.site.register(Traiteur)

@admin.register(Traiteur)
class TraiteurAdmin(admin.ModelAdmin):
    list_display = (
        "fullname",
        "speciality",
        "phone",
        "adress"
        
    )