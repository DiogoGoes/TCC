# -*- coding: utf-8 -*-
"""
Created on Thu Jun 02 14:30:25 2016

@author: szq4379
"""

from bs4 import BeautifulSoup
import re
import pprint

def IsolaLinksUsuario(url):
	soup = BeautifulSoup(open(url, 'r'), 'lxml')
	
	user_infos = soup.findAll('ul', {'class': 'caixa-user-itens'})
	
	for link in user_infos[0].findAll('a'):
		print link.get_text()
		print link['href'], '\n'

def CapturaJogos(url):
	soup = BeautifulSoup(open(url, 'r'), 'lxml')
	
	boards = dict()
	i = 0
	
	for bg in soup.findAll('a', {'class': 'titulo-row'}):
		boards[i] = {'name': bg.get_text(), 'link': bg['href'], 'type': 'B'}
		i += 1
	
	pprint.pprint(boards)


def CapturaUsuarios(url):
	soup = BeautifulSoup(open(url, 'r'), 'lxml')
	
	leiloes = soup.findAll('a', href = re.compile('http://www\.ludopedia\.com\.br/usuario/.+'))
	
	users = dict()
	i = 0
	
	for leilao in leiloes:
		users[i] = {'user': leilao.get_text(), 'page': leilao['href']}

	pprint.pprint(users)

#IsolaLinksUsuario('pagina.html')

#CapturaJogos('pagina.html')

#CapturaUsuarios('pagina.html')
