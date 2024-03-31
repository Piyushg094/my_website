# Generated by Django 4.1.1 on 2022-10-02 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=50)),
                ('hostel_name', models.CharField(max_length=50)),
                ('room_no', models.CharField(max_length=50)),
                ('phone_no', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=500)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/products/')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('description', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/products/')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='SellPurchase.category')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SellPurchase.student')),
            ],
        ),
    ]
