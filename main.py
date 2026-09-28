import string

termos_dificeis = {
    "pusilânime":"covarde",
    "rescindir": "cancelar",
    "pundonor": "orgulho ",
    "inócuo": "inofensivo",
    "locador": "dono do imóvel"
}

def simplifica(texto):
    return mock_ia(substitui(texto))


def substitui(texto):
    palavras = texto.split()
    
    resultado = []
    for palavra in palavras:
        palavra = palavra.lower()
        palavra = palavra.strip(string.punctuation)
        
        if palavra in termos_dificeis:
            palavra = termos_dificeis[palavra]
        
        resultado.append(palavra)
        
    frase = " ".join(resultado)
    return frase

def mock_ia (texto):
    print("Simulando IA..")
    return texto
    
    
#testes
print(simplifica("O Locador rescinde o contrato."))
print(simplifica("Isso é pusilânime e inócuo."))