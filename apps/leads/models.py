from django.db import models
from django.utils.translation import ugettext_lazy as _


class Lead(models.Model):
    class Meta:
        verbose_name = _("Lead")
        verbose_name_plural = _("Leads")

    name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)

    def __str__(self):
        return self.name
