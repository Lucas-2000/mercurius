from datetime import datetime
from django.db import models
from django.conf import settings

EMPLOYER_ROLE = [
  ('Prefeito', 'Prefeito'),
  ('Vereador', 'Vereador'),
  ('Acessor', 'Acessor'),
  ('Funcionário Publico', 'Funcionário Publico')
]

TYPE_TRANSACTION = [
  ('Gasto', 'Gasto'),
  ('Entrada', 'Entrada'),
]

UF = [
  ('AC', 'Acre'),
  ('AL', 'Alagoas'),
  ('AP', 'Amapá'),
  ('AM', 'Amazonas'),
  ('BA', 'Bahia'),
  ('CE', 'Ceará'),
  ('DF', 'Distrito Federal'),
  ('ES', 'Espirito Santo'),
  ('GO', 'Goiás'),
  ('MA', 'Maranhão'),
  ('MT', 'Mato Grosso'),
  ('MS', 'Mato Grosso do Sul'),
  ('MG', 'Minas Gerais'),
  ('PA', 'Pará'),
  ('PB', 'Paraíba'),
  ('PR', 'Paraná'),
  ('PE', 'Pernambuco'),
  ('PI', 'Piauí'),
  ('RJ', 'Rio de Janeiro'),
  ('RN', 'Rio Grande do Norte'),
  ('RS', 'Rio Grande do Sul'),
  ('RO', 'Rondônia'),
  ('RR', 'Roraima'),
  ('SC', 'Santa Catarina'),
  ('SP', 'São Paulo'),
  ('SE', 'Sergipe'),
  ('TO', 'Tocantins'),
]

# Create your models here.
class Neighborhood(models.Model):
  nome = models.CharField(max_length=255)
  populacao = models.DecimalField(max_digits=12, decimal_places=2)
  
  def __str__(self):
    return self.nome
    
class Employer(models.Model):
  cpf = models.CharField(max_length=11)
  nome = models.CharField(max_length=255)
  sobrenome = models.CharField(max_length=255)
  data_nascimento = models.DateField(default=datetime.today)
  uf = models.CharField(choices=UF, max_length=255)
  cargo = models.CharField(choices=EMPLOYER_ROLE, max_length=255)
  salario = models.DecimalField(max_digits=10, decimal_places=2)
  
  def __str__(self):
    return f"{self.nome} {self.sobrenome}"
    
class Transaction(models.Model):
  descricao = models.CharField(max_length=255)
  valor = models.DecimalField(max_digits=12, decimal_places=2)
  tipo = models.CharField(max_length=255, choices=TYPE_TRANSACTION, default='Gasto')
  data_criacao = models.DateTimeField(auto_now_add=True)
  comprovante = models.FileField(upload_to='comprovantes/')
  usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.descricao
