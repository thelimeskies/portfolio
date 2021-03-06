# Generated by Django 4.0 on 2021-12-18 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_social'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='header_image',
            field=models.ImageField(upload_to='header/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='project_image/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image_2x',
            field=models.ImageField(upload_to='project_image2x/'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='image',
            field=models.ImageField(upload_to='testimonial/'),
        ),
    ]
