# Generated by Django 3.0 on 2021-12-19 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_auto_20211219_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.categoria'),
        ),
    ]
