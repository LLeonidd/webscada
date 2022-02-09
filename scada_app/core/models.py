from django.db import models
from devices.models import DeviceGroup, WidgetType

class District(models.Model):
    """ Федеральный округ """
    name = models.CharField(max_length=200, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tb_districts'
        verbose_name = 'Округ'
        verbose_name_plural = 'Округа'


class Region(models.Model):
    """ Область, федерация, штат, край """
    name = models.CharField(max_length=200, verbose_name='Регион')
    district = models.ForeignKey(District, on_delete=models.CASCADE, verbose_name='Округ')
    timezone = models.CharField(max_length=128, verbose_name='Часовой пояс')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tb_regions'
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'


class ServiceCompany(models.Model):
    """
    Сервисные компании, обслуживающие объекты
    """
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    contacts = models.CharField(max_length=128)

    class Meta:
        db_table = 'tb_service_companies'
        verbose_name = 'Сервисная компания'
        verbose_name_plural = 'Сервисные компании'

    def __str__(self):
        return self.Name


class ObjectPoint(models.Model):
    """ Объект диспетчеризации """
    name = models.CharField(max_length=200, verbose_name='Название объекта')
    address = models.CharField(max_length=300, blank=True, verbose_name='Адрес')
    on_service_mode = models.BooleanField(default=True, verbose_name='Сервиснай режим', help_text='В сервисном режиме не отправляет оповещения об авариях')
    code = models.CharField(max_length=10, verbose_name='Код объекта', blank=True)
    guid = models.CharField(max_length=300, null=True, blank=True, verbose_name='GUID объекта')
    service = models.ForeignKey(ServiceCompany, on_delete=models.CASCADE, blank=True, verbose_name='Сервисная компания')
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name='Округ')
    devices = models.ManyToManyField(DeviceGroup, blank=True, verbose_name='Группы устройств объекта',)
    widgets = models.ManyToManyField(WidgetType, blank=True, verbose_name='Виджеты',)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tb_objects'
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'


