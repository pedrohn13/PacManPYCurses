#Roteiro de Projeto 3, Laboratorio de Programacao 1, UFCG.
#Jogo PACMAN, feito no modulo curses de Python
#Desenvolvedor: Pedro Henriques Neto (21111114)

import curses
import random
import time

#recebe o nome do jogador
player = raw_input('DIGITE O NOME DO JOGADOR: ').upper()

#tenta abrir o arquivo com o recorde
try:
	arq = open("recordpacman.txt","r")
	r = arq.read().split(',')
	arq.close()

except IOError:
	arq = open("recordpacman.txt","w")
	arq.write("NINGUEM,0")
	arq.close()
	r = ["NINGUEM","0"]

#estrutura de dados
vidas = [3]
pontuacao = [0]
pacman = [12,23]
fantasma1 = [10,28,1]
fantasma2 = [10,29,1]
fantasma3 = [10,30,1]
fantasma4 = [10,31,1]
estado = ['forte']
sentido = ['X']
labirinto = []
contador = 0
hit = [0]
fase = [0]
speed = 0.21
extra = 0
#lista onde vao ficar os pontos que o pacman vai comer
pontos = []
superpontos = [[1,3],[19,3],[1,57],[19,57]]
#lista onde vai ficar as coordenadas dos pontos onde nao pode aparecer comida
crit = []


#gera fase1
def gerafase1():
	for c in range(23,29):
		labirinto.append([8,c])
	for c in range(31,37):
		labirinto.append([8,c])
	for c in range(23,37):
		labirinto.append([11,c])
	for c in range(8,12):
		labirinto.append([c,23])
		labirinto.append([c,24])
		labirinto.append([c,36])
		labirinto.append([c,37])
	for c in range(61):
		labirinto.append([0,c])
		labirinto.append([20,c])
	for c in range(9):
		labirinto.append([c,0])
		labirinto.append([c,1])
		labirinto.append([c,59])
		labirinto.append([c,60])
	for c in range(10,21):
		labirinto.append([c,0])
		labirinto.append([c,1])
		labirinto.append([c,59])
		labirinto.append([c,60])
	for c in range(3,10):
		for d in range(2,7):
			labirinto.append([d,c])
		for d in range(8,12):
			labirinto.append([d,c])
		for d in range(13,19):
			labirinto.append([d,c])
	for c in range(11,22):
		for d in range(2,7):
			labirinto.append([d,c])
		for d in range(8,12):
			labirinto.append([d,c])
		for d in range(13,19):
			labirinto.append([d,c])
	for c in range(23,38):
		for d in range(2,7):
			labirinto.append([d,c])
		for d in range(13,19):
			labirinto.append([d,c])
	for c in range(39,50):
		for d in range(2,7):
			labirinto.append([d,c])
		for d in range(8,12):
			labirinto.append([d,c])
		for d in range(13,19):
			labirinto.append([d,c])
	for c in range(51,58):
		for d in range(2,7):
			labirinto.append([d,c])
		for d in range(8,12):
			labirinto.append([d,c])
		for d in range(13,19):
			labirinto.append([d,c])
#gera fase2
def gerafase2():
	for c in range(23,29):
		labirinto.append([8,c])
	for c in range(31,37):
		labirinto.append([8,c])
	for c in range(23,37):
		labirinto.append([11,c])
	for c in range(8,12):
		labirinto.append([c,23])
		labirinto.append([c,24])
		labirinto.append([c,36])
		labirinto.append([c,37])
	for c in range(61):
		labirinto.append([0,c])
		labirinto.append([20,c])
	for c in range(9):
		labirinto.append([c,0])
		labirinto.append([c,1])
		labirinto.append([c,59])
		labirinto.append([c,60])
	for c in range(10,20):
		labirinto.append([c,0])
		labirinto.append([c,1])
		labirinto.append([c,59])
		labirinto.append([c,60])
	for c in range(2,7):
		labirinto.append([c,3])
		labirinto.append([c,4])
		labirinto.append([c,56])
		labirinto.append([c,57])
	for c in range(13,19):
		labirinto.append([c,3])
		labirinto.append([c,4])
		labirinto.append([c,56])
		labirinto.append([c,57])
	for c in range(1,5):
		labirinto.append([c,6])
		labirinto.append([c,7])
		labirinto.append([c,53])
		labirinto.append([c,54])
	for c in range(15,20):
		labirinto.append([c,6])
		labirinto.append([c,7])
		labirinto.append([c,53])
		labirinto.append([c,54])
	for c in range(9,52):
		labirinto.append([2,c])
		labirinto.append([17,c])
		labirinto.append([18,c])
	for c in range(5,56):
		labirinto.append([6,c])
		labirinto.append([13,c])
	for c in range(8,29):
		labirinto.append([4,c])
		labirinto.append([15,c])
	for c in range(31,53):
		labirinto.append([4,c])
		labirinto.append([15,c])
	for c in range(8,12):
		for d in range(3,22):
			labirinto.append([c,d])
		for d in range(39,58):
			labirinto.append([c,d])

