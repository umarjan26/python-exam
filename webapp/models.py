from django.db import models

STATUS = [('active', 'активная'), ('blocked', 'заблокировано')]


class Guestbook(models.Model):
    author = models.CharField(max_length=50, null=False, blank=False, verbose_name="автор")
    email = models.EmailField(max_length=50, null=False, blank=False, verbose_name="почта")
    text = models.CharField(max_length=3000, null=False, blank=False, verbose_name="текст")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    status = models.CharField(max_length=20, choices=STATUS, verbose_name="Статус", default=STATUS[0][0])



    def __str__(self):
        return f"{self.id}. {self.author}: {self.email}"



    class Meta:
        db_table = "Guestbooks"
        verbose_name = "гостевая книга"
        verbose_name_plural = "гостевые книги"
