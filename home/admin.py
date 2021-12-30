from django.contrib import admin

from home.models import HostType, Host


@admin.register(Host)
class HostAdmin(admin.ModelAdmin):

    list_display = ('name', 'ip_address', 'status', 'date', 'rtt_avg_ms', 'packets_lost', 'host_type')


@admin.register(HostType)
class HostTypeAdmin(admin.ModelAdmin):

    list_display = ('name', )