#gera fase3
def gerafase3():
	labirinto.append([13,6])
	labirinto.append([13,7])
	labirinto.append([13,52])
	labirinto.append([13,53])
	for c in range(60):
		labirinto.append([0,c])
		labirinto.append([20,c])
	for c in range(9):
		labirinto.append([c,0])
		labirinto.append([c,1])
		labirinto.append([c,59])
		labirinto.append([c,60])
	for c in range(10,21):
		labirinto.append([c,0])
		labirinto.append([c,1])
		labirinto.append([c,59])
		labirinto.append([c,60])
	for c in range(3,14):
		labirinto.append([2,c])
		labirinto.append([17,c])
		labirinto.append([18,c])
	for c in range(18,28):
		labirinto.append([2,c])
		labirinto.append([17,c])
		labirinto.append([18,c])
	for c in range(32,42):
		labirinto.append([2,c])
		labirinto.append([17,c])
		labirinto.append([18,c])
	for c in range(46,58):
		labirinto.append([2,c])
		labirinto.append([17,c])
		labirinto.append([18,c])
	for c in range(11,22):
		labirinto.append([7,c])
		labirinto.append([12,c])
	for c in range(38,49):
		labirinto.append([7,c])
		labirinto.append([12,c])
	for c in range(23,29):
		labirinto.append([8,c])
	for c in range(31,37):
		labirinto.append([8,c])
	for c in range(23,37):
		labirinto.append([4,c])
		labirinto.append([6,c])
		labirinto.append([11,c])
		labirinto.append([13,c])
		labirinto.append([15,c])
	for c in range(6,14):
		labirinto.append([4,c])
		labirinto.append([5,c])
		labirinto.append([14,c])
		labirinto.append([15,c])
	for c in range(15,19):
		labirinto.append([4,c])
		labirinto.append([5,c])
		labirinto.append([14,c])
		labirinto.append([15,c])
	for c in range(41,45):
		labirinto.append([4,c])
		labirinto.append([5,c])
		labirinto.append([14,c])
		labirinto.append([15,c])
	for c in range(46,54):
		labirinto.append([4,c])
		labirinto.append([5,c])
		labirinto.append([14,c])
		labirinto.append([15,c])
	for c in range(11,22):
		labirinto.append([9,c])
		labirinto.append([10,c])
	for c in range(38,49):
		labirinto.append([9,c])
		labirinto.append([10,c])
	for c in range(1,4):
		labirinto.append([c,15])
		labirinto.append([c,16])
		labirinto.append([c,29])
		labirinto.append([c,30])
		labirinto.append([c,43])
		labirinto.append([c,44])
	for c in range(16,20):
		labirinto.append([c,15])
		labirinto.append([c,16])
		labirinto.append([c,29])
		labirinto.append([c,30])
		labirinto.append([c,43])
		labirinto.append([c,44])
	for c in range(6,14):
		labirinto.append([c,8])
		labirinto.append([c,9])
		labirinto.append([c,50])
		labirinto.append([c,51])
	for c in range(4,7):
		labirinto.append([c,20])
		labirinto.append([c,21])
		labirinto.append([c,38])
		labirinto.append([c,39])
	for c in range(13,16):
		labirinto.append([c,20])
		labirinto.append([c,21])
		labirinto.append([c,38])
		labirinto.append([c,39])
	for c in range(3,6):
		labirinto.append([c,3])
		labirinto.append([c,4])
		labirinto.append([c,55])
		labirinto.append([c,56])
		labirinto.append([c,57])
	for c in range(13,17):
		labirinto.append([c,3])
		labirinto.append([c,4])
		labirinto.append([c,55])
		labirinto.append([c,56])
		labirinto.append([c,57])
	for c in range(2,7):
		labirinto.append([7,c])
		labirinto.append([8,c])
		labirinto.append([10,c])
		labirinto.append([11,c])
	for c in range(53,59):
		labirinto.append([7,c])
		labirinto.append([8,c])
		labirinto.append([10,c])
		labirinto.append([11,c])
	for c in range(9,12):
		labirinto.append([c,23])
		labirinto.append([c,24])
		labirinto.append([c,35])
		labirinto.append([c,36])
		

