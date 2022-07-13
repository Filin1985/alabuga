# Generated by Django 4.0.4 on 2022-07-12 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Citizen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=200, verbose_name='Фамилия')),
                ('age', models.IntegerField(verbose_name='Возраст')),
                ('status', models.CharField(choices=[('Феодал', 'Феодал'), ('Духовенство', 'Духовенство'), ('Крестьянин', 'Крестьянин')], max_length=50, verbose_name='Статус')),
                ('subordinate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='citizens.citizen', verbose_name='Подчиненный')),
            ],
        ),
    ]