from datetime import datetime
from django.db import models
from pythonping import ping


COUNT = 2


class HostType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Host(models.Model):
    name            = models.CharField(max_length=100)
    ip_address      = models.GenericIPAddressField()
    status          = models.BooleanField(null=True, blank=True)
    date            = models.DateTimeField(null=True, blank=True)
    last_date_alive = models.DateTimeField(null=True, blank=True)
    rtt_avg_ms      = models.FloatField(null=True, blank=True)
    packets_lost    = models.IntegerField(null=True, blank=True)
    host_type       = models.ForeignKey(HostType, null=True, on_delete=models.SET_NULL, help_text='The host type can be a Desktop, Antenna, Router, AP, Switch...')
    acknowledged    = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} - {self.ip_address}'
    
    def call_ping(self):
        print(f'------Calling PING for {self.ip_address}-{self.name}')
        self.date = datetime.now()
        result = ping(self.ip_address, count=COUNT, match=True)
        self.status = result.success(option=2)
        self.rtt_avg_ms = result.rtt_avg_ms
        self.packets_lost = int(result.packets_lost * COUNT)
        
        if self.status:
            self.last_date_alive = self.date
        
        self.save()

    @property
    def formated_date(self):
        if self.date:
            return self.date.strftime('%d/%m/%Y %H:%M:%S')
    
    @property
    def formated_last_date_alive(self):
        if self.last_date_alive:
            return self.last_date_alive.strftime('%d/%m/%Y %H:%M:%S')