colores_claros = ["blanco", "beige", "celeste", "rosa", "amarillo"]

def es_tono_claro(color):
  return color in colores_claros
  
def tiene_contraste(letra, fondo):
  return es_tono_claro(letra) != es_tono_claro(fondo)