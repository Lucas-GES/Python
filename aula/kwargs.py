# Exemplo de kwargs

def format(template, **kwargs):
    """Substitui as chaves de kwargs em template e retorna a string
    resultante.
    """
    for termo, substituto in kwargs.items():
        template = template.replace(termo, substituto)

    return template
