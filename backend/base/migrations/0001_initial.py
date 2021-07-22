# Generated by Django 3.2.5 on 2021-07-22 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('image', models.ImageField(null=True, upload_to='')),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
            ],
        ),
    ]
