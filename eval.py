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
clusterer = KMeans(data, 5, DataPoint.EUCLIDEAN)
clusterer.cluster()
print "---KMEANS DONE---"
clusters = clusterer.get_clusters()	

# Store purities relative to clusters
purities = []
for cluster in clusters:
	purity_labels = {}

	# print "-" * 25
	for point in cluster:
		# print point.get_label() + ": " + str(point)
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
	purities.append(max_occurence / float(len(cluster)))



i = 0
# Print average purities purities
print "-"*25
print "NON-WEIGHTED PURITY"
print "-"*25
for p in purities:
	print "Cluster "+str(i)+":"+str(p)
	i+=1

print "Average Unweighted Purity: "+str(sum(purities) / float(len(purities)))

print ""
print "-"*25
print "WEIGHTED PURITY"
print "-"*25
total_points = 0
cluster_lengths=[]
for cluster in clusters:
	c = len(cluster)
	total_points += c
	cluster_lengths.append(c)

i=0
weighted_purities = []
for p in purities:
	weighted_purities.append(p*cluster_lengths[i])
	print "Cluster "+str(i)+":"+str(p*cluster_lengths[i])
	i+=1
print "Average Weighted Purity: "+str(sum(weighted_purities)/float(total_points))

