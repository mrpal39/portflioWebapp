# Generated by Django 3.2.7 on 2021-10-05 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyjobs',
            name='company_profile',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='companyjobs',
            name='department',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='companyjobs',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
