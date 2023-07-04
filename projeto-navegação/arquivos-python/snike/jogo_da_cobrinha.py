import pygame 
from pygame.locals import * 
from sys import exit 
from random import randint 

# Configurações da tela 
TELA_LARGURA = 640
TELA_ALTURA = 480
x = TELA_ALTURA/2
y = TELA_LARGURA/2
# Musica 
pygame.mixer.init()
musica_moeda = pygame.mixer.Sound('musica_coin.wav')
tela = pygame.display.set_mode((TELA_LARGURA,TELA_ALTURA))
pygame.font.init()
fonte = pygame.font.SysFont('arial',20,False,True)
# Função de um unico jogador 
def jogador_1():
    x_cobra = TELA_LARGURA/2
    y_cobra = TELA_ALTURA/2
    pontos = 0 
    TELA_JODADOR_LARGURA = 640 
    TELA_JOGADOR_ALTURA = 480
    tela_jogador_1 = pygame.display.set_mode((TELA_JODADOR_LARGURA,TELA_JOGADOR_ALTURA))
    frames = pygame.time.Clock()
    velocidade = 10
    x_maça = randint(50,610)
    y_maça = randint(40,430)
    pygame.font.init()
    fonte = pygame.font.SysFont('gabriola',20,True,True)
    # Função para aumenta a cobra 
    lista_cobra = []
    comprimento_inicial = 2
    # Variavel reponsavel por movimentação da cobra mesmo parada 
    # Variaveis tambem reponsavel por não deixa a cobra se mover nas diagonais
    x_controle = 20 
    y_controle = 0    
    def aumenta_cobrinha(lista_cobra):
        # Loop responsavel por criar novos bloquinho a cada interação da cobra com a maça
        # o loop irá pega os valores [ X ] e [ Y ] da cobrinha 
        for cont in lista_cobra:
            cobra = pygame.draw.rect(tela_jogador_1,(255,255,255),(cont[0],cont[1],20,20))
    while True:
        msg = f'PONTOS {pontos}'
        render = fonte.render(msg,True,(0,255,0))
        frames.tick(20)
        tela.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_a:
                    x_controle = -velocidade
                    y_controle = 0
                if event.key == K_d:
                    x_controle = velocidade
                    y_controle = 0
                if event.key == K_w:
                    y_controle = -velocidade
                    x_controle = 0
                if event.key == K_s:
                    y_controle = velocidade
                    x_controle = 0
        if pygame.key.get_pressed()[K_a]:
            x_controle = -velocidade
            y_controle = 0
        if pygame.key.get_pressed()[K_d]:
            x_controle = velocidade
            y_controle = 0
        if pygame.key.get_pressed()[K_w]:
            y_controle = -velocidade
            x_controle = 0
        if pygame.key.get_pressed()[K_s]:
            y_controle = velocidade
            x_controle = 0
        x_cobra += x_controle
        y_cobra += y_controle
        cobra = pygame.draw.rect(tela_jogador_1,(255,255,255),(x_cobra,y_cobra,20,20))
        maça = pygame.draw.rect(tela_jogador_1,(255,0,0),(x_maça,y_maça,20,20))
        x_azul = TELA_LARGURA /2            
        y_azul = TELA_ALTURA /2
        velocidade_obs = 20 
        # Movimentação da cobra mesmo parada 
        if cobra.colliderect(maça):
            x_maça = randint(50,610)
            y_maça = randint(40,430)
            pontos += 1 
            comprimento_inicial += 1 
            musica_moeda.play()
        tela.blit(render,(450,30))
        lista_cabeça = []
        lista_cabeça.append(x_cobra)
        lista_cabeça.append(y_cobra)
        lista_cobra.append(lista_cabeça)
        # Função chamada 
        aumenta_cobrinha(lista_cobra)
        # Condição responsavel para reniciar o jogo 
        if x_cobra > 640:
            break
        if y_cobra > 480:
            break
        if y_cobra < -10 :
            break
        if x_cobra < -10:
            break
        if lista_cobra.count(lista_cabeça) > 1 :
            break
        if len(lista_cobra) > comprimento_inicial:
            del(lista_cobra[0])

        pygame.display.update()
