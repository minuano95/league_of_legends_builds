# Generated by Django 4.1 on 2022-10-23 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_build'),
    ]

    operations = [
        migrations.AddField(
            model_name='build',
            name='lanes',
            field=models.CharField(choices=[('Top', 'Top'), ('Jungle', 'Jungle'), ('Mid', 'Mid'), ('ADC', 'ADC'), ('Sup', 'Sup')], default='Top', max_length=8),
        ),
    ]
