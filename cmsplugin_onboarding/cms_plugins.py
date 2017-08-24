# -*- coding: utf-8 -*-
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from .models import OnboardingContainer, OnboardingItem

class OnboardingContainerPlugin(CMSPluginBase):
    model = OnboardingContainer
    name = _('Onboarding Container')
    module = _('Onboarding')
    render_template = 'onboarding_container.html'
    allow_children = True
    child_classes = ['OnboardingItemPlugin', 'TextPlugin']

    def render(self, context, instance, placeholder):
        context = super(OnboardingContainerPlugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(OnboardingContainerPlugin)

class OnboardingItemPlugin(CMSPluginBase):
    model = OnboardingItem
    name = _('Onboarding Item')
    module = _('Onboarding')
    render_template = 'onboarding_item.html'
    require_parent = True
    parent_classes = ['OnboardingContainerPlugin']

    def render(self, context, instance, placeholder):
        context = super(OnboardingItemPlugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(OnboardingItemPlugin)
