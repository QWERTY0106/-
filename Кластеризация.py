import random

import copy
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt



class Klaster:
	def __init__(self, xs, ys, zs, N_clust):
		self.xs = xs #список координат x 
		self.ys = ys #список координат у
		self.zs = zs #список координат z
		self.N_clust = N_clust #количество кластеров
		self.array = [] #список точек вида (x, y, z)
		self.index = [] #список элементов вида (точка, номер кластера)
		self.cluster = [] #список центроид
		for i in range (len(self.xs)):
			self.array.append((xs[i], ys[i], zs[i])) #из списков координат составляем список точек
		n = len(self.xs) #количество точек
		self.cluster = [[0 for i in range (3)] for q in range (self.N_clust)] #задаем N_clust кластеров их центрами
		print('Координаты кластеров (x, y, z):')
		for i in range (self.N_clust): #здесь происходит первое задание центров
			for q in range (3):
				self.cluster[i][q] = np.random.uniform(0, 100) #рандомно задаем координаты центров
			print(self.cluster[i])
		#self.cluster = [[100,0,0],[0,100,0],[100,100,0]] для задания кластеров вручную
		print()  
		while 1: #цикл, который выполняется, пока кластеры не перестанут менять свои центры
			for i in range(n): #в этом цикле будет происходить распределение точек по кластерам
					min_distance = 10**8
					distance = 0
					index_claster = 0 #счетчик номера кластера
					for j in range(self.N_clust): #проверим каждый кластер на минимальность расстояния до его центра от текцщей точки
							distance = ((self.array[i][0] - self.cluster[j][0])**2 + (self.array[i][1] - self.cluster[j][1])**2 + (self.array[i][2] - self.cluster[j][2])**2)**(0.5)
							if distance < min_distance: #если дистанция меньше предыдущей то перезаписываем min дистанцию и запоминаем индекс кластера
								min_distance = distance
								index_claster = j
					self.index.append((self.array[i], index_claster)) #формируем данные в список index
			cluster_content = [[] for i in range(self.N_clust)] #более удобный для понимания список, состоящий из N_clust списков, в каждом из которых хранятся точки соответствующего кластера
			for i in range(n): #здесь перераспределяем данные списка index в более удобные данные cluster_content
				cluster_content[self.index[i][1]].append(self.index[i][0])
			previous_cluster = copy.deepcopy(self.cluster) #глубокая копия предыдущих центроид, чтобы далее сравнивать ее с новыми

			for i in range(self.N_clust): #в этом цикле происходит пересчёт центров, которые перемещаются в центр масс множества своих точек
				sumx = 0
				sumy = 0
				sumz = 0
				for j in range(len(cluster_content[i])):
					sumx += cluster_content[i][j][0] #сумма координат х
					sumy += cluster_content[i][j][1] #сумма координат у
					sumz += cluster_content[i][j][2] #сумма координат z
				self.cluster[i][0] = sumx/len(cluster_content[i]) #координата х центра масс
				self.cluster[i][1] = sumy/len(cluster_content[i]) #координата у центра масс
				self.cluster[i][2] = sumz/len(cluster_content[i]) #координата z центра масс
			
			print('Координаты кластеров (x, y, z):') #вывод на экран новых центров
			for i in range (self.N_clust): 
				print(self.cluster[i])
			print()
			
			if previous_cluster == self.cluster: #проверка на выход из цикла
				break
				
				
	def get_indexes(self): #метод, показывающий к какому кластеру пренадлежит каждая точка
		n = len(self.xs)
		for i in range(n):
			print('Точка с координатами (x, y, z):', self.index[i][0], 'индекс кластера к которому относится точка:', self.index[i][1])

	

	def plot(self): #метод для получения трёхмерного графика
		colors = ['b', 'g', 'c', 'r', 'm', 'y', 'k', 'w']
		fig = plt.figure()
		ax = plt.axes(projection='3d')
		plt.xlabel("x")    
		plt.ylabel("y")
		
		ax.set_title('Трехмерный точечный график')
		n = len(self.xs)
		for i in range (n):
			ax.scatter3D(self.index[i][0][0], self.index[i][0][1], self.index[i][0][2], color = colors[self.index[i][1]])
		plt.show()
	
	def what_cluster(self, x, y, z): #метод, возращающий индекс кластера к которому принадлежит введённая с клавиатуры точка
		min_distance = 10**8
		distance = 0
		index_claster = 0
		for j in range(self.N_clust): #как уже было выше, проверка на минимальность расстояния от точки до центра
			distance = ((x - self.cluster[j][0])**2 + (y - self.cluster[j][1])**2 + (z - self.cluster[j][2])**2)**(0.5)
			if distance < min_distance:

				min_distance = distance
				index_claster = j
		print('Точка с координатами (',x,y,z,')','принадлежит кластеру с координатами:', self.cluster[index_claster])

print('Введите количество точек для генерации:')
count_poins = int(input()) #количество точек
xs, ys, zs = [], [], [] #списки координат
for i in range (count_poins): #заполнение списков координат рандомными числами
	xs.append(np.random.uniform(0,100))
	ys.append(np.random.uniform(0,100))
	zs.append(np.random.uniform(0,100))
print('Введите количество кластеров (N_clust):')
N_clust = int(input()) #количество кластеров
while True: #цикл продолжается пока не выберем выход из программы
	print('Меню:')
	print('Введите 1, если хотите распределить точки по кластерам!')
	print('Введите 2, если хотите нарисовать трехмерный точечный график с распределением точек по кластерам!')
	print('Введите 3, если хотите узнать, к какому кластеру относится новая введенная с клавиатуры точка!')
	print('Введите 4, если хотите выйти из программы!')
	menu = int(input())
	if menu == 1: #распределение точек по кластерам
		Klaster(xs, ys, zs, N_clust).get_indexes()
	elif menu == 2: #график
		Klaster(xs, ys, zs, N_clust).plot()
	elif menu == 3: #к какому кластеру относится точка?
		print('Введите координаты точки!')
		print('Введите x:'); x = float(input())
		print('Введите y:'); y = float(input())
		print('Введите z:'); z = float(input())
		Klaster(xs, ys, zs, N_clust).what_cluster(x, y, z)
	elif menu == 4: #выход из программы
		break
