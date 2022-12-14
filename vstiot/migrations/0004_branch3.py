# Generated by Django 4.0.4 on 2022-06-05 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vstiot', '0003_branch2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ICCID1', models.CharField(max_length=50)),
                ('IMEI', models.CharField(max_length=50)),
                ('SERIAL', models.CharField(max_length=50)),
                ('STATUS', models.CharField(choices=[('ACTIVATED', 'active'), ('INACTIVE', 'not active')], default='INACTIVE', max_length=50)),
            ],
        ),
    ]
