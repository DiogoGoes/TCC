# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 22:58:00 2016

@author: Diogo
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 19:08:00 2016

@author: Diogo
"""
def ImportGames():
	games = list()
	user_games = dict()

	with open('C:\\Users\\Diogo\\Documents\\Monografia FIA\\UserGamesCleansed.txt', 'r', encoding = 'utf-8') as lines:
		
		next(lines) # Skiping headers
		
		for ln in lines:
			user, board_game, board_type, list_type, score10 = ln.split('##')
			
			if board_game not in games:
				games.append(board_game.replace('\t',' ').replace('  ', ' '))
				
			if user not in user_games:
				user_games[user] = dict()

			if board_game not in user_games[user].keys():
				user_games[user][board_game] = 1
			
	return (games, user_games)
	
games, user_games = ImportGames()

def BuildMatrix(games, user_games):
	with open('C:\\Users\\Diogo\\Documents\\Monografia FIA\\UserGamesMatrix.tab', 'a', encoding = 'utf-8') as lines:
		lines.write('user\t' + '\t'.join(games) + '\n')
	
	for user in user_games:
		user_line = list()
		
		for game in games:
			
			if game in user_games[user].keys():
				user_line.append('1')
			else:
				user_line.append('0')
		
		with open('C:\\Users\\Diogo\\Documents\\Monografia FIA\\UserGamesMatrix.tab', 'a', encoding = 'utf-8') as lines:
			lines.write(user + '\t' + '\t'.join(user_line) + '\n')
		
BuildMatrix(games, user_games)