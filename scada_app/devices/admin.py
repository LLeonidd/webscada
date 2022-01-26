from django.contrib import admin

from .models import (DeviceGroup, Tag, ModesGroup, Mode, Box, ValueStyle, Plc, WidgetType, WidgetItem)


@admin.register(Plc)
class PlcAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', )


@admin.register(Box)
class BoxAdmin(admin.ModelAdmin):
    search_fields = ('name', 'description')
    ordering = ('group__name', 'description',)
    list_display = ('id', 'name', 'description', 'group' ,)
    list_filter = ('group',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    ordering = ('box__group__name', 'plc__name',
                'box__name', 'name', 'description',)
    search_fields = ('name', 'description', 'box__name', 'box__group__name',)
    list_display = ('plc', 'box', 'name',
                    'description', 'access', 'data_type', 'priority')
    list_filter = ('plc', 'box',)


@admin.register(WidgetItem)
class WidgetItemAdmin(admin.ModelAdmin):
    list_display = ('widget', 'name', 'plc', 'tag', 'description', )
    list_filter = ('widget', 'plc', 'description')
    search_field = ('name', 'tag')


@admin.register(Mode)
class ModeAdmin(admin.ModelAdmin):
    ordering = ('name',)
    list_display = ('name', 'value', 'text')


@admin.register(DeviceGroup)
class DeviceGroupAdmin(admin.ModelAdmin):
    ordering = ('name',)
    list_display = ('name', 'id', 'description',
        'link', 'icon', 'priority')


admin.site.register(ModesGroup)
admin.site.register(ValueStyle)
admin.site.register(WidgetType)
