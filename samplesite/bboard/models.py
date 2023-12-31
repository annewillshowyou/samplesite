from django.db import models

"BBOARD"
class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    content = models.TextField(null = True, blank = True,verbose_name="Описание")
    price = models.FloatField(null = True, blank = True, verbose_name="Цена")
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')

    rubric = models.ForeignKey('Rubric', null = True, on_delete=models.PROTECT, verbose_name = 'Рубрика')

    class Meta:
        verbose_name_plural = "Объявления"
        verbose_name = "Объявление"
        ordering = ['-published']

"RUBRIC"
class Rubric(models.Model):
    name = models.CharField(max_length=50, db_index = True, verbose_name = 'Название')

    class Meta:
        verbose_name_plural = "Рубрики"
        verbose_name = "Рубрика"
        ordering = ['name']
        