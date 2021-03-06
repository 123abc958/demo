# Generated by Django 3.1.7 on 2021-05-20 09:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35, verbose_name='名前')),
                ('education', models.CharField(max_length=35, verbose_name='教育')),
                ('github', models.CharField(max_length=35, verbose_name='GitHub')),
                ('facebook', models.CharField(max_length=35, verbose_name='facebook')),
                ('blog', models.CharField(max_length=35, verbose_name='blog')),
                ('mail', models.CharField(max_length=35, verbose_name='mail')),
                ('mobile', models.CharField(max_length=35, verbose_name='携帯')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=35, verbose_name='タイトル')),
                ('text', models.TextField(verbose_name='本文')),
                ('image', models.ImageField(blank=True, upload_to='images', verbose_name='画像')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='投稿日')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
