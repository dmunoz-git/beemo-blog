# Generated by Django 2.2.4 on 2019-08-22 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment_reply'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]