#gera pontos criticos, onde nao pode aparecer pontos
crit.append([8,29])
crit.append([8,30])
for c in range(23,37):
	crit.append([9,c])
	crit.append([10,c])

#gera pontos a comer
def gerapontos():
	for c in range(61):
		for d in range(20):
			if [d,c] not in crit:
				if [d,c] not in labirinto:
					if [d,c] not in superpontos:
						pontos.append([d,c])
		
#desenha tela
def tela(scr):
	global pacman,labirinto,pontos,player,pontuacao,vidas,recorde,fantasma1,fantasma2,fantasma3,fantasma4

	scr.addstr(1,62,"--==[PACMAN]==--")
	scr.addstr(2,64,"-=[FASE %d]=-" % fase[0])
	scr.addstr(4,62,"[JOGADOR]=-------")
	scr.addstr(5,62,"%s" % player)
	scr.addstr(7,62,"[VIDAS]=---------")
	scr.addstr(8,62,"%d" % vidas[0])
	scr.addstr(10,62,"[PONTUACAO]=-----")
	scr.addstr(11,62,"%08d" % pontuacao[0])
	scr.addstr(13,62,"[RECORDE]=-------")
	scr.addstr(14,62,"%s - %s " % (r[0],r[1]))
	scr.addstr(16,64,"[P] - PAUSA")
	scr.addstr(17,64,"[Q] - SAIR")

	for coor in pontos:
		scr.addch(coor[0],coor[1],"-")
	for co in superpontos:
		scr.addch(co[0],co[1],"$")
	for coo in labirinto:
		scr.addch(coo[0],coo[1]," ",curses.A_REVERSE)

	if estado[0] == 'forte':
		curses.init_pair(1,1,curses.COLOR_BLACK)
		scr.addch(fantasma1[0],fantasma1[1],"M",curses.color_pair(1))
		scr.addch(fantasma2[0],fantasma2[1],"M",curses.color_pair(1))
		scr.addch(fantasma3[0],fantasma3[1],"M",curses.color_pair(1))
		scr.addch(fantasma4[0],fantasma4[1],"M",curses.color_pair(1))
	elif estado[0] == 'fraco':
		curses.init_pair(6,6,curses.COLOR_BLACK)
		scr.addch(fantasma1[0],fantasma1[1],"m",curses.color_pair(6))
		scr.addch(fantasma2[0],fantasma2[1],"m",curses.color_pair(6))
		scr.addch(fantasma3[0],fantasma3[1],"m",curses.color_pair(6))
		scr.addch(fantasma4[0],fantasma4[1],"m",curses.color_pair(6))	

	curses.init_pair(3,3,curses.COLOR_BLACK)
	scr.addch(pacman[0],pacman[1],"@",curses.color_pair(3))

	scr.refresh()

#movimentos do pacman
def move_direita():
	global pacman,labirinto
	coluna = (pacman[1] + 1) % 61
	if not [pacman[0],coluna] in labirinto:
		pacman[1] = coluna
		sentido[0] = '>'

def move_esquerda():
	global pacman,labirinto
	coluna = (pacman[1] - 1) % 61
	if not [pacman[0],coluna] in labirinto:
		pacman[1] = coluna
		sentido[0] = '<'

def move_acima():
	global pacman,labirinto
	linha = (pacman[0] - 1) % 21
	if not [linha,pacman[1]] in labirinto:
		pacman[0] = linha
		sentido[0] = '^'

