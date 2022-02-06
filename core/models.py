from django.db import models


NULL_BLANK = {
    "null": True,
    "blank": True
}


class TimeModel(models.Model):
    created_at = models.DateTimeField("Дата создания", auto_now_add=True, **NULL_BLANK)
    updated_at = models.DateTimeField("Дата изменения", auto_now=True, **NULL_BLANK)

    class Meta:
        abstract = True


class Note(TimeModel):
    text = models.TextField('Текст', **NULL_BLANK)
    image = models.ImageField('Фотоверсия', upload_to="foto/%Y/%m/%d", **NULL_BLANK)

    class Meta:
        verbose_name = 'Заметки'
        verbose_name_plural = 'Заметки'
        ordering = ['-created_at', '-id']

    def __str__(self):
        return f"{self.pk} {self.created_at}"
