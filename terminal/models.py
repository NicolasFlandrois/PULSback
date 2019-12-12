from django.db import models
from django.conf import settings
from fleet.models import Customer, Campaign


class Terminal(models.Model):
    name = models.CharField(max_length=255)
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="terminal")
    campaign = models.ForeignKey(Campaign, on_delete=models.PROTECT, null=True, related_name="terminals")
    is_active = models.BooleanField(default=False)
    is_on = models.BooleanField(default=False)
    is_playing = models.BooleanField(default=False)

    def __str__(self):
        return 'Terminal {} : {}'.format(self.pk, 'Active' if self.is_active else 'False')


class Donator(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    balance = models.FloatField(default=0)
    gender = models.CharField(max_length=1)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Session(models.Model):
    donator = models.ForeignKey(Donator, on_delete=models.PROTECT, related_name="sessions")
    campaign = models.ForeignKey(Campaign, on_delete=models.PROTECT, related_name="sessions")
    terminal = models.ForeignKey(Terminal, on_delete=models.PROTECT, related_name="sessions")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    timesession = models.DurationField()

    def __str__(self):
        return "Session {} : {}".format(self.pk, self.timesession)


class Payment(models.Model):
    donator = models.ForeignKey(Donator, on_delete=models.PROTECT, null=True, related_name="payments")
    campaign = models.ForeignKey(Campaign, on_delete=models.PROTECT, related_name="payments")
    terminal = models.ForeignKey(Terminal, on_delete=models.PROTECT, related_name="payments")
    date = models.DateTimeField(auto_now=True)
    method = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    amount = models.FloatField()
    currency = models.CharField(max_length=255)

    def __str__(self):
        return "Payment of {} {} by {}".format(self.amount, self.currency, self.donator)