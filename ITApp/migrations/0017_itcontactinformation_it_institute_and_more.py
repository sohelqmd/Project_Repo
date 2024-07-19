# Generated by Django 5.0.7 on 2024-07-17 05:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ITApp', '0016_itadmissionprocess_it_institute_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='itcontactinformation',
            name='it_institute',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ITApp.itinstitute'),
        ),
        migrations.AddField(
            model_name='itlocationinformation',
            name='it_institute',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ITApp.itinstitute'),
        ),
    ]
