from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def employee_network(request):
    active_tab = request.GET.get('tab', 'routers')

    routers = [
        {
            'type': 'Router',
            'name': 'EMP-RTR-1',
            'status': 'Online',
            'ip_address': '192.168.7.192',
            'ssh': 'Enabled',
            'firewall': 'Enabled',
            'status_color': 'green',
            'icon': 'fa-wifi',
        },
        {
            'type': 'Router',
            'name': 'EMP-RTR-2',
            'status': 'Offline',
            'ip_address': '192.168.171.174',
            'ssh': 'Disabled',
            'firewall': 'Enabled',
            'status_color': 'red',
            'icon': 'fa-wifi',
        },
    ]

    switches = [
        {
            'type': 'Switch',
            'name': 'EMP-SW-1',
            'status': 'Online',
            'ip_address': '192.168.45.135',
            'ssh': 'Enabled',
            'status_color': 'green',
            'icon': 'fa-server',
        },
        {
            'type': 'Switch',
            'name': 'EMP-SW-2',
            'status': 'Offline',
            'ip_address': '192.168.153.105',
            'ssh': 'Enabled',
            'status_color': 'red',
            'icon': 'fa-server',
        },
        {
            'type': 'Switch',
            'name': 'EMP-SW-3',
            'status': 'Online',
            'ip_address': '192.168.44.110',
            'ssh': 'Disabled',
            'status_color': 'green',
            'icon': 'fa-server',
        },
        {
            'type': 'Switch',
            'name': 'EMP-SW-4',
            'status': 'Online',
            'ip_address': '192.168.134.163',
            'ssh': 'Disabled',
            'status_color': 'green',
            'icon': 'fa-server',
        },
        {
            'type': 'Switch',
            'name': 'EMP-SW-5',
            'status': 'Online',
            'ip_address': '192.168.192.38',
            'ssh': 'Enabled',
            'status_color': 'green',
            'icon': 'fa-server',
        },
    ]

    end_devices = [
        {
            'type': 'End Device',
            'name': 'EMP-PC-1',
            'status': 'Online',
            'ip_address': '192.168.20.12',
            'ssh': 'N/A',
            'status_color': 'green',
            'icon': 'fa-laptop',
        },
        {
            'type': 'End Device',
            'name': 'EMP-PC-2',
            'status': 'Offline',
            'ip_address': '192.168.20.18',
            'ssh': 'N/A',
            'status_color': 'red',
            'icon': 'fa-laptop',
        },
        {
            'type': 'End Device',
            'name': 'EMP-PC-3',
            'status': 'Warning',
            'ip_address': '192.168.20.27',
            'ssh': 'Enabled',
            'status_color': 'yellow',
            'icon': 'fa-laptop',
        },
    ]

    if active_tab == 'switches':
        devices = switches
        page_title = 'Employee Network'
        section_title = 'Switches'
        total_label = f'Total Switches: {len(switches)}'
        active_tab_name = 'switches'
    elif active_tab == 'end-devices':
        devices = end_devices
        page_title = 'Employee Network'
        section_title = 'End Devices'
        total_label = f'Total End Devices: {len(end_devices)}'
        active_tab_name = 'end-devices'
    else:
        devices = routers
        page_title = 'Employee Network'
        section_title = 'Routers'
        total_label = f'Total Routers: {len(routers)}'
        active_tab_name = 'routers'

    return render(request, 'employee_network.html', {
        'page_title': page_title,
        'section_title': section_title,
        'total_label': total_label,
        'devices': devices,
        'active_tab': active_tab_name,
    })

def management_network(request):
    active_tab = request.GET.get('tab', 'routers')

    routers = []
    switches = []
    end_devices = []

    if active_tab == 'switches':
        devices = switches
        total_label = f'Total Switches: {len(switches)}'
        active_tab_name = 'switches'
    elif active_tab == 'end-devices':
        devices = end_devices
        total_label = f'Total End Devices: {len(end_devices)}'
        active_tab_name = 'end-devices'
    else:
        devices = routers
        total_label = f'Total Routers: {len(routers)}'
        active_tab_name = 'routers'

    return render(request, 'management_network.html', {
        'page_title': 'Management Network',
        'devices': devices,
        'total_label': total_label,
        'active_tab': active_tab_name,
    })