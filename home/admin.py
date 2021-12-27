from django.contrib import admin

from home.models import Host


@admin.register(Host)
class HostAdmin(admin.ModelAdmin):

    list_display = ('name', 'ip_address', 'status', 'date', 'rtt_avg_ms', 'packets_lost')