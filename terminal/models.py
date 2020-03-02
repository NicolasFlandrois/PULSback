from django.db import models
from django.conf import settings
from fleet.models import Campaign


class Game(models.Model):
    name = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
    description = models.TextField()
    logo = models.FileField(blank=True, null=True, upload_to="games/logos/")
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Terminal(models.Model):
    name = models.CharField(max_length=255)
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="terminal")
    campaigns = models.ManyToManyField(Campaign)
    games = models.ManyToManyField(Game)
    location = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    is_on = models.BooleanField(default=False)
    is_playing = models.BooleanField(default=False)

    def __str__(self):
        return 'Terminal {} : {}'.format(self.pk, 'Active' if self.is_active else 'False')


class Donator(models.Model):
    email = models.EmailField(blank=True, null=True)
    accept_asso = models.BooleanField(blank=True, null=True, default=False)
    accept_newsletter = models.BooleanField(blank=True, null=True, default=False)

    def __str__(self):
        return 'Donator {}'.format(self.pk)


class Session(models.Model):
    donator = models.ForeignKey(Donator, on_delete=models.PROTECT, related_name="sessions")
    campaign = models.ForeignKey(Campaign, on_delete=models.PROTECT, related_name="sessions")
    terminal = models.ForeignKey(Terminal, on_delete=models.PROTECT, related_name="sessions")
    game = models.ForeignKey(Game, on_delete=models.PROTECT, null=True, related_name="sessions")
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    start_global = models.DateTimeField(blank=True, null=True)
    end_global = models.DateTimeField(blank=True, null=True)
    position_asso = models.IntegerField()
    timesession = models.DurationField(blank=True, null=True)
    timesession_global = models.DurationField(blank=True, null=True)

    def __str__(self):
        return "Session {} : {} global".format(self.pk, self.timesession_global)


class Payment(models.Model):
    donator = models.ForeignKey(Donator, on_delete=models.PROTECT, null=True, related_name="payments")
    campaign = models.ForeignKey(Campaign, on_delete=models.PROTECT, related_name="payments")
    terminal = models.ForeignKey(Terminal, on_delete=models.PROTECT, related_name="payments")
    game = models.ForeignKey(Game, on_delete=models.PROTECT, null=True, related_name="payments")
    date = models.DateTimeField(auto_now=True)
    method = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    amount = models.FloatField()
    currency = models.CharField(max_length=255)

    def __str__(self):
        return "Payment of {} {} by {}".format(self.amount, self.currency, self.donator)