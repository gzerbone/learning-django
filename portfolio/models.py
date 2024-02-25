from django.contrib.auth.models import \
    User  # User também é uma tabela na base de dados
from django.db import models


# Imaginar models como tabelas da base de dados.
class Category(models.Model):
    name = models.CharField(max_length = 65)

    # FAz retornar o nome das categorias lá pagina "admin" ao inves de aparecer object(1)
    def __str__(self):
        return self.name


class Portfolio(models.Model):
    title = models.CharField(max_length = 65)
    description = models.CharField(max_length = 165)
    slug = models.SlugField()
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    project_detail = models.TextField()
    project_detail_is_html = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True) #auto_now_add = gera uma data no momento da criação
    updated_at = models.DateTimeField(auto_now = True) #auto_now = atualiza o campo mudado
    is_published = models.BooleanField(default = False)
    cover = models.ImageField(upload_to='portfolio/covers/%y/%m/%d/' ,blank=True, default='')

    #RELAÇÃO ENTRE TABELAS

    #Se algum tipo de categoria for excluida, esse campo tbm será. Ao ser excluido o campo será setado com NULL
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True,blank=True, default= None) 

    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 

    def __str__(self):
        return self.title