# Generated by Django 3.2.16 on 2022-11-20 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='pimg',
            field=models.ImageField(upload_to='pis2'),
        ),
    ]
