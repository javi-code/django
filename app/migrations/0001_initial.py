# Generated by Django 4.0.4 on 2022-11-17 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CategoryShop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('id_file', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('name', models.CharField(default='', max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('urlid', models.CharField(max_length=80)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.categoryshop')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('urlid', models.CharField(max_length=80)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.categoryproduct')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.shop')),
            ],
        ),
    ]