def move_abaixo():
	global pacman,labirinto
	linha = (pacman[0] + 1) % 21
	if not [linha,pacman[1]] in labirinto:
		pacman[0] = linha
		sentido[0] = 'V'

#funcao colide, verifica qual o estado dos fantasmas, de acordo com este, ocorre uma interacao diferente, se estiverem fortes, todos voltam para posicao inicial e o pacman tambem, se estiverem fracos, o fantasma que colidiu volta para o meio e pacman permanesse na posicao
def colide(scr):
	global vidas,fantasma1,fantasma2,fantasma3,fantasma4,pacman,pontos,sentido,estado,hit,pontuacao,extra
	if estado[0] == 'forte':
		vidas[0] -= 1
		extra += 1 #registra que morreu um vez na fase
		time.sleep(1)
		scr.addch(pacman[0],pacman[1]," ")
		pacman = [12,23]
		if not [fantasma1[0],fantasma1[1]] in pontos:
			scr.addch(fantasma1[0],fantasma1[1]," ")
		if not [fantasma2[0],fantasma2[1]] in pontos:
			scr.addch(fantasma2[0],fantasma2[1]," ")
		if not [fantasma3[0],fantasma3[1]] in pontos:
			scr.addch(fantasma3[0],fantasma3[1]," ")
		if not [fantasma4[0],fantasma4[1]] in pontos:
			scr.addch(fantasma4[0],fantasma4[1]," ")
		fantasma1 = [10,28,1]
		fantasma2 = [10,29,1]
		fantasma3 = [10,30,1]
		fantasma4 = [10,31,1]
		sentido = ['X']

	elif estado[0] == 'fraco':
		hits = [200,400,800,1600]  #lista para dar pontos extras ao matar os fantasmas
		pontuacao[0] += hits[hit[0]] #soma a pontuacao o hit respectivo
		hit[0] += 1 #a cada fantasma comido, aumenta 1 no hit
		if pacman == [fantasma1[0],fantasma1[1]]:
			if not [fantasma1[0],fantasma1[1]] in pontos:
				scr.addch(fantasma1[0],fantasma1[1]," ")
			fantasma1 = [10,28,1]
		if pacman == [fantasma2[0],fantasma2[1]]:
			if not [fantasma2[0],fantasma2[1]] in pontos:
				scr.addch(fantasma2[0],fantasma2[1]," ")
			fantasma2 = [10,29,1]
		if pacman == [fantasma3[0],fantasma3[1]]:
			if not [fantasma3[0],fantasma3[1]] in pontos:
				scr.addch(fantasma3[0],fantasma3[1]," ")
			fantasma3 = [10,30,1]
		if pacman == [fantasma4[0],fantasma4[1]]:
			if not [fantasma4[0],fantasma4[1]] in pontos:
				scr.addch(fantasma4[0],fantasma4[1]," ")
			fantasma4 = [10,31,1]

#funcao pausa
def pausa(scr):
	scr.addstr(10,27,'PAUSE')
	while True:
		pause = scr.getch()
		if pause == ord('p') or pause == ord('P'):		
			scr.addstr(10,27,'     ')
			break

#funcao que finaliza o jogo
def end(scr):
	global pontuacao,player
	scr.clear()
	scr.addstr(10,15,"GAME OVER!")
	scr.addstr(11,15,"TOTAL DE PONTOS: %d" % pontuacao[0])
  	if pontuacao[0] > int(r[1]):
      		scr.addstr(12,15,"PARABENS, VOCE QUEBROU O RECORDE")
     		scr.addstr(13,15,"NOVO RECORDE: %d" % pontuacao[0])
     		arq = open("recordpacman.txt","w")
     		arq.write('%s,%d' % (player,pontuacao[0]))
     		arq.close()
     		r[0],r[1] = player,str(pontuacao[0])
	else:
		scr.addstr(12,15,"RECORDE ATUAL: %s" % r[1])
	scr.refresh()
   	time.sleep(5)

