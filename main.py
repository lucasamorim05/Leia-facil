termos_dificeis = {
    "pusilânime":"covarde",
    "rescindir": "cancelar",
    "pundonor": "orgulho ",
    "inócuo": "inofensivo",
    "locador": "dono do imóvel"
}

def simplifica(texto):
    palavras = texto.split()
    
    resultado = []
    for palavra in palavras:
        palavra = palavra.lower()
        palavra = palavra.strip(",")
        
        if palavra in termos_dificeis:
            palavra = termos_dificeis[palavra]
        
        resultado.append(palavra)
        
    frase = " ".join(resultado)
    return frase

print(simplifica("ele vai rescindir o contrato"))