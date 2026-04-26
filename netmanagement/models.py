from django.db import models

# Create your models here.
from django.db import models

class Device(models.Model):
    DEVICE_TYPES = [
        ('router', 'Router'),
        ('switch', 'Switch'),
        ('end', 'End Device'),
    ]

    NETWORK_TYPES = [
        ('employee', 'Employee'),
        ('management', 'Management'),
    ]

    STATUS_TYPES = [
        ('online', 'Online'),
        ('offline', 'Offline'),
        ('warning', 'Warning'),
    ]

    name = models.CharField(max_length=100)
    device_type = models.CharField(max_length=10, choices=DEVICE_TYPES)
    network = models.CharField(max_length=15, choices=NETWORK_TYPES)

    ip_address = models.GenericIPAddressField()

    status = models.CharField(max_length=10, choices=STATUS_TYPES)
    ssh_enabled = models.BooleanField(default=False)
    firewall_enabled = models.BooleanField(default=False)

    def __str__(self):
        return self.name