# Generated by Django 4.2.2 on 2023-06-12 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('T_name', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('Salary', models.IntegerField()),
                ('join_Date', models.DateField(max_length=30)),
            ],
        ),
    ]
