# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
    ]

    operations = [
        migrations.CreateModel(
            name='OnboardingContainer',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
            ],
            options={
                'verbose_name': 'Onboarding Container',
                'verbose_name_plural': 'Onboarding Containers',
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='OnboardingItem',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('target', models.CharField(max_length=250, verbose_name='Selector for the tooltip target')),
                ('tooltip_position', models.CharField(default=b'bottom', max_length=6, verbose_name='Tooltip position', choices=[(b'top', b'Top'), (b'bottom', b'Bottom'), (b'left', b'Left'), (b'right', b'Right')])),
            ],
            options={
                'verbose_name': 'Onboarding Item',
                'verbose_name_plural': 'Onboarding Items',
            },
            bases=('cms.cmsplugin',),
        ),
    ]
