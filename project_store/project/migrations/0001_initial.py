# Generated by Django 3.2.4 on 2021-09-12 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('desc', models.TextField(max_length=1000)),
                ('web_url', models.URLField(blank=True)),
                ('yt_url', models.URLField(blank=True)),
                ('yt_embed_url', models.URLField(blank=True)),
                ('img', models.ImageField(upload_to='project')),
                ('original_price', models.IntegerField()),
                ('discounted_price', models.IntegerField()),
                ('publish_date', models.DateTimeField()),
            ],
        ),
    ]
