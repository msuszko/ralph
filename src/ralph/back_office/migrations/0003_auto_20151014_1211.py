# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ralph.lib.transitions.fields


class Migration(migrations.Migration):

    dependencies = [
        ('back_office', '0002_backofficeasset_imei'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backofficeasset',
            name='status',
            field=ralph.lib.transitions.fields.TransitionField(choices=[(1, 'new'), (2, 'in progress'), (3, 'waiting for release'), (4, 'in use'), (5, 'loan'), (6, 'damaged'), (7, 'liquidated'), (8, 'in service'), (9, 'installed'), (10, 'free'), (11, 'reserved')], default=1),
        ),
    ]
