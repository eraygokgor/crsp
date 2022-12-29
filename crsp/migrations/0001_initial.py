# Generated by Django 4.1.4 on 2022-12-29 18:13

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
            name='Recipes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=80)),
                ('beans', models.CharField(max_length=80)),
                ('roast', models.CharField(max_length=30)),
                ('grinder', models.CharField(max_length=80)),
                ('click', models.CharField(max_length=10)),
                ('blooming', models.CharField(max_length=10)),
                ('duration', models.CharField(max_length=10)),
                ('ratio', models.CharField(max_length=10)),
                ('method', models.CharField(max_length=30)),
                ('descripton', models.CharField(max_length=2000)),
                ('created_at', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
