from django.shortcuts import render, get_object_or_404, redirect
from .models import Device
from .forms import DeviceForm
from django.urls import reverse

def home(request):
    return render(request, 'home.html')

def employee_network(request):
    active_tab = request.GET.get('tab', 'routers')

    if active_tab == 'switches':
        devices = Device.objects.filter(network='employee', device_type='switch')
        total_label = f'Total Switches: {devices.count()}'
    elif active_tab == 'end-devices':
        devices = Device.objects.filter(network='employee', device_type='end')
        total_label = f'Total End Devices: {devices.count()}'
    else:
        devices = Device.objects.filter(network='employee', device_type='router')
        total_label = f'Total Routers: {devices.count()}'
        active_tab = 'routers'

    return render(request, 'employee_network.html', {
        'devices': devices,
        'total_label': total_label,
        'active_tab': active_tab,
        'page_title': 'Employee Network',
    })

def management_network(request):
    active_tab = request.GET.get('tab', 'routers')

    if active_tab == 'switches':
        devices = Device.objects.filter(network='management', device_type='switch')
        total_label = f'Total Switches: {devices.count()}'
    elif active_tab == 'end-devices':
        devices = Device.objects.filter(network='management', device_type='end')
        total_label = f'Total End Devices: {devices.count()}'
    else:
        devices = Device.objects.filter(network='management', device_type='router')
        total_label = f'Total Routers: {devices.count()}'
        active_tab = 'routers'

    return render(request, 'management_network.html', {
        'devices': devices,
        'total_label': total_label,
        'active_tab': active_tab,
        'page_title': 'Management Network',
    })

def device_detail(request, pk):
    device = get_object_or_404(Device, pk=pk)

    next_url = request.POST.get('next') or request.GET.get('next') or reverse('home')

    if request.method == 'POST':
        form = DeviceForm(request.POST, instance=device)

        if form.is_valid():
            form.save()
            return redirect(next_url)

        else:
            print(form.errors)  # keep this while debugging

    else:
        form = DeviceForm(instance=device)

    return render(request, 'device_detail.html', {
        'device': device,
        'form': form,
        'next_url': next_url,
    })