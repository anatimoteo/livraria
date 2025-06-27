from django.db import models

class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return f"({self.id}) {self.descricao.title()}" 
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['descricao']
        indexes = [
            models.Index(fields=['descricao']),
        ]