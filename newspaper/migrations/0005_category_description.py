# Generated by Django 5.2 on 2025-04-17 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0004_category_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
