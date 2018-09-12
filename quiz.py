# -*- coding: utf-8 -*-
"""
O programa foi feito no python3

Baseado em uma lista de frases o jogador tem que acertar os espaços em branco
de uma frase gerada aleatoriamente.
A dificuldade do jogo consiste no número de espaçoes em branco e na 
possibilidade de errar ou não uma palavra.
De acordo com o nível de dificuldade e a frase gerada aleatoriamente o programa
define o número de substituições e as posições das substituições na frase.
Se o jogador acerta a frase ele tem uma pontuação de acordo com a escolha
 da dificuldade.
Em cada rodada ele é questionado qual o nível quer jogar.
O jogo pode ser finalizado pelo jogador por um comando de teclado ou
quando erra uma palavra e esgota o número de tentativas.

"""

#importação de pacotes necessários
import numpy as np 

#cria os níveis do jogo

niveis=["f","m", "d"]

#cria os espaços a serem preenchidos
espacos_em_branco=["__1__", "__2__", "__3__", "__4__", "__5__","__6__"]

# adiciona as frases do jogo

frases_brutas=     ["A César o que é de César, a Deus o que é de Deus.",
                   "Água mole, pedra dura, tanto bate até que fura.",
                   "A pressa é a inimiga da perfeição",
                   "À noite todos os gatos são pardos.",
                   "Antes só do que mal acompanhado.",
                   "As aparências enganam.",
                   "Apressado come cru e quente.",
                   "A voz do povo é a voz de Deus.",
                   "Cada macaco no seu galho.",
                   "Caiu na rede, é peixe",
                   "Casa de ferreiro, espeto de pau.",
                   "Cão que ladra não morde.",
                   "Cavalo dado não se olha os dentes",
                   "De grão em grão, a galinha enche o papo.",
                   "De médico e de louco todo mundo tem um pouco.",
                   "Devagar se vai ao longe.",
                   "Deus ajuda quem cedo madruga.",
                   "Deus escreve certo por linhas tortas.",
                   "Diz-me com quem andas e eu te direi quem és.",
                   "É dando que se recebe.",
                   "Em terra de cego quem tem olho é rei.",
                   "Escreveu, não leu; o pau comeu.",
                   "Filho de peixe, peixinho é.",
                   "Gato escaldado tem medo de água fria.",
                   "Ladrão que rouba ladrão tem cem anos de perdão.",
                   "Mais vale um pássaro na mão do que dois voando.",
                   "Mentira tem perna curta.",
                   "O barato sai caro.",
                   "O hábito faz o monge.",
                   "Onde há fumaça há fogo.",
                   "O seguro morreu de velho.",
                   "Para bom entendedor, meia palavra basta.",
                   "Para baixo todo santo ajuda.",
                   "Pimenta nos olhos dos outros é refresco.",
                   "Por ele eu ponho minha mão no fogo.",
                   "Quando os porcos bailam adivinham chuva.",
                   "Quando um burro fala, o outro abaixa a orelha.",
                   "Quem ama o feio, bonito lhe parece.",
                   "Quem canta seus males espanta.",
                   "Quem casa quer casa.",
                   "Quem com ferro fere, com ferro será ferido.",
                   "Quem mistura-se com porcos, farelo come.",
                   "Quem não tem cão, caça com gato.",
                   "Quem pode, pode; quem não pode, se sacode.",
                   "Quem ri por último ri melhor.",
                   "Quem semeia vento, colhe tempestade.",
                   "Quem tem boca vai à Roma.",
                   "Saco vazio não para em pé.",
                   "Uma andorinha sozinha não faz verão.",
                   "Um dia é da caça, outro do caçador."]

#armazena o numero de frases
numerofrases=len(frases_brutas)

#numero espacos em branco

numero_espacos=[2,3,4,5,6]

#tamanhos de frases
tamanhos_de_frases=[3,4,5,6,7]

#numero de tentativas de um nivel
tentativas_de_nivel=[3,2,1]

