#entrega 2 - 3 filtros
# define filtros personalizados para serem usados nos templates do Django.

""" Explicação dos Filtros utilizados no index.html:
1- Filtro truncate_chars:
Aplicado ao título do post (post.title) para truncar em até 50 caracteres.
Aplicado ao corpo do post (post.body) para truncar em até 400 caracteres.

2- Filtro format_date:
Aplicado à data de criação do post (post.created_on) para formatá-la como DD/MM/AAAA.

3- Filtro to_uppercase:
Aplicado ao nome das categorias (category.name) para exibi-las em letras maiúsculas.

Resultado Esperado:
Os títulos e conteúdos dos posts serão truncados para evitar textos muito longos.
As datas serão exibidas no formato DD/MM/AAAA.
Os nomes das categorias aparecerão em letras maiúsculas."""

from django import template

# Cria uma instância de biblioteca de filtros para registrar os filtros personalizados.
register = template.Library()

#filtro 1 - Trunca o texto para o número de caracteres especificado.
@register.filter
def truncate_chars(value, num): 
    """ Trunca o texto para o número de caracteres especificado.
        - value: O texto a ser truncado.
        - num: O número máximo de caracteres permitidos. """
    if len(value) > num:
        # Retorna o texto truncado com "..." no final, se exceder o limite.
        return value[:num] + "..."
    # Retorna o texto original, se não exceder o limite.
    return value

#filtro 2 - Formata a data no formato DD/MM/AAAA.
@register.filter
def format_date(value):
    """Formata a data no formato DD/MM/AAAA.
    - value: O objeto de data a ser formatado."""
    # Converte a data para o formato desejado.
    return value.strftime("%d/%m/%Y")

#filtro 3 - Converte o texto para letras maiúsculas.
@register.filter
def to_uppercase(value):
    """Converte o texto para letras maiúsculas.
    - value: O texto a ser convertido."""
    # Retorna o texto em letras maiúsculas.
    return value.upper()