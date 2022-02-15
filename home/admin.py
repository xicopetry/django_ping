from django.contrib import admin

from home.models import HostType, Host

from import_export import resources
from import_export.admin import ImportExportModelAdmin


class HostResource(resources.ModelResource):

    class Meta:
        model = Host
        fields = ('name', 'ip_address', 'status', 'date', 'last_date_alive', 'host_type__name', 'rtt_avg_ms')


@admin.register(Host)
class HostAdmin(ImportExportModelAdmin):

    list_display = ('name', 'ip_address', 'status', 'date', 'host_type', 'rtt_avg_ms')
    list_filter = ('host_type', 'status')
    resource_class = HostResource


@admin.register(HostType)
class HostTypeAdmin(admin.ModelAdmin):

    list_display = ('name', )