# Função para dois jogadores 
def dois_jogadores():
    pontos_1 = 0
    pontos_2 = 0
    frames = pygame.time.Clock()
    TELA_LARGURA = 640
    TELA_ALTURA = 480 
    tela_jogador_2 = pygame.display.set_mode((TELA_LARGURA,TELA_ALTURA))
    x_jogador_1 = randint(50,610)
    y_jogador_1 = randint(40,430)
    # Jogador dois 
    x_jogador_2 = randint(30,610)
    y_jogador_2 = randint(40,430)
    velocidade = 7
    # Variavel da maça 
    x_maça = randint(40,610)
    y_maça = randint(50,430)
    x_controle = 20 
    y_controle = 0 
    # Segundo jogador 
    x2_controle = 10 
    y2_controle = 0
    comprimento_1 = 2
    comprimento_2 = 2 
    lista_cobras = []
    lista_cobras_2 = []
    def aumenta_1(lista_cobra):
        for cont in lista_cobra:
            jogador_1 = pygame.draw.rect(tela_jogador_2,(0,255,0),(cont[0],cont[1],20,20))
    def aumenta_2(lista_cobra):
        for cont in lista_cobra:
            jogador_2 = pygame.draw.rect(tela_jogador_2 , (0,0,255),(cont[0],cont[1],20,20))
    while True:
        frames.tick(17)
        tela.fill((0,0,0))
        pygame.font.init()
        fonte_1 = pygame.font.SysFont('gabriola',15,True,True)
        mensagem_1 = f'PONTOS DO JOGADOR 1: {pontos_1}'
        render_jogador_1 = fonte_1.render(mensagem_1,True,(0,255,0))
        # Segunda renderização 
        font_2 = pygame.font.SysFont('gabriola',15,True,True)
        mensagem_2 = f'PONTOS DO JOGADOR 2: {pontos_2}'
        render_jogador_2 = font_2.render(mensagem_2,True,(0,0,255))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_a:
                    x_jogador_1 -= velocidade 
                if event.key == K_d:
                    x_jogador_1 += velocidade 
                if event.key == K_w:
                    y_jogador_1 -= velocidade
                if event.key == K_s:
                    y_jogador_1 += velocidade
            # Movimentação do segundo jogador 
                if event.key == K_RIGHT:
                    x_jogador_2 += velocidade
                if event.key == K_LEFT:
                    x_jogador_2 -= velocidade 
                if event.key == K_UP:
                    y_jogador_2 -= velocidade 
                if event.key == K_DOWN:
                    y_jogador_2 += velocidade
        if pygame.key.get_pressed()[K_a]:
            x_controle = -velocidade
            y_controle = 0
        if pygame.key.get_pressed()[K_d]:
            x_controle = velocidade
            y_controle = 0
        if pygame.key.get_pressed()[K_w]:
            y_controle = -velocidade
            x_controle = 0
        if pygame.key.get_pressed()[K_s]:
            y_controle = velocidade
            x_controle = 0
        # Segundo jogador 
        if pygame.key.get_pressed()[K_LEFT]:
            x2_controle = -velocidade
            y2_controle = 0
        if pygame.key.get_pressed()[K_RIGHT]:
            x2_controle = velocidade
            y2_controle = 0
        if pygame.key.get_pressed()[K_UP]:
            y2_controle = -velocidade
            x2_controle = 0
        if pygame.key.get_pressed()[K_DOWN]:
            y2_controle = velocidade
            x2_controle = 0
        x_jogador_1 += x_controle
        y_jogador_1 += y_controle
        x_jogador_2 += x2_controle
        y_jogador_2 += y2_controle
        pygame.mixer.init()
        musica = pygame.mixer.Sound('musica_coin.wav')
        jogador_1 = pygame.draw.rect(tela_jogador_2,(0,255,0),(x_jogador_1,y_jogador_1,20,20))
        jogador_2 = pygame.draw.rect(tela_jogador_2,(0,0,255),(x_jogador_2,y_jogador_2,20,20))
        maça = pygame.draw.rect(tela_jogador_2,(255,0,0),(x_maça,y_maça,20,20))
        if jogador_1.colliderect(maça):
            x_maça = randint(50,610)
            y_maça = randint(40,410)
            pontos_1 += 1 
            comprimento_1 += 1 
            musica.play()
        # Colisão do segundo jogador 
        if jogador_2.colliderect(maça):
            x_maça = randint(50,610)
            y_maça = randint(40,410)
            pontos_2 += 2 
            comprimento_2 += 1
            musica.play() 
        # Colisão entre os dois jogadores 
        if jogador_1.colliderect(jogador_2) or jogador_2.colliderect(jogador_1):
            break
        if x_jogador_1 > 640:
            break
        if y_jogador_1 > 480:
            break
        # Negativo jogador 1 
        if x_jogador_1 < -10:
            break
        if y_jogador_1 < -10:
            break
        # Segundo jogandor 
        if x_jogador_2 > 640:
            break
        if y_jogador_2 > 480:
            break
        if x_jogador_2 < -10:
            break
        if y_jogador_2 < -10:
            break
        lista_jogador1 = []
        lista_jogador1.append(x_jogador_1)
        lista_jogador1.append(y_jogador_1)
        lista_cobras.append(lista_jogador1)
        tela_jogador_2.blit(render_jogador_1,(20,20))
        tela_jogador_2.blit(render_jogador_2,(450,30))
        # Lista do segundo jogador 
        lista_jogador_2 = []
        lista_jogador_2.append(x_jogador_2)
        lista_jogador_2.append(y_jogador_2)
        lista_cobras_2.append(lista_jogador_2)
        aumenta_2(lista_cobras_2)
        if len(lista_cobras) > comprimento_1:
            del lista_cobras[0]
        if len(lista_cobras_2) > comprimento_2:
            del lista_cobras_2[0]
        aumenta_1(lista_cobras)
        if lista_cobras.count(lista_jogador1) > 1:
            break
        if lista_cobras_2.count(lista_jogador_2) > 1 :
            break
        pygame.display.update()
# Parte principal do jogo 
x_incial = TELA_ALTURA/2
y_inicial = TELA_LARGURA/2
frames = pygame.time.Clock()
velocidade = 20
while True:
    frames.tick(20)
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_1:
                jogador_1()
            if event.key == K_2:
                dois_jogadores()
    verde = pygame.draw.rect(tela,(0,255,0),(x_incial,y_inicial,40,50))
    y_inicial += velocidade 
    if y_inicial >= TELA_LARGURA:
        y_inicial = 0
    mensagem = ''' 1 - Jogador [ aperte 1 ]  |  2 - jogadores [ aperte 2 ] '''
    mensagem_2 = 'MENU PRINCIPAL'
    renderização = fonte.render(mensagem,True,(255,255,255))
    render_2 = fonte.render(mensagem_2,False,(0,255,0))
    tela.blit(renderização,(20,20))
    tela.blit(render_2,(60,60))
    pygame.display.update()
