from django.contrib import admin

from home.models import HostType, Host


@admin.register(Host)
class HostAdmin(admin.ModelAdmin):

    list_display = ('name', 'ip_address', 'status', 'date', 'host_type', 'rtt_avg_ms')
    list_filter = ('host_type', 'status')


@admin.register(HostType)
class HostTypeAdmin(admin.ModelAdmin):

    list_display = ('name', )