#pontuação de nivel
pontuacao_nivel=[1,3,5]

#cria uma lista onde são armazenadas as frases do jogo
frases_do_jogo=[]

def verificapontuacao(palavra):
    """ Dada uma palavra retorna True se a palavra contém pontuação
    ou False caso contrário.    
    """
    ultimo_simbolo=palavra[-1]
    
    if ((ultimo_simbolo==",")or(ultimo_simbolo=="."))or (ultimo_simbolo==";"):
        return True
    return False 

def frasesemlista(lista):
    """ Traansforma uma lista de strings, onde cada elemento da lista é uma
    frase em uma lista de listas, onde cada lista interna contém elementos
    que são as palavras das frases. 
    """
    listatemporaria=[]
    for frase in lista:
        listatemporaria.append(frase.split())
    return listatemporaria

def frasesemlistasemponto(lista):
    """Transforma uma lista de frases onde cada palavara é armazenda em um
    elemento da sublista, substituindo as palavras com pontuação pela palavra 
    sem pontuação.
    """
    
    listatemporaria=[]
    
    for frase in lista:
        
        listatemporaria2=[]
        for palavra in frase:
            if verificapontuacao(palavra):
                palavratemporaria=palavra[:-1]
            else:
                palavratemporaria=palavra
            listatemporaria2.append(palavratemporaria)
        listatemporaria.append(listatemporaria2)
    return listatemporaria

def instrucoes():
    """Imprime instruções iniciais sobre a partida.
    """
    print("")
    print("O objetivo do jogo é completar as palavras de uma frase...")
    print("Não se esqueça dos acentos!")
    print("Se você escolher difícil você só terá uma chance por palavra,")
    print("médio duas chances e fácil três chances.")   
    print("A escolha dos níveis também pode deixar mais espaços em branco!")
    print("Fácil são dois, médio é de dois a três e difícil é de três à seis espaços!")
    print("")
    print("Cada frase acertada no nível difícil acumula {} pontos!"\
          .format(pontuacao_nivel[2]))
    print("Cada frase acertada no nível médio acumula {} pontos!"\
          .format(pontuacao_nivel[1]))
    print("Cada frase acertada no nível fácil acumula {} ponto!"\
          .format(pontuacao_nivel[0]))
    print("Pense nas suas escolhas e boa sorte!!")
    print("")
    
def definejogador():
    """Pede ao usuário entrar com seu nome e retorna esse nome.    
    """
    nome=input("Por favor digite seu nome: ")
    return nome


def selecionar_nivel():
    
    """ Esse método permite ao jogador escolher um nível de dificuldade
    assim que o jogo é iniciado"""
    
    print("")
    nivel=input("Escolha um nível: fácil({}), médio({}), difícil({}): "\
                .format(niveis[0],niveis[1],niveis[2]).lower())
        
    while nivel not in niveis :
        print("Digite um nível válido...")
        nivel=input("Escolha um nível: fácil({}), médio({}), difícil({}): ".\
                    format(niveis[0],niveis[1],niveis[2])).lower()
            
    return nivel


def selecionafrase(lista, totalfrases):
    
    """Seleciona aleatoriamente um índice dentros dos possíveis indices de
    frases que não estão na lista(frases já utilizadas).    
    """
    indice=np.random.randint(totalfrases)
    
    while indice in lista:
        indice=np.random.randint(totalfrases)
    
    lista.append(indice)
    
    return indice


def listaemminusculo(lista,tamanhofrase):
    
    """ Dada uma lista de palavras e o seu tamanho, retorana as palavras em minusculo
    """
    for indice in range(tamanhofrase):
        lista[indice]=lista[indice].lower()
    return lista


def calculanumerosubstituicoes(nivel,frase,tamanhofrase):
    
    """ De acordo com o nível escolhido e com a frase, define o número
    de substituições que deverão ser feitas na frase. Um nível fácil 
    requer poucas substituições. Um nível difícil requer muitas substituições.
    """    
    
    
    if nivel == niveis[0]:
        return numero_espacos[0]
    if nivel == niveis[1]:
        if tamanhofrase>=tamanhos_de_frases[2]:
            return numero_espacos[1]
        else:
            return numero_espacos[0]
    if nivel == "d":
        if tamanhofrase> tamanhos_de_frases[4]:
            return numero_espacos[4]
        if tamanhofrase>tamanhos_de_frases[3]:
            return numero_espacos[3]
        elif tamanhofrase>tamanhos_de_frases[2]:
            return numero_espacos[2]
        elif tamanhofrase<=tamanhos_de_frases[2]:
            return numero_espacos[1]


def procuraposicaosubstituicao(tamanho, numero):
    
    """ Dado o tamanho de uma frase e o número de substituições 
    que serão feitas, retorna uma lista com as posições onde essas
    substituições serão feitas.    
    """
    lista=[]
    lista.append(np.random.randint(tamanho))
    
    count = 1
    posicao=np.random.randint(tamanho)
    while count < numero:
        while posicao in lista:
            posicao=np.random.randint(tamanho)
        lista.append(posicao)
        count+=1
    lista.sort()
    return lista


def listacomespacos(frase,lista,tamanho):
    """ Dado uma frase, uma lista de posicoes a serem substituidas e o tamanho da frase,
    faz as substituições por espacos em branco e armazena em uma lista.    
    """    
    
    listatemporaria=[]
    count=0
    for i in range(tamanho):
        if i in lista:
            listatemporaria.append(espacos_em_branco[count])
            count+=1
        else:
            listatemporaria.append(frase[i])
    return listatemporaria

def imprime(frasequalquer):
    """Imprime espaço de uma lina e string.
    """
    print("")
    print(frasequalquer)

def imprimedelista(lista):
    """Dada uma lista de palavras imprime a frase formada pelos elementos da lista.
    """
    print(" ".join(lista))


def verificaigualdade(palavra, posicao,frase):
    """Dada uma palavra, uma posicao e uma frase, verifica se a palavra
    esta na posicao exata da frase independente de minusculo ou maiusculo.
    """
    if palavra.lower()==frase[posicao].lower():
        return True
    return False

def numerodetentativas(dificuldade):
    """De acordo com o nível de dificuldade retorna o número de tentativas possíveis
     de acerto de uma palavra.
    """
    if dificuldade==niveis[0]:
        return tentativas_de_nivel[0]
    if dificuldade ==niveis[1]:
        return tentativas_de_nivel[1]
    if dificuldade ==niveis[2]:
        return  tentativas_de_nivel[2]   
 
       
def jogarodada(listaposicao,dificuldade,frasecomespaco,fraserodada,numerosubstituicao):
    
    """ Fase da rodada do jogo, mostra a palavra com espacos em branco,
    o jogador entra com a palavra e o programa verifica se acertou ou não,\
    caso tenha acertado
    a palavra imprime a nova frase e continua para a proxima. \
    Caso nao tenha acertado imprime a 
    frase original e repete o processo. Faz isso ate esgotar o numero de \
    tentativas ou acertar
    a frase inteira.    
    """

    tentativas = numerodetentativas(dificuldade)    
    frasesaidatemp=frasecomespaco.copy()   
    
    for i in range(numerosubstituicao):
        contatentativas=1        
        while contatentativas<=tentativas:        
            texto="Entre com a palavra "+frasecomespaco[listaposicao[i]] + " : " 
            resultado = input(texto).lower()   
            
            if verificaigualdade(resultado,listaposicao[i],fraserodada):
                frasesaidatemp[listaposicao[i]]=resultado
                contatentativas=4
                print("Você acertou, continue assim!")
                imprimedelista(frasesaidatemp)
            else:
                contatentativas+=1
                if contatentativas<=tentativas:
                    print("Você errou, tente novamente.")
                    imprimedelista(frasesaidatemp)
                else:
                    print("Você esgotou o número de tentativas!")
                    return frasesaidatemp  
                
    return frasesaidatemp
    
def resultadorodada(lista1,lista2,indice,dificuldade,pontuacao):
    """Compara duas listas de palavras, se as listas são iguais entao acertou.
    Se são diferentes errou. Retorna a pontuação depois de uma rodada\
    e se acertou ou não a frase.
    """
    
    if lista1 == lista2:
        print("")
        print("Parabéns, você acertou a frase: ")
        if dificuldade ==niveis[0]:
            pontuacao+=pontuacao_nivel[0]
        if dificuldade ==niveis[1]:
            pontuacao+=pontuacao_nivel[1]
        if dificuldade == niveis[2]:
            pontuacao+=pontuacao_nivel[2]
        print(frases_brutas[indice])
        return pontuacao,True
    else:
        print("")
        print("Você errou, que pena! A frase era: ")
        print(frases_brutas[indice])
        return pontuacao,False


def mostrapontuacao(teste):
    """Recebe os pontos do jogo que tem duas entradas, a primeira com a pontução,
    e a segunda indicando se errou ou não a frase. Caso não tenha errado a \
    frase imprime os pontos do 
    jogo. Caso tenha errado a frase não faz nada.
    """
    condicao_continuar=teste[1]
    pontosmostrar=teste[0]
    
    if condicao_continuar:
        print("Você marcou: {} pontos até agora!".format(pontosmostrar))
        print("")

def jogarnovamente(testeterminou):
    """Se errou a frase retorna falso. 
    Se acertou dependendo da entrada do usuario retorna Falso ou verdadeiro. \
    Se não digitar nada retorna 
    verdadeiro. Caso contrário retorna falso.
    """
    if testeterminou:
        texto = input("Digite enter para jogar novamente, ou qualquer outra tecla para sair: ")
        if not bool(texto):
            return True
        return False
    return False

def fimdejogo(nome,pontos):
    """Finaliza o jogo. Exibe a pontuação e o nome do jogador.
    """
    print("")
    print("Fim de jogo!")
    print("Você marcou {} pontos {}!".format(pontos,nome))



def iniciajogo():
    """
    Desenvolve todo o jogo.
    """
    instrucoes()
    condicao_continuajogo=True
    pontuacao=0
    pontos_do_jogo=[pontuacao,condicao_continuajogo]
    jogar_de_novo=True
    frases_do_jogo=frasesemlista(frases_brutas)
    frases_do_jogo=frasesemlistasemponto(frases_do_jogo)
    nome_jogador= definejogador()
    indice_frases_utilizadas=[] 
    
    while jogar_de_novo:
        nivel_do_jogo = selecionar_nivel()
        indice_frase_rodada=selecionafrase(indice_frases_utilizadas,numerofrases)
        frase_da_rodada = frases_do_jogo[indice_frase_rodada]
        tamanho_da_frase=len(frase_da_rodada)
        frase_da_rodada=listaemminusculo(frase_da_rodada,tamanho_da_frase)
        numero_substituicoes=calculanumerosubstituicoes(nivel_do_jogo,frase_da_rodada,tamanho_da_frase)
        posicao_substituicao=procuraposicaosubstituicao(tamanho_da_frase,numero_substituicoes)
        frase_com_espacos= listacomespacos(frase_da_rodada,posicao_substituicao,tamanho_da_frase)
        imprime("Sua frase é:")
        imprimedelista(frase_com_espacos)
        frase_jogada=jogarodada(posicao_substituicao,nivel_do_jogo,frase_com_espacos,frase_da_rodada,numero_substituicoes)
        pontos_do_jogo=resultadorodada(frase_da_rodada,frase_jogada,indice_frase_rodada, nivel_do_jogo,pontuacao)
        mostrapontuacao(pontos_do_jogo)
        pontuacao=pontos_do_jogo[0]
        jogar_de_novo= jogarnovamente(pontos_do_jogo[1])
        
    fimdejogo(nome_jogador,pontuacao)
        
    
    
#chama o começo de um jogo
iniciajogo()

