# Generated by Django 4.0.4 on 2022-07-12 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('citizens', '0003_alter_citizen_income_alter_citizen_subordinate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citizen',
            name='subordinate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='citizens.citizen', verbose_name='Подчиненный'),
        ),
    ]
