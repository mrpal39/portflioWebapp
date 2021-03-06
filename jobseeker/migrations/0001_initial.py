# Generated by Django 3.2.7 on 2021-10-05 03:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Occupation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(blank=True, default='3', max_length=100, null=True)),
                ('image', models.ImageField(default='assets/img/avataaars.svg', upload_to='media/')),
                ('email', models.EmailField(default='admin@gmial.com', max_length=254)),
                ('phone', models.IntegerField(default='012345678')),
                ('experence', models.CharField(default='d', max_length=100)),
                ('occupation', models.CharField(max_length=100)),
                ('skills', models.CharField(default='d', max_length=100)),
                ('age', models.CharField(default='d', max_length=100)),
                ('status', models.CharField(default='d', max_length=100)),
                ('mobile', models.CharField(default='d', max_length=100)),
                ('gender', models.CharField(default='d', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='social_conect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform_name', models.CharField(default='facebook', max_length=100)),
                ('platform_url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_created', models.DateTimeField(auto_now_add=True, verbose_name='Date of Review')),
                ('reviewer_name', models.CharField(default='admin', max_length=55)),
                ('reviewer_city', models.CharField(default='kaithal', max_length=55)),
                ('reviewer_state', models.CharField(default='hr', max_length=2)),
                ('email', models.EmailField(default='admin@gmail.com', max_length=254)),
                ('rating', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1)),
                ('review_comment', models.TextField(default='Great Work')),
                ('review_slug', models.SlugField(default='')),
                ('profile_rating', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='jobseeker.profile')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='social_account',
            field=models.ManyToManyField(to='jobseeker.social_conect'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
