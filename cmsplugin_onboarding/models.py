# -*- coding: utf-8 -*-
from django.db import models
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _

class OnboardingContainer(CMSPlugin):
    class Meta:
        verbose_name = _('Onboarding Container')
        verbose_name_plural = _('Onboarding Containers')

    def __unicode__(self):
        return ''

class OnboardingItem(CMSPlugin):
    POSITIONS = (
        ('top', 'Top'),
        ('bottom', 'Bottom'),
        ('left', 'Left'),
        ('right', 'Right')
    )

    target = models.CharField(max_length=250, verbose_name=_('Selector for the tooltip target'))
    tooltip_position = models.CharField(max_length=6, verbose_name=_('Tooltip position'), default='bottom', choices=POSITIONS)
    instruction = models.CharField(max_length=250, verbose_name=_('Item instruction'), default='')

    class Meta:
        verbose_name = _('Onboarding Item')
        verbose_name_plural = _('Onboarding Items')

    def __unicode__(self):
        return '%s' % self.target
