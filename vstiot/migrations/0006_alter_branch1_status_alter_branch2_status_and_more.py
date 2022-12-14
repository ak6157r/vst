# Generated by Django 4.0.4 on 2022-06-05 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vstiot', '0005_alter_branch3_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch1',
            name='STATUS',
            field=models.CharField(choices=[('ACTIVE', 'active'), ('INACTIVE', 'not active')], default='INACTIVE', max_length=50),
        ),
        migrations.AlterField(
            model_name='branch2',
            name='STATUS',
            field=models.CharField(choices=[('ACTIVE', 'active'), ('INACTIVE', 'not active')], default='INACTIVE', max_length=50),
        ),
        migrations.AlterField(
            model_name='items',
            name='STATUS',
            field=models.CharField(choices=[('ACTIVE', 'active'), ('INACTIVE', 'not active')], default='INACTIVE', max_length=50),
        ),
    ]
