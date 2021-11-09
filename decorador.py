def anunciar(f):
    def wrapper():
        print("rodando a função...")
        f()
        print("terminando a função")
    return wrapper 

@anunciar
def capivara():
    print("capivara, world")

capivara()