# Generated by Django 4.0.4 on 2022-05-06 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ics', '0014_alter_bscs1_1_coursecs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bscs1_1',
            name='courseCS',
            field=models.CharField(default=0, max_length=5),
            preserve_default=False,
        ),
    ]
