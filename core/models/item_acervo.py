from django.db import models

class ItemAcervo(models.Model):

    ESTADO_CONSERVACAO_CHOICES = [
        ("excelente", "Excelente"),
        ("bom", "Bom"),
        ("regular", "Regular"),
        ("ruim", "Ruim"),
        ("pessimo", "Péssimo"),
        ("restaurado", "Restaurado"),
    ]

    numero_acervo = models.CharField(max_length=100, unique=True)
    titulo = models.CharField(max_length=255)

    colecao = models.ForeignKey(
        'Colecao', on_delete=models.SET_NULL, null=True, blank=True
    )
    materia_prima = models.ForeignKey(
        'MateriaPrima', on_delete=models.SET_NULL, null=True, blank=True
    )
    subtipo_materia_prima = models.ForeignKey(
        'SubtipoMateriaPrima', on_delete=models.SET_NULL, null=True, blank=True
    )

    procedencia_origem = models.CharField(max_length=255, blank=True, null=True)

    # DATACAO COMO INTERVALO (recomendado)
    datacao_de = models.DateField(null=True, blank=True)
    datacao_ate = models.DateField(null=True, blank=True)

    estado_conservacao = models.CharField(
        max_length=20,
        choices=ESTADO_CONSERVACAO_CHOICES,
        default="bom"
    )

    localizacao_fisica = models.ForeignKey(
        'Localizacao',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='itens'
    )

    descricao = models.TextField(blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.numero_acervo} - {self.titulo}"
