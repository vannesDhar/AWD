# Generated by Django 4.2.6 on 2023-12-28 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('L001app', '0004_alter_nutritionalinformation_food_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nutritionalinformation',
            name='food_item',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='L001app.fooditem'),
        ),
    ]
