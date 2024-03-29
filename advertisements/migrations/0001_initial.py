# Generated by Django 4.2.1 on 2023-05-23 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('description', models.TextField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.car', verbose_name='car')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advertisements.ad')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.user')),
            ],
        ),
        migrations.AddField(
            model_name='ad',
            name='comments',
            field=models.ManyToManyField(related_name='commented_ads', through='advertisements.Comment', to='account.user'),
        ),
        migrations.AddField(
            model_name='ad',
            name='likes',
            field=models.ManyToManyField(related_name='liked_ads', to='account.user'),
        ),
        migrations.AddField(
            model_name='ad',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.user', verbose_name='user'),
        ),
    ]
