# Generated by Django 4.0.4 on 2022-07-13 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('citizens', '0009_alter_citizen_age_citizen_age_gte_120_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='citizen',
            name='age_gte_120',
        ),
        migrations.RemoveConstraint(
            model_name='citizen',
            name='age_lte_0',
        ),
    ]
