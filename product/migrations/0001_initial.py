# Generated by Django 4.2.7 on 2023-11-18 07:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('color', models.CharField(choices=[('none', 'None'), ('red', 'Red'), ('blue', 'Blue'), ('green', 'Green')], default='none', max_length=20)),
                ('weight', models.IntegerField()),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]