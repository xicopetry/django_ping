from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from datetime import datetime

from home.models import Host


def index(request):
    context = {}
    context['hosts_list'] = Host.objects.all()
    return render(request, 'home/index.html', context)


def update_ping(request):
    pk = request.GET.get("pk", None)
    host = get_object_or_404(Host, pk=pk)
    host.call_ping()
    response = {
        'name': host.name,
        'ip_address': host.ip_address,
        'status': host.status,
        'rtt_avg': host.rtt_avg_ms,
        'packets_lost': host.packets_lost,
        'date': host.formated_date,
    }
    return JsonResponse(response, status=200)