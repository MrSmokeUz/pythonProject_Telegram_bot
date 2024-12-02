from django.db import models

class Card(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='cards/', verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
