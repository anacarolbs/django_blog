from django.apps import AppConfig

# Define a configuração do aplicativo `blog`.
class BlogConfig(AppConfig):
    # Define o tipo padrão de campo de chave primária para os modelos do aplicativo.
    # `BigAutoField` é usado para gerar IDs automáticos como inteiros grandes.
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Define o nome do aplicativo. Este nome deve corresponder ao diretório do aplicativo.
    name = 'blog'
