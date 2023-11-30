# exemplo
def concatenar(**kwargs):
    resultado = ""
    for key in kwargs:
        resultado += f"{kwargs[key]} "
    return resultado
    
    
print(concatenar(a="oi", b="mano", c="tudo", d="bem?"))