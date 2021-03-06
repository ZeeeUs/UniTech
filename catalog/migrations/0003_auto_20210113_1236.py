# Generated by Django 3.1.5 on 2021-01-13 09:36

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_order_orderduration_territory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['date']},
        ),
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.UUIDField(default=uuid.UUID('de07ba83-15aa-4769-97ab-76e776ce48f6'), primary_key=True, serialize=False),
        ),
    ]
