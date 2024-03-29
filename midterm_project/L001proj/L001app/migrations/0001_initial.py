# Generated by Django 4.2.6 on 2023-12-27 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='NutritionalInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calories', models.IntegerField()),
                ('cal_fat', models.IntegerField()),
                ('total_fat', models.IntegerField()),
                ('sat_fat', models.IntegerField()),
                ('trans_fat', models.FloatField()),
                ('cholesterol', models.IntegerField()),
                ('sodium', models.IntegerField()),
                ('food_item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='L001app.fooditem')),
            ],
        ),
        migrations.AddField(
            model_name='fooditem',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='L001app.restaurant'),
        ),
    ]
