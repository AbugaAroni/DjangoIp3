# Generated by Django 3.1.2 on 2020-10-27 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0003_auto_20201027_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='live_site',
            field=models.CharField(max_length=100),
        ),
    ]