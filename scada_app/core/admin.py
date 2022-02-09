from django.contrib import admin
from .models import District, Region, ServiceCompany, ObjectPoint

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    ordering = ('name',)
    list_display = ('id', 'name',)
    list_filter = ('name',)


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    ordering = ('name',)
    list_display = ('id', 'name', 'district', 'timezone', )
    list_filter = ('name',)


@admin.register(ObjectPoint)
class ObjectPointAdmin(admin.ModelAdmin):
    ordering = ('region__name', 'name',)
    list_display = ('code', 'name', 'address', 'guid', 'on_service_mode')
    list_filter = ('on_service_mode', 'region__district__name', 'region__name')
    search_fields = ('name', 'region__name', 'code', 'address')

    # name = models.CharField(max_length=200, verbose_name='Название объекта')
    # address = models.CharField(max_length=300, blank=True, verbose_name='Адрес')
    # on_service_mode = models.BooleanField(default=True, verbose_name='Сервиснай режим',
    #                                       help_text='В сервисном режиме не отправляет оповещения об авариях')
    # code = models.CharField(max_length=10, verbose_name='Код объекта', blank=True)
    # guid = models.CharField(max_length=300, null=True, blank=True, verbose_name='GUID объекта')
    # service = models.ForeignKey(ServiceCompany, on_delete=models.CASCADE, blank=True, verbose_name='Сервисная компания')
    # district = models.ForeignKey(District, on_delete=models.CASCADE, verbose_name='Округ')
    # devices = models.ManyToManyField(DeviceGroup, blank=True, verbose_name='Группы устройств объекта', )
    # widgets = models.ManyToManyField(WidgetType, blank=True, verbose_name='Виджеты', )

