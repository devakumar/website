from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, blank=True)
    date = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    venue = models.CharField(max_length=200, null=True, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    contact_number = models.CharField(validators=[phone_regex], blank=True, max_length=15) # validators should be a list
    contact_number_sec = models.CharField(validators=[phone_regex], blank=True, max_length=15) # validators should be a list
    
    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')
        ordering = ('date',)

    def __unicode__(self):
        return self.name