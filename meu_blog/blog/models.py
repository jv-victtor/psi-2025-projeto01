from django.db import models


class SiteInfo(models.Model):
	titulo_site = models.CharField(max_length=200)
	autor_projeto = models.CharField(max_length=100)
	email_contato = models.EmailField(blank=True)
	ano_copyright = models.CharField(max_length=10, blank=True)
	descricao_site = models.TextField(blank=True)

	class Meta:
		verbose_name = "Informação do Site"
		verbose_name_plural = "Informações do Site"

	def __str__(self):
		return self.titulo_site


class Atleta(models.Model):
	nome = models.CharField(max_length=200)
	idade = models.PositiveIntegerField()
	posicao = models.CharField(max_length=100)
	nascimento = models.CharField(max_length=200)
	foto_url = models.URLField(blank=True)

	class Meta:
		verbose_name = "Atleta"
		verbose_name_plural = "Atletas"

	def __str__(self):
		return self.nome


class Tarefa(models.Model):
	PENDENTE = 'pendente'
	CONCLUIDO = 'concluido'
	STATUS_CHOICES = [
		(PENDENTE, 'Pendente'),
		(CONCLUIDO, 'Concluído'),
	]

	titulo = models.CharField(max_length=200)
	descricao = models.TextField(blank=True)
	status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDENTE)
	criado_em = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = "Tarefa"
		verbose_name_plural = "Tarefas"

	def __str__(self):
		return self.titulo
