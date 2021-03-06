# Generated by Django 4.0.1 on 2022-01-26 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('devices', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Округ',
                'verbose_name_plural': 'Округа',
                'db_table': 'tb_districts',
            },
        ),
        migrations.CreateModel(
            name='ServiceCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('address', models.CharField(max_length=128)),
                ('contacts', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Сервисная компания',
                'verbose_name_plural': 'Сервисные компании',
                'db_table': 'tb_service_companies',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Регион')),
                ('timezone', models.CharField(max_length=128, verbose_name='Часовой пояс')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.district', verbose_name='Округ')),
            ],
            options={
                'verbose_name': 'Регион',
                'verbose_name_plural': 'Регионы',
                'db_table': 'tb_regions',
            },
        ),
        migrations.CreateModel(
            name='ObjectPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название объекта')),
                ('address', models.CharField(blank=True, max_length=300, verbose_name='Адрес')),
                ('on_service_mode', models.BooleanField(default=True, help_text='В сервисном режиме не отправляет оповещения об авариях', verbose_name='Сервиснай режим')),
                ('code', models.CharField(blank=True, max_length=10, verbose_name='Код объекта')),
                ('guid', models.CharField(blank=True, max_length=300, null=True, verbose_name='GUID объекта')),
                ('devices', models.ManyToManyField(blank=True, to='devices.DeviceGroup', verbose_name='Группы устройств объекта')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.district', verbose_name='Округ')),
                ('service', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='core.servicecompany', verbose_name='Сервисная компания')),
                ('widgets', models.ManyToManyField(blank=True, to='devices.WidgetType', verbose_name='Виджеты')),
            ],
            options={
                'verbose_name': 'Объект',
                'verbose_name_plural': 'Объекты',
                'db_table': 'tb_objects',
            },
        ),
    ]
