from datetime import datetime
from django.db import models
from pythonping import ping


COUNT = 2


class Host(models.Model):
    name = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField()
    status = models.BooleanField(null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    rtt_avg_ms = models.FloatField(null=True, blank=True)
    packets_lost = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.name} - {self.ip_address}'
    
    def call_ping(self):
        print(f'------Calling PING for {self.ip_address}-{self.name}')
        self.date = datetime.now()
        result = ping(self.ip_address, count=COUNT, match=True)
        self.status = result.success(option=2)
        self.rtt_avg_ms = result.rtt_avg_ms
        self.packets_lost = int(result.packets_lost * COUNT)
        self.save()

    @property
    def formated_date(self):
        return self.date.strftime('%b %d %Y %H:%M:%S')