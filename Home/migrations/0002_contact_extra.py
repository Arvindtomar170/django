# Generated by Django 4.0.1 on 2022-01-09 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='extra',
            field=models.CharField(default='This is a extra coulumn', max_length=100),
            preserve_default=False,
        ),
    ]
