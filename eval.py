from datapoint import *
from kmeans import *
from kmeansGUI import *
from DataReader import *

data = []
reader = DataReader("movies.condensed.data")
for label, tokens in reader:
	# pass the label to the WordData constructor to keep track of it for later use
	data.append(WordDataPoint(tokens, label=label))
# k=five clusters
clusterer = KMeans(data, 5, KMeans.COSINE)
clusters = clusterer.cluster()
for cluster in clusters:
	print "-" * 25
	for point in cluster:
		print point.get_label() + ": " + str(point)