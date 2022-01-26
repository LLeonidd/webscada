from django.db import models


class DeviceGroup(models.Model):
    """
    Группа оборудования
    """
    name = models.CharField(max_length=300, verbose_name='Название группы')
    description = models.CharField(max_length=300, verbose_name='Описание группы')
    link = models.CharField(max_length=228, verbose_name='Альяс группы', help_text='Из альяса формируется ссылка в панели навигации на группу')
    icon = models.CharField(max_length=228, null=True, blank=True, default='',
                            verbose_name='Css Class иконки',
                            help_text='css класс иконки')
    priority = models.PositiveSmallIntegerField(
        default=0,
        verbose_name='Приоритет в панели навигации',
        help_text='Чем меньше значение, тем левее расположена группа в панели навигации'
    )

    class Meta:
        db_table = 'tb_device_groups'
        verbose_name = 'Группа оборудования'
        verbose_name_plural = 'Группы оборудования'

    def __str__(self):
        return self.name


class Box(models.Model):
    """
    Бокс. Контейнер, в который помещаются теги
    """
    name = models.CharField(max_length=228)
    description = models.CharField(max_length=228)
    group = models.ForeignKey(DeviceGroup, on_delete=models.CASCADE, null=True, blank=True)
    priority = models.CharField(max_length=228)
    visible = models.BooleanField(default=True)
    expanded = models.BooleanField(default=False) # бокс свёрнут при False

    class Meta:
        db_table = 'tb_boxes'
        verbose_name = 'Бокс'
        verbose_name_plural = 'Боксы'

    def __str__(self):
        return f'{self.group.description if self.group else "Нет группы"}. {self.description}'


class ValueStyle(models.Model):
    """
    Единица измерения
    """
    name = models.CharField(max_length=228)
    description = models.CharField(max_length=228, null=True, blank=True)

    class Meta:
        db_table = 'tb_value_styles'
        verbose_name = 'Единица измерения'
        verbose_name_plural = 'Единицы измерения'

    def __str__(self):
        return f'{self.name}. {self.description}'


class Plc(models.Model):
    """
    Контроллер.
    """
    name = models.CharField(max_length=228)
    description = models.CharField(max_length=228)

    class Meta:
        db_table = 'tb_plcs'
        verbose_name = 'Контроллер'
        verbose_name_plural = 'Контроллеры'

    def __str__(self):
        return self.name


class AccessType(models.Model):
    """
    Тип доступа.
    """
    name = models.CharField(max_length=228)
    description = models.CharField(max_length=228)

    class Meta:
        db_table = 'tb_access_types'
        verbose_name = 'Тип доступа'
        verbose_name_plural = 'Типы доступа'

    def __str__(self):
        return self.name


class DataType(models.Model):
    """
    Тип данных.
    """
    name = models.CharField(max_length=228)
    description = models.CharField(max_length=228)

    class Meta:
        db_table = 'tb_data_types'
        verbose_name = 'Тип данных'
        verbose_name_plural = 'Типы данных'

    def __str__(self):
        return self.name


class Mode(models.Model):
    """
    Вариант состояния.
    """
    name = models.CharField(max_length=228, verbose_name='Название')
    value = models.CharField(max_length=228, verbose_name='Значение')
    text = models.CharField(max_length=228, verbose_name='Текст при значении')
    style = models.CharField(max_length=228, verbose_name='Классы при значении')

    class Meta:
        db_table = 'tb_modes'
        verbose_name = 'Вариант состояний'
        verbose_name_plural = 'Варианты состояний'

    def __str__(self):
        return self.value + '-' + self.text


class ModesGroup(models.Model):
    """
    Набор вариантов состояний.
    """
    name = models.CharField(max_length=228)
    description = models.CharField(max_length=228)
    modes = models.ManyToManyField(Mode)

    class Meta:
        db_table = 'tb_modes_groups'
        verbose_name = 'Набор состояний'
        verbose_name_plural = 'Наборы состояний'

    def __str__(self):
        return self.description


class LineType(models.Model):
    """
    Тип линии графиков.
    """
    name = models.CharField(max_length=228)
    description = models.CharField(max_length=228, blank=True, null=True)

    class Meta:
        db_table = 'tb_line_types'
        verbose_name = 'Тип линии'
        verbose_name_plural = 'Типы линий'

    def __str__(self):
        return f'{self.name}. {self.description}'


class Tag(models.Model):
    """
    Тег.
    """
    name = models.CharField(max_length=228, verbose_name='Имя')
    description = models.CharField(max_length=228, verbose_name='Описание')
    data_type = models.ForeignKey(DataType, on_delete=models.CASCADE, verbose_name='Тип данных')
    access = models.ForeignKey(AccessType, on_delete=models.CASCADE, verbose_name='Доступ')
    box = models.ForeignKey(Box, on_delete=models.CASCADE, verbose_name='Бокс')
    priority = models.PositiveSmallIntegerField(
        default=0,
        verbose_name='Приоритет в боксе',
        help_text='Чем меньше значение, тем выше тег расположен в боксе'
    )
    icon = models.CharField(max_length=228, verbose_name='Значок тега на форме', help_text='CSS class')
    valueStyle = models.ForeignKey(ValueStyle, on_delete=models.CASCADE, verbose_name='Единица измерения')
    decimal = models.CharField(max_length=228, verbose_name='Количество знаков после запятой')
    plc = models.ForeignKey(Plc, on_delete=models.CASCADE, verbose_name='Контроллер')
    modes = models.ForeignKey(ModesGroup, on_delete=models.CASCADE, verbose_name='Отображать как')
    info_page = models.BooleanField(default=False, verbose_name='Выводить на сводной странице объкта')
    chart = models.BooleanField(default=False, verbose_name='Выводить в графиках')
    line = models.ForeignKey(LineType, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Тип линии графиков')
    alarm = models.BooleanField(default=False, db_index=True, verbose_name='Аварийный тег')
    comm = models.BooleanField(default=False, verbose_name='Тег признака связи с устройством')
    spm = models.BooleanField(default=False, verbose_name='Использовать в мониторе уставок')

    class Meta:
        db_table = 'tb_tags'
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return f'{self.plc.name}. {self.box.name}. {self.name}. {self.description}'


class WidgetType(models.Model):
    """
    Виджет.
    """
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.CharField(max_length=300, verbose_name='Описание')
    infopage = models.BooleanField(default=True, verbose_name='Отображать на главной', help_text='Отображать на главной странице объекта')

    class Meta:
        db_table = 'tb_widgets'
        verbose_name = 'Виджет'
        verbose_name_plural = 'Виджеты'

    def __str__(self):
        return f'{self.name}. {self.description}'


class WidgetItem(models.Model):
    """
    Элемент виджета.
    """
    widget = models.ForeignKey(WidgetType, on_delete=models.CASCADE, verbose_name='Виджет')
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    plc = models.CharField(max_length=100)

    class Meta:
        db_table = 'tb_widget_items'
        verbose_name = 'Элемент виджета'
        verbose_name_plural = 'Элементы виджетов'

    def __str__(self):
        return f'{self.name}. {self.plc}. {self.tag.Name}. {self.tag.Description}'