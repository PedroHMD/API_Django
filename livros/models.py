from django.db import models
from uuid import uuid4
class livros(models.Model):
    id_livro = models.UUIDField(primary_key=True,default=uuid4(),editable= False)
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=60)
    ano_lancamento = models.IntegerField()
    condicao = models.CharField(max_length=30) # condição atual do livro: "novo","usado"
    paginas_qtd = models.IntegerField()
    editora = models.CharField(max_length=80)
    qnd_criado = models.DateField(auto_now_add=True)