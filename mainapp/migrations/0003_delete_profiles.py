# Generated by Django 4.0.5 on 2022-07-23 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_remove_profiles_image_alter_comments_product_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='profiles',
        ),
    ]
