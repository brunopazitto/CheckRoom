import requests
import time
import pygame

def play_mp3(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)

def sound():
    file_path = "som/notificacao.mp3"
    play_mp3(file_path)

def check_for_updates():
    # Faça uma solicitação para a API para verificar atualizações
    response = requests.get('https://nextplusapi.nextplus.com.br/api/filatendimento/numeropessoasnafila')
    data = response.json()
    # Verifique se houve alguma atualização
    if data > 0 and data == 1:
        # Se houver uma atualização, execute o bloco de código desejado
        print("Houve uma atualização na API:", data)
        sound()
        # Coloque aqui o seu bloco de código para lidar com a atualização

def main():
    while True:
        check_for_updates()
        # Espere um tempo antes de fazer a próxima verificação
        time.sleep(60)  # Por exemplo, verifica a cada minuto

if __name__ == "__main__":
    main()


""" 
import requests
import pygame
import time
import threading

requisicao = requests.get('https://nextplusapi.nextplus.com.br/api/filatendimento/numeropessoasnafila')
requisicao_dic = requisicao.json()
print(requisicao_dic)


def play_mp3(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)

def main():
    file_path = "som/notificacao.mp3"
    play_mp3(file_path)


if requisicao_dic > 0:
    main() """
