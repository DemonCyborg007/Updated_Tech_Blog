# Generated by Django 5.0.4 on 2024-05-29 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blog_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
