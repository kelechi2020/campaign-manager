from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from buharisupport.models import Members, State, LocalGovernment, Ward, PoolingUnit

admin.site.site_header = 'Buhari Support Organization Data Management system'
admin.site.site_title = "Buhari Support Organization Data Management system"



@admin.register(Members)
class ApplicantAdmin(ImportExportModelAdmin):
    pass


@admin.register(LocalGovernment)
class ApplicantAdmin(ImportExportModelAdmin):
    pass


@admin.register(State)
class ApplicantAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Ward)
admin.site.register(PoolingUnit)

