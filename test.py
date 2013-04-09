from datapoint import *
from kmeans import *
from kmeansGUI import *
from DataReader import *


# 1. Test GUI
# data = gen_random_data(4, 100)
# clusterer = KMeans(data, 3)
# KMeansGUI(data, clusterer)

# 2. Test Words
# data = []
# data.append(WordDataPoint("I like bananas".split()))
# data.append(WordDataPoint("bananas like me".split()))
# data.append(WordDataPoint("you like bananas".split()))
# data.append(WordDataPoint("I hate apples".split()))
# data.append(WordDataPoint("apples hate me".split()))
# data.append(WordDataPoint("you hate apples".split()))
# # generally use the cosine distance for words
# clusterer = KMeans(data, 2, KMeans.COSINE)
# clusterer.cluster()
# clusters = clusterer.get_clusters()
# # print out the clusters
# for cluster in clusters:
# 	print "-" * 25
# 	for point in cluster:
# 		print point

# 3. Test on larger data
# data = []
# reader = DataReader("movies.condensed.data")
# for label, tokens in reader:
# 	# pass the label to the WordData constructor to keep track of it for later use
# 	data.append(WordDataPoint(tokens, label=label))
# # k=five clusters
# clusterer = KMeans(data, 5, KMeans.COSINE)
# clusters = clusterer.cluster()
# for cluster in clusters:
# 	print "-" * 25
# 	for point in cluster:
# 		print point.get_label() + ": " + str(point)