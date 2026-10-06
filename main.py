import string

from dotenv import load_dotenv
import os

from google import genai
from google.genai import types

load_dotenv()  # carrega o conteúdo do .env pra "dentro" do ambiente
chave = os.getenv("GEMINI_API_KEY")  # pega o valor da variável

client = genai.Client(api_key=chave)

termos_dificeis = {
    "pusilânime":"covarde",
    "rescindir": "cancelar",
    "pundonor": "orgulho ",
    "inócuo": "inofensivo",
    "locador": "dono do imóvel"
}

def simplifica(texto):
    return revisorIa(substitui(texto))


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

def revisorIa (texto):
    response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=texto,
    config=types.GenerateContentConfig(
        system_instruction= "Você é um revisor de textos . Você vai receber uma frase e deve tornar ela coerente. Mude as palavras que " \
"ainda soarem formais/difíceis para serem coerentes com o tom simples do texto. Não invente informações que não estavam no " \
"texto original nem mudar seu contexto ou adicionar opinião. Na resposta, quero apenas a frase simplificada e coerente"

    )
)
    return response.text


#testes
print(simplifica("O Locador rescinde o contrato."))
print(simplifica("Isso é pusilânime e inócuo."))
