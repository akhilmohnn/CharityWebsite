# Generated by Django 5.0 on 2024-03-03 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Organization', '0016_alter_tbl_rating_org_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_rating',
            name='rating_data',
            field=models.IntegerField(),
        ),
    ]
