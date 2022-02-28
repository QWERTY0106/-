import random

import copy
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt



class Klaster:
	def __init__(self, xs, ys, zs, N_clust):
		self.xs = xs
		self.ys = ys
		self.zs = zs
		self.N_clust = N_clust
		self.array = []
		self.index = []
		self.cluster = []
		for i in range (len(self.xs)):
			self.array.append((xs[i], ys[i], zs[i]))
		n = len(self.xs)
		self.cluster = [[0 for i in range (3)] for q in range (self.N_clust)]
		print('Координаты кластеров (x, y, z):')
		for i in range (self.N_clust):
			for q in range (3):
				self.cluster[i][q] = np.random.uniform(0, 100)
			print(self.cluster[i])
		#self.cluster = [[100,0,0],[0,100,0],[100,100,0]] для задания кластеров вручную
		print()  
		while 1:
			for i in range(n):
					min_distance = 10**8
					distance = 0
					index_claster = 0
					for j in range(self.N_clust):
							distance = ((self.array[i][0] - self.cluster[j][0])**2 + (self.array[i][1] - self.cluster[j][1])**2 + (self.array[i][2] - self.cluster[j][2])**2)**(0.5)
							if distance < min_distance:
								min_distance = distance
								index_claster = j
					self.index.append((self.array[i], index_claster))
			cluster_content = [[] for i in range(self.N_clust)]
			for i in range(n):
				cluster_content[self.index[i][1]].append(self.index[i][0])
			previous_cluster = copy.deepcopy(self.cluster)

			for i in range(self.N_clust):
				sumx = 0
				sumy = 0
				sumz = 0
				for j in range(len(cluster_content[i])):
					sumx += cluster_content[i][j][0]
					sumy += cluster_content[i][j][1]
					sumz += cluster_content[i][j][2]
				self.cluster[i][0] = sumx/len(cluster_content[i])
				self.cluster[i][1] = sumy/len(cluster_content[i])
				self.cluster[i][2] = sumz/len(cluster_content[i])
			
			print('Координаты кластеров (x, y, z):')
			for i in range (self.N_clust):
				print(self.cluster[i])
			print()
			
			if previous_cluster == self.cluster:
				break
				
				
	def get_indexes(self):
		n = len(self.xs)
		for i in range(n):
			print('Точка с координатами (x, y, z):', self.index[i][0], 'индекс кластера к которому относятся точки:', self.index[i][1])

	

	def plot(self):
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
	
	def what_cluster(self, x, y, z):
		min_distance = 10**8
		distance = 0
		index_claster = 0
		for j in range(self.N_clust):
			distance = ((x - self.cluster[j][0])**2 + (y - self.cluster[j][1])**2 + (z - self.cluster[j][2])**2)**(0.5)
			if distance < min_distance:

				min_distance = distance
				index_claster = j
		print('Точка с координатами (',x,y,z,')','принадлежит кластеру с координатами:', self.cluster[index_claster])

print('Введите количество точек для генерации:')
count_poins = int(input())
xs, ys, zs = [], [], []
for i in range (count_poins):
	xs.append(np.random.uniform(0,100))
	ys.append(np.random.uniform(0,100))
	zs.append(np.random.uniform(0,100))
print('Введите количество кластеров (N_clust)')
N_clust = int(input())
while True:
	print('Меню:')
	print('Введите 1, если хотите распределить точки по кластерам!')
	print('Введите 2, если хотите нарисовать трехмерный точечный график с распределением точек по кластерам!')
	print('Введите 3, если хотите узнать, к какому кластеру относится новая веденная с клавиатуры точка!')
	print('Введите 4, если хотите выйти из программы!')
	menu = int(input())
	if menu == 1:
		Klaster(xs, ys, zs, N_clust).get_indexes()
	elif menu == 2:
		Klaster(xs, ys, zs, N_clust).plot()
	elif menu == 3:
		print('Введите координаты 3-х точек!')
		print('Введите x:'); x = float(input())
		print('Введите y:'); y = float(input())
		print('Введите z:'); z = float(input())
		Klaster(xs, ys, zs, N_clust).what_cluster(x, y, z)
	elif menu == 4:
		break
