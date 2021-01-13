# Generated by Django 3.1.5 on 2021-01-13 00:34

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('worktime', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Territory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('bec8a0ff-9999-4247-8573-bcc5c04592b3'), primary_key=True, serialize=False)),
                ('customer', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=255)),
                ('note', models.CharField(max_length=255)),
                ('duration', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.orderduration')),
                ('technik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.technik')),
                ('territory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.territory')),
            ],
        ),
    ]
