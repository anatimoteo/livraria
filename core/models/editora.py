from django.db import models

class Editora(models.Model):
    nome = models.CharField(max_length=100)
    site = models.URLField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    cidade = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Editora"
        verbose_name_plural = "Editoras"
        ordering = ['nome']
        indexes = [
            models.Index(fields=['nome']),
            models.Index(fields=['site']),
        ]