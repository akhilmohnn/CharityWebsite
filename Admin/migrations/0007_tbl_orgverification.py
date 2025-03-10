# Generated by Django 5.0 on 2024-01-26 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0006_delete_tbl_orgverification'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_orgverification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('logo', models.FileField(upload_to='Orgdoc/')),
                ('proof', models.FileField(upload_to='Orgdoc/')),
                ('type', models.CharField(max_length=50)),
                ('status', models.CharField(default=0, max_length=50, null=True)),
            ],
        ),
    ]
