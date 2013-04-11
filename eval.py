from datapoint import *
from kmeans import *
from kmeansGUI import *
from DataReader import *

data = []
reader = DataReader("data/movies.condensed.data")
for label, tokens in reader:
	# pass the label to the WordData constructor to keep track of it for later use
	data.append(WordDataPoint(tokens, label=label))
# k=five clusters
clusterer = KMeans(data, 5, KMeans.COSINE)
clusters = clusterer.cluster()

# Store purities relative to clusters
purities = []
for cluster in clusters:
	purity_labels = {}

	print "-" * 25
	for point in cluster:
		print point.get_label() + ": " + str(point)
		if point.get_label() in purity_labels:
			purity_labels[point.get_label()] += 1
		else:
			purity_labels[point.get_label()] = 1
	max_occurence = 0
	max_label = ""
	for k,v in purity_labels.items():
		if v > max_occurence:
			max_occurence = v
			max_label = k
	purities.append(max_occurence / len(cluster))



i = 0
# Print individual purities
for p in purities:
	print "Cluster "+str(i)+":"+str(p)
print "Average purity: "+str(sum(l) / float(len(l)))


