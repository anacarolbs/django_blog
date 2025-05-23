# Generated by Django 5.2 on 2025-05-05 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_event_poll_votepoll'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('category', models.CharField(max_length=100)),
                ('tags', models.CharField(blank=True, max_length=200, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
