import pygame 
from pygame.locals import * 
from sys import exit 
from random import randint,choice
# Lista de perguntas 
lista_perguntas = ['Qual o maior planeta do sistema solar ? ','Qual a formula da agua ? ','Qual o maior continente do planeta ? ']
pergunta_aletoria = choice(lista_perguntas)
# Configuração da tela 
TELA_LARGURA = 640 
TELA_ALTURA = 480 
tela = pygame.display.set_mode((TELA_LARGURA,TELA_ALTURA))

# Titulo da tela 
pygame.display.set_caption('QUIZ PERGUNTAS')
# Fonte do jogo 
pygame.font.init()
fonte = pygame.font.SysFont('gabriola',20,False,True)
# Função principal
def jogo():
    global VIDAS
    # Lista de perguntas 
    lista_perguntas = ['Qual o maior planeta do sistema solar ? ','Qual a formula da agua ? ','Qual o maior continente do planeta ? ']
    pergunta_aletoria = choice(lista_perguntas)
    pergunta_aletoria = lista_perguntas[0]
    # Configuração da tela 
    TELA_LARGURA = 640 
    TELA_ALTURA = 480 
    # Variavel do rect_time 
    x_time = 50 
    y_time = 400
    tela = pygame.display.set_mode((TELA_LARGURA,TELA_ALTURA))
    # Variavel responsavel pelo tempo 
    tempo = 0 

    # Titulo da tela 
    pygame.display.set_caption('QUIZ PERGUNTAS')
    VIDAS = 5
    # Fonte do jogo 
    pygame.font.init()
    fonte = pygame.font.SysFont('gabriola',20,False,True)
    tempo = 0 
    while True:
        tela.fill((0,0,0))
        resposta = 'ESPERANDO REPOSTA...'
        render_reposta = fonte.render(resposta,True,(255,255,255))
        tela.blit(render_reposta,(230,10))
        # Evento do jogos 
        for cont in pygame.event.get():
            if cont.type == QUIT:
                pygame.quit()
                exit()
        renderezição = fonte.render(f'VIDAS: {VIDAS} ',True,(255,255,0))
        pergunta_render = fonte.render(pergunta_aletoria,True,(255,255,255))
        tempo_render = fonte.render(f'TIME : {tempo}',True,(0,255,0))
        rect_time = pygame.draw.rect(tela,(255,0,0),(x_time,y_time,10,10))
        tela.blit(tempo_render,(250,350))
        x_time += 2
        if x_time > 640:
            x_time = 0
            tempo += 1
            if tempo == 10:
                derrota_tela = pygame.display.set_mode((640,480))
                while True:
                    for cont in pygame.event.get():
                        if cont.type == QUIT:
                            pygame.quit()
                            exit()
                        if cont.type == KEYDOWN:
                            if cont.key == K_1:
                                reniciar_jogo()
                    derrota_msg = fonte.render('VOCÊ PERDEU,Pressione [ 1 ] para tenta novamente ',True,(255,255,255))
                    derrota_tela.blit(derrota_msg,(60,60))
                    pygame.display.flip() 
        if pergunta_aletoria == lista_perguntas[0]:
            alternativa_a = '( A ) - JUPITER'
            render_a = fonte.render(alternativa_a,True,(255,255,255))
            alternativa_b = '( B ) - SATURNO'
            render_b = fonte.render(alternativa_b,True,(255,255,255))
            alternativa_c = '( C ) - MERCUIO'
            render_c = fonte.render(alternativa_c,True,(255,255,255))
            alternativa_d = '( D ) - PLUTÃO'
            render_d = fonte.render(alternativa_d,True,(255,255,255))
            alternativa_e = '( E ) - NENHUMAS ACIMA'
            tela.blit(render_a,(50,130))
            tela.blit(render_b,(50,170))
            tela.blit(render_c,(50,210))
            tela.blit(render_d,(50,245))
            tela.blit(renderezição,(430,30))
            if pygame.key.get_pressed()[K_a]:
                resposta = 'VOCÊ ACERTOU'
                render_reposta = fonte.render('VOCÊ ACERTOU',True,(255,255,0))
                VIDAS += 1 
                tela.blit(render_reposta,(230,10))
                reniciar_jogo()
            if pygame.key.get_pressed()[K_b]:
                VIDAS -= 1 
                derrota_jogo()
        tela.blit(pergunta_render,(60,60))
        pygame.display.flip()
# Funçaõ para reniciar jogo 
def reniciar_jogo():
    jogo()
def derrota_jogo():
    pygame.font.init()
    derrota_fonte = pygame.font.SysFont('arial',20,True,True)
    derrota_tela = pygame.display.set_mode((640,480))
    derrota_render = derrota_fonte.render('VOCÊ PERDEU,PRESSIONE [ 1 ] PARA TENTA DE NOVO',True,(0,0,0))
    while True:
        tela.fill((255,0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_1:
                    reniciar_jogo()
        tela.blit(derrota_render,(60,50))
        
        pygame.display.flip()

# Função acertou 
        
jogo()

