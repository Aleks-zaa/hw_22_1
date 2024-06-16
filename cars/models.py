from django.db import models


class Category(models.Model):
    objects = None
    name = models.CharField(max_length=100, verbose_name='Категория')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    objects = None
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to='cars/photo', blank=True, null=True, verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория',
                                 related_name='products')
    price = models.IntegerField(verbose_name='Цена за покупку', blank=True,
                                null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')

    view_counter = models.PositiveIntegerField(
        verbose_name='Счетчик просмотров',
        help_text='Укажите колличество просмотров',
        default=0
    )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.name} {self.description} {self.category} {self.price}'


class Version(models.Model):
    objects = None
    product = models.ForeignKey(Product, related_name='versions', on_delete=models.CASCADE, null=True, blank=True,
                                verbose_name='Версия машины', )
    name = models.TextField(verbose_name="название версии")
    number = models.IntegerField(verbose_name="номер версии", null=True, blank=True)
    sign = models.BooleanField(default=True, verbose_name='признак текущей версии')

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'

    def __str__(self):
        return f'{self.name}'
