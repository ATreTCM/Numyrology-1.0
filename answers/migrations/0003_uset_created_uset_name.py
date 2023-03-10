# Generated by Django 4.0.5 on 2022-10-02 17:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('answers', '0002_uset'),
    ]

    operations = [
        migrations.AddField(
            model_name='uset',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uset',
            name='name',
            field=models.CharField(null=True, max_length=50, verbose_name='Имя'),
        ),
    ]
