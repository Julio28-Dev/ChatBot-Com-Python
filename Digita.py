import speech_recognition as sr  #captação de voz
import pyttsx3  #falar computador
import difflib #comparar strings

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Diga algo...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        text = recognizer.recognize_google(audio, language='pt-BR')
        print("Você disse: " + text)
        return text.lower()
    except sr.UnknownValueError:
        print("Não entendi o que você disse.")
        return ""
    except sr.RequestError:
        print("Erro ao conectar com o serviço de reconhecimento de voz.")
        return ""

def chatbot_responder(comando):
    respostas = {
        "ola": "Olá! Como posso ajudar você hoje?",
        "tudo bem": "Tudo ótimo, obrigado por perguntar!",
        "qual seu nome": "Eu sou a sexta-feira, sua assistente virtual.",
        "o que voce pode fazer": "Posso ajudar com várias tarefas, como responder perguntas e fornecer informações.",
        "adeus": "Até mais! Tenha um ótimo dia!",
        "sair": "Até mais! Tenha um ótimo dia!" 
    }

    if not comando.strip():
        return "Não entendi o que você disse."

    # Tenta encontrar a frase mais parecida
    chave_parecida = difflib.get_close_matches(comando, respostas.keys(), n=1, cutoff=0.6)

    if chave_parecida:
        return respostas[chave_parecida[0]]

    # Se não encontrar, procura se alguma parte da chave está no comando
    for key in respostas.keys():
        if key in comando:
            return respostas[key]

    return "Você é gostoso!"

if __name__ == "__main__":
    speak("Olá! Me chamo sexta-feira. Como posso ajudar hoje?")
    while True:
        comando = listen()
        if "sair" in comando or "adeus" in comando:
            speak("Até mais!")
            break
        resposta = chatbot_responder(comando)
        print("Chatbot: " + resposta)
        speak(resposta)
