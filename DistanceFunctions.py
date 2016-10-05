# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 20:48:23 2016

@author: Diogo
"""

import pprint

from math import sqrt
from collections import OrderedDict

def BuildData():
	user_collection = dict()
	user_hadlist = dict()
	user_whishlist = dict()
	games_list = list()
	
	with open('C:\\Users\\Diogo\\Documents\\Monografia FIA\\UserGamesCleansed.txt', 'r', encoding = 'utf-8') as lines:
		
		next(lines) # Skiping headers
		
		for ln in lines:
			user, board_game, board_type, list_type, score10 = ln.strip().split('##')
			
			if board_game not in games_list:
				games_list.append(board_game)
			
			if user not in user_collection:
				user_collection[user] = dict()
				user_hadlist[user] = dict()
				user_whishlist[user] = dict()
			
			if board_type == 'colecao' and board_game not in user_collection[user].keys():
				user_collection[user][board_game] = int(score10)
				
			elif board_type == 'teve' and board_game not in user_hadlist[user].keys():
				user_hadlist[user][board_game] = int(score10)
			
			elif board_type == 'lista_desejos' and board_game not in user_whishlist[user].keys():
				user_whishlist[user][board_game] = int(score10)
			
	return (user_collection, user_hadlist, user_whishlist, games_list)
	
def DefineCommons(user, neighbour):
	
	common_list = list()
	
	for bg in user:
		if bg in neighbour.keys():
			common_list.append(bg)
	
	return None if len(common_list) == 0 else common_list

def CoefficientJaccard(user, neighbour):
	
	user_games = len(user) or 0
	neighbour_games = len(neighbour) or 0
	inter_games = 0
	
	for bg in user:
		if bg in neighbour.keys():
			inter_games += 1
			
	den = user_games + neighbour_games - inter_games
	
	return None if den == 0 or inter_games == 0 else inter_games/den

def CoefficientSorensen(user, neighbour):
	
	user_games = len(user) or 0
	neighbour_games = len(neighbour) or 0
	inter_games = 0
	
	for bg in user:
		if bg in neighbour.keys():
			inter_games += 1
			
	den = user_games + neighbour_games
	
	return None if den == 0 or inter_games == 0 else (inter_games*2)/den

def EuclideanDistance(user, neighbour, fl_correct = False):
	
	sum_of_squares = 0
	number_of_vars = 0
	non_missings = 0
	factor = 1
	n = 0
	
	for bg, sc in user.items():
		
		number_of_vars += 1
		
		if sc == -1:
			continue
		
		non_missings += 1
		
		if bg in neighbour.keys() and neighbour[bg] > -1:
			n += 1
			sum_of_squares += pow(sc - neighbour[bg], 2)
	
	if fl_correct == True and non_missings > 0:
		factor = number_of_vars/non_missings
	
	return None if n == 0 else sqrt(factor*sum_of_squares)


def ApplyFunc(target, func):
	return_var = dict()
	sorted_return_var = dict()
	
	for user in target:
		
		return_var[user] = dict()
		sorted_return_var[user] = dict()
		
		for neighbour in target:
			
			if user != neighbour:
				num = func(target[user], target[neighbour])
				
				if num != None:
					return_var[user][neighbour] = num
				
		sorted_return_var[user] = OrderedDict(sorted(return_var[user].items(), key = lambda x: x[1]))
	
	return sorted_return_var

user_collection, user_hadlist, user_whishlist, games_list = BuildData()
#distance_sorted[user] = OrderedDict(sorted(distance[user].items(), key = lambda x: x[1]))

jaccard = ApplyFunc(user_collection, CoefficientJaccard)

pprint.pprint(user_collection['CoronelMostarda'])
#pprint.pprint(common_list['CoronelMostarda'])
pprint.pprint(jaccard['CoronelMostarda'])



