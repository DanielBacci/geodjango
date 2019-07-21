from django.contrib import admin

from pdv.partners.models import Partner


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    pass