#funcao passa fase, reseta todas as posicoes e variaveis de controle do jogo, assim como gera novo labirinto, pontos e superpontos
def passafase():
	global pacman,pontos,fantasma1,fantasma2,fantasma3,fantasma4,labirinto,superpontos,speed,contador,estado,fase,extra
	pacman = [12,23]
	fantasma1 = [10,28,1]
	fantasma2 = [10,29,1]
	fantasma3 = [10,30,1]
	fantasma4 = [10,31,1]
	superpontos = [[1,3],[19,3],[1,57],[19,57]]
	estado = ['forte']
	sentido = ['X']
	contador = 0
	extra = 0
	labirinto = []
	pontos = []
	fase[0] += 1
	speed -= 0.03
	if fase[0] == 1:
		gerafase1()
		gerapontos()
	elif fase[0] == 2:
		gerafase2()
		gerapontos()
	elif fase[0] == 3:
		gerafase3()
		gerapontos()

#funcao das telas iniciais
def start(scr):
	scr.addstr(8,15,"UNIVERSIDADE FEDERAL DE CAMPINA GRANDE - UFCG")
	scr.addstr(9,15,"LABORATORIO DE PROGRAMACAO I")
	scr.addstr(10,15,"ROTEIRO DE PROJETO 3")
	scr.addstr(11,15,"JOGO PACMAN, FEITO NO MODULO CURSES DE PYTHON")
	scr.addstr(12,15,"DESENVOLVEDOR: PEDRO HENRIQUES NETO")
	scr.addstr(15,15,"APERTE QUALQUER TECLA PARA CONTINUAR")
	scr.refresh()
	temp = scr.getch()
	scr.clear()
	scr.addstr(2,12,"XXXXXXXX  XXXXXXXX  XXXXXXXX  XX    XX  XXXXXXXX  XXX   XX")
	scr.addstr(3,12,"XX    XX  XX    XX  XX        XXX  XXX  XX    XX  XXXX  XX")
	scr.addstr(4,12,"XX    XX  XX    XX  XX        XX XX XX  XX    XX  XX XX XX")
	scr.addstr(5,12,"XXXXXXXX  XXXXXXXX  XX        XX XX XX  XXXXXXXX  XX  XXXX")
	scr.addstr(6,12,"XX        XX    XX  XX        XX    XX  XX    XX  XX   XXX")
	scr.addstr(7,12,"XX        XX    XX  XXXXXXXX  XX    XX  XX    XX  XX    XX")
	scr.addstr(10,8,"    xxxxxxxxxxxxx")
	scr.addstr(11,8,"  xxxxx   xxxxx")
	scr.addstr(12,8,"xxxxxxxxxxxxx       xx       xx       xx       xx       xx       xx")
	scr.addstr(13,8,"xxxxxxxxxxx        xxxx     xxxx     xxxx     xxxx     xxxx     xxxx")
	scr.addstr(14,8,"xxxxxxxxxxxxx       xx       xx       xx       xx       xx       xx")
	scr.addstr(15,8,"  xxxxxxxxxxxxx")
	scr.addstr(16,8,"    xxxxxxxxxxxxx")
	scr.addstr(19,20,"APERTE QUALQUER TECLA PARA CONTINUAR")
	scr.refresh()
	temp = scr.getch()
	scr.clear()
	scr.addstr(2,25,"----====[INSTRUNCOES]====----")
	scr.addstr(4,5,"- USE AS SETAS PARA SE MOVIMENTAR")
	scr.addstr(5,5,"- COMA TODOS OS PONTOS PARA PASSAR DE FASE")
	scr.addstr(6,5,"- SE ALGUM FANTASMA TE PEGAR VOCE MORRE")
	scr.addstr(7,5,"- COMENDO OS SUPER-PONTOS $, VOCE PODERA COMER OS FANTASMAS POR UM TEMPO")
	scr.addstr(8,5,"- CADA FANTASMA COMIDO NESSE TEMPO VALE MAIS PONTOS: 200, 400, 800, 1600")
	scr.addstr(9,5,"- CADA PONTO VALE 10 PONTOS, CADA SUPER-PONTO VALE 50 PONTOS")
	scr.addstr(10,5,"- APERTE [P] PARA PAUSAR")
	scr.addstr(11,5,"- APERTE [Q] PARA SAIR DO JOGO")
	scr.addstr(12,5,"- A CADA FASE A VELOCIDADE AUMENTA E VOCE GANHA 1 VIDA EXTRA")
	scr.addstr(13,5,"- SE VOCE PASSAR DE UMA FASE SEM MORRER, GANHA 1000 PONTOS EXTRA")
	scr.addstr(14,5,"- SE VOCE CONCLUIR O JOGO SEM MORRER NENHUMA VEZ, GANHA 2000 PONTOS EXTRA")
	scr.addstr(15,5,"- E CLARO, DIVIRTA-SE!!!")
	scr.addstr(19,20,"APERTE QUALQUER TECLA PARA INICIAR O JOGO")
	scr.refresh()
	temp = scr.getch()
	scr.clear()
	
#funcao principal
def main(scr):
	global pacman,pontuacao,pontos,fantasma1,fantasma2,fantasma3,fantasma4,labirinto,contador,hit,speed,extra
	curses.curs_set(0)
	start(scr)
	
	scr.nodelay(1)
	passafase()
	while True:

		#temporizador para os fantasma no estado fraco
		if estado[0] == 'fraco':
			contador += 1
			if contador == 100 or hit[0] == 4:
				estado[0] = 'forte'
				hit[0] = 0
				contador = 0

		tela(scr)
		
		#testa colisao 1
		if pacman == [fantasma1[0],fantasma1[1]] or pacman == [fantasma2[0],fantasma2[1]] or pacman == [fantasma3[0],fantasma3[1]] or pacman == [fantasma4[0],fantasma4[1]]:
			if estado[0] == 'forte':
				time.sleep(1)
			elif estado[0] == 'fraco':
				time.sleep(0.5)
			colide(scr)

		#movimentacao do pacman
		ch = scr.getch()

		if ch == ord('p') or ch == ord('P'):
			pausa(scr)

		if ch == ord('q') or ch == ord('Q'):
			break

		if ch == curses.KEY_UP or sentido[0] == '^':
			scr.addch(pacman[0],pacman[1]," ")
			move_acima()
		if ch == curses.KEY_DOWN or sentido[0] == 'V':
			scr.addch(pacman[0],pacman[1]," ")
			move_abaixo()
		if ch == curses.KEY_RIGHT or sentido[0] == '>':
			scr.addch(pacman[0],pacman[1]," ")
			move_direita()
		if ch == curses.KEY_LEFT or sentido[0] == '<':
			scr.addch(pacman[0],pacman[1]," ")
			move_esquerda()

		#atribui uma variavel a posicao do pacman
		posicao = [pacman[0],pacman[1]]	
		
		#testa colisao 2
		if posicao == [fantasma1[0],fantasma1[1]] or posicao == [fantasma2[0],fantasma2[1]] or posicao == [fantasma3[0],fantasma3[1]] or posicao == [fantasma4[0],fantasma4[1]]:
			if estado[0] == 'forte':
				time.sleep(1)
			elif estado[0] == 'fraco':
				time.sleep(0.5)
			colide(scr)
		
		#testa se a posicao esta sobre algum ponto
		if posicao in pontos:
			pontos.remove(posicao)
			pontuacao[0] += 10
		
		if posicao in superpontos:
			superpontos.remove(posicao)
			pontuacao[0] += 50
			estado[0] = 'fraco'
			contador = 0

	


		#movimentacao do fantasma1		
		if not [fantasma1[0],fantasma1[1]] in pontos:
			scr.addch(fantasma1[0],fantasma1[1]," ")
		if fantasma1[2] == 1:
			p1 = [(fantasma1[0] - 1) % 21,fantasma1[1],1]
			p2 = [fantasma1[0],(fantasma1[1] - 1) % 61,3]
			p3 = [fantasma1[0],(fantasma1[1] + 1) % 61,4]
			temp = [p1,p2,p3]
			destino = temp[random.randint(0,2)]
			while [destino[0],destino[1]] in labirinto:
				destino = temp[random.randint(0,2)]
			fantasma1 = destino
		if fantasma1[2] == 2:
			p1 = [(fantasma1[0] + 1) % 21,fantasma1[1],2]
			p2 = [fantasma1[0],(fantasma1[1] - 1) % 61,3]
			p3 = [fantasma1[0],(fantasma1[1] + 1) % 61,4]
			temp = [p1,p2,p3]
			destino = temp[random.randint(0,2)]
			while [destino[0],destino[1]] in labirinto:
				destino = temp[random.randint(0,2)]
			fantasma1 = destino
		if fantasma1[2] == 3:
			p1 = [(fantasma1[0] - 1) % 21,fantasma1[1],1]
			p2 = [(fantasma1[0] + 1) % 21,fantasma1[1],2]
			p3 = [fantasma1[0],(fantasma1[1] - 1) % 61,3]
			temp = [p1,p2,p3]
			destino = temp[random.randint(0,2)]
			while [destino[0],destino[1]] in labirinto:
				destino = temp[random.randint(0,2)]
			fantasma1 = destino
		if fantasma1[2] == 4:
			p1 = [(fantasma1[0] - 1) % 21,fantasma1[1],1]
			p2 = [(fantasma1[0] + 1) % 21,fantasma1[1],2]
			p3 = [fantasma1[0],(fantasma1[1] + 1) % 61,4]
			temp = [p1,p2,p3]
			destino = temp[random.randint(0,2)]
			while [destino[0],destino[1]] in labirinto:
				destino = temp[random.randint(0,2)]
			fantasma1 = destino
		

		#movimentacao do fantasma2
		if not [fantasma2[0],fantasma2[1]] in pontos:
			scr.addch(fantasma2[0],fantasma2[1]," ")
		if fantasma2[2] == 1:
			p1 = [(fantasma2[0] - 1) % 21,fantasma2[1],1]
			p2 = [fantasma2[0],(fantasma2[1] - 1) % 61,3]
			p3 = [fantasma2[0],(fantasma2[1] + 1) % 61,4]
			temp = [p1,p2,p3]
			destino = temp[random.randint(0,2)]
			while [destino[0],destino[1]] in labirinto:
				destino = temp[random.randint(0,2)]
			fantasma2 = destino
		if fantasma2[2] == 2:
			p1 = [(fantasma2[0] + 1) % 21,fantasma2[1],2]
			p2 = [fantasma2[0],(fantasma2[1] - 1) % 61,3]
			p3 = [fantasma2[0],(fantasma2[1] + 1) % 61,4]
			temp = [p1,p2,p3]
			destino = temp[random.randint(0,2)]
			while [destino[0],destino[1]] in labirinto:
				destino = temp[random.randint(0,2)]
			fantasma2 = destino
		if fantasma2[2] == 3:
			p1 = [(fantasma2[0] - 1) % 21,fantasma2[1],1]
			p2 = [(fantasma2[0] + 1) % 21,fantasma2[1],2]
			p3 = [fantasma2[0],(fantasma2[1] - 1) % 61,3]
			temp = [p1,p2,p3]
			destino = temp[random.randint(0,2)]
			while [destino[0],destino[1]] in labirinto:
				destino = temp[random.randint(0,2)]
			fantasma2 = destino
		if fantasma2[2] == 4:
			p1 = [(fantasma2[0] - 1) % 21,fantasma2[1],1]
			p2 = [(fantasma2[0] + 1) % 21,fantasma2[1],2]
			p3 = [fantasma2[0],(fantasma2[1] + 1) % 61,4]
			temp = [p1,p2,p3]
			destino = temp[random.randint(0,2)]
			while [destino[0],destino[1]] in labirinto:
				destino = temp[random.randint(0,2)]
			fantasma2 = destino	


		#movimentacao do fantasma3
		if not [fantasma3[0],fantasma3[1]] in pontos:
			scr.addch(fantasma3[0],fantasma3[1]," ")
		if fantasma3[2] == 1:
			p1 = [(fantasma3[0] - 1) % 21,fantasma3[1],1]
			p2 = [fantasma3[0],(fantasma3[1] - 1) % 61,3]
			p3 = [fantasma3[0],(fantasma3[1] + 1) % 61,4]
			temp = [p1,p2,p3]
			destino = temp[random.randint(0,2)]
			while [destino[0],destino[1]] in labirinto:
				destino = temp[random.randint(0,2)]
			fantasma3 = destino
		if fantasma3[2] == 2:
			p1 = [(fantasma3[0] + 1) % 21,fantasma3[1],2]
			p2 = [fantasma3[0],(fantasma3[1] - 1) % 61,3]
			p3 = [fantasma3[0],(fantasma3[1] + 1) % 61,4]
			temp = [p1,p2,p3]
			destino = temp[random.randint(0,2)]
			while [destino[0],destino[1]] in labirinto:
				destino = temp[random.randint(0,2)]
			fantasma3 = destino
		if fantasma3[2] == 3:
			p1 = [(fantasma3[0] - 1) % 21,fantasma3[1],1]
			p2 = [(fantasma3[0] + 1) % 21,fantasma3[1],2]
			p3 = [fantasma3[0],(fantasma3[1] - 1) % 61,3]
			temp = [p1,p2,p3]
			destino = temp[random.randint(0,2)]
			while [destino[0],destino[1]] in labirinto:
				destino = temp[random.randint(0,2)]
			fantasma3 = destino
		if fantasma3[2] == 4:
			p1 = [(fantasma3[0] - 1) % 21,fantasma3[1],1]
			p2 = [(fantasma3[0] + 1) % 21,fantasma3[1],2]
			p3 = [fantasma3[0],(fantasma3[1] + 1) % 61,4]
			temp = [p1,p2,p3]
			destino = temp[random.randint(0,2)]
			while [destino[0],destino[1]] in labirinto:
				destino = temp[random.randint(0,2)]
			fantasma3 = destino


		#movimentacao do fantasma4
		if not [fantasma4[0],fantasma4[1]] in pontos:
			scr.addch(fantasma4[0],fantasma4[1]," ")
		if fantasma4[2] == 1:
			p1 = [(fantasma4[0] - 1) % 21,fantasma4[1],1]
			p2 = [fantasma4[0],(fantasma4[1] - 1) % 61,3]
			p3 = [fantasma4[0],(fantasma4[1] + 1) % 61,4]
			temp = [p1,p2,p3]
			destino = temp[random.randint(0,2)]
			while [destino[0],destino[1]] in labirinto:
				destino = temp[random.randint(0,2)]
			fantasma4 = destino
		if fantasma4[2] == 2:
			p1 = [(fantasma4[0] + 1) % 21,fantasma4[1],2]
			p2 = [fantasma4[0],(fantasma4[1] - 1) % 61,3]
			p3 = [fantasma4[0],(fantasma4[1] + 1) % 61,4]
			temp = [p1,p2,p3]
			destino = temp[random.randint(0,2)]
			while [destino[0],destino[1]] in labirinto:
				destino = temp[random.randint(0,2)]
			fantasma4 = destino
		if fantasma4[2] == 3:
			p1 = [(fantasma4[0] - 1) % 21,fantasma4[1],1]
			p2 = [(fantasma4[0] + 1) % 21,fantasma4[1],2]
			p3 = [fantasma4[0],(fantasma4[1] - 1) % 61,3]
			temp = [p1,p2,p3]
			destino = temp[random.randint(0,2)]
			while [destino[0],destino[1]] in labirinto:
				destino = temp[random.randint(0,2)]
			fantasma4 = destino
		if fantasma4[2] == 4:
			p1 = [(fantasma4[0] - 1) % 21,fantasma4[1],1]
			p2 = [(fantasma4[0] + 1) % 21,fantasma4[1],2]
			p3 = [fantasma4[0],(fantasma4[1] + 1) % 61,4]
			temp = [p1,p2,p3]
			destino = temp[random.randint(0,2)]
			while [destino[0],destino[1]] in labirinto:
				destino = temp[random.randint(0,2)]
			fantasma4 = destino

		
		
		
		#tempo de tela de acordo com a variavel speed, que a cada nova fase eh diminuida em 0.03s
		time.sleep(speed)

		#quando acaba os pontos, passa de fase
		if len(pontos) == 0 and len(superpontos) == 0:
			if extra == 0:
				pontuacao[0] += 1000 #da 1000 pontos extra se nao morreu durante a fase
			vidas[0] += 1
			passafase()

		#quando as vidas ou as fases acabam, o jogo acaba
		if vidas[0] == 0 or fase[0] == 4:
			if vidas[0] == 5:
				pontuacao[0] += 2000 #da 2000 pontos extra se nao morreu durante todo jogo
			end(scr)
			break

		


curses.wrapper(main)
