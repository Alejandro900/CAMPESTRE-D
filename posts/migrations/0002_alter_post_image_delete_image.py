# Generated by Django 5.0.6 on 2024-07-21 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]