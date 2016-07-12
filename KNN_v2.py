# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 19:08:00 2016

@author: Diogo
"""
import pprint

from math import sqrt
from collections import OrderedDict
from statistics import mean, median, mode

def ImportDatabase():
	user_games = dict()
	
	with open('C:\\Users\\Diogo\\Documents\\Monografia FIA\\UserGamesCleansed.txt', 'r', encoding = 'utf-8') as lines:
		
		next(lines) # Skiping headers
		
		for ln in lines:
			user, board_game, board_type, list_type, score10 = ln.split('##')
			
			if user not in user_games:
				user_games[user] = dict()
			
			score10 = score10.strip()
			
			if board_type == 'colecao' and score10 != '-1' and board_game not in user_games[user].keys():
				user_games[user][board_game] = int(score10.strip())
			
	return user_games

def EuclideanDistance(user_list, neighbour):
	sum_of_squares = 0
	
	for bg in user_list:
		if bg in neighbour.keys():
			sum_of_squares += pow(user_list[bg] - neighbour[bg], 2)
			
	return -1 if sum_of_squares == 0 else 1/(1+sqrt(sum_of_squares))

def ScoreAverage(user_list, neighbour, weight):
	average = 0
	
	for bg in user_list:
		if bg in neighbour.keys():
			average += pow(user_list[bg] - neighbour[bg], 2)
			
	return average

def RunDistance(user_games):
	distance = dict()
	distance_sorted = dict()
	
	for user in user_games:
		distance[user] = dict()
		for neighbour in user_games:
			distance[user][neighbour] = EuclideanDistance(user_games[user], user_games[neighbour])
			
			if distance[user][neighbour] == -1:
				del(distance[user][neighbour])
		
		distance_sorted[user] = OrderedDict(sorted(distance[user].items(), key = lambda x: x[1]))
	
	return distance_sorted

#user_games = ImportDatabase()
#distance_sorted = RunDistance(user_games)

#pprint.pprint(distance_sorted['CoronelMostarda'])

def KNN(user_games, distance_sorted, knn):
	user_games_avg = dict()
	sum_of_errors = 0
	scores = list()
	n = 0
	
	for user in user_games:
		
		user_games_avg[user] = dict()		
		user_games_avg[user]['avg'] = -1
		user_games_avg[user]['mean'] = -1
		user_games_avg[user]['mode'] = -1
		
		for bg in user_games[user]:
			
			scores.append(bg)
			sum_of_weights = 0
			sum_of_scores = 0
			k = 1
			
			for neighbour, weight in distance_sorted[user].items():
				
				if bg in user_games[neighbour].keys():
					
					sum_of_scores = user_games[neighbour][bg]*weight
					sum_of_weights += weight
					
					if k >= knn:
						break
					else:
						k += 1
			
			if sum_of_weights > 0:
				
				avg = sum_of_scores/sum_of_weights
				user_games_avg[user][bg] = {'score': user_games[user][bg], 'avg': avg, 'max_k': knn, 'count_k': k}
				sum_of_errors += pow(user_games[user][bg] - avg, 2)
				n += 1
	
	if len(scores) > 0:
		user_games_avg[user]['mean'] = mean(scores)
		user_games_avg[user]['median'] = median(scores)
		user_games_avg[user]['mode'] = mode(mode)
		
	rmse = -1 if sum_of_errors == 0 else sqrt(sum_of_errors)
	
	return (user_games_avg, rmse)
	
for i in range(1, 31):
	user_games_avg, rmse = KNN(user_games, distance_sorted, i)
	print("KNN: %d - Errors: %12.8f" % (i, rmse))


		
#user_games_avg = dict()
#sum_of_errors = 0
#	
#for user in user_games:
#	
#	user_new_games[user] = dict()
#	
#	for bg in user_games[user]:
#		
#		sum_of_weights = 0
#		sum_of_scores = 0
#		k = 1
#		
#		for neighbour, weight in distance_sorted[user].items():
#			
#			if bg in user_games[neighbour].keys():
#				
#				sum_of_scores = user_games[neighbour][bg]*weight
#				sum_of_weights += weight
#				
#				if k >= knn:
#					break
#				else:
#					k += 1
#		
#		if sum_of_weights > 0: