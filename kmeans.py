"""
k-means clusterer

author: David Kauchak
date: April, 2013
"""

from random import randint
from datapoint import DataPoint
from copy import deepcopy

class KMeans:
  """
  A class for doing k-means clustering of a data set
  """

  INFINITY = 1.0e400

  def __init__(self, data, k, distance_metric=DataPoint.EUCLIDEAN):
    """
    Create a new k-means cluster to cluster *data* into *k*
    clusters.  By default the clustering will use euclidean
    distance, but cosine distance can also be used.

    data should be a list of DataPoints.

    clustering does NOT begin until the cluster method is called.
    """

    self.distance = distance_metric

    self.clusters = []
    self.centers = []
    self.prev_centers = []

    cluster_indexes = []
    num_points = len(data)
    possible_indexes = range(num_points)

    for i in range(1, k+1):
      self.clusters.append([])
      which_index = randint(0, num_points-i)
      self.centers.append(data[possible_indexes[which_index]])
      possible_indexes.pop(which_index)

    self.clusters[0] = data

  def cluster(self, iterations=INFINITY):
    """
    Cluster the data and return the found clusters.

    By default, the clustering will continue until the clusters converge,
    i.e. don't change. Optionally, you can specify a fixed number of iterations.
    """

    def isDone():
      same = True
      for i, prev_center in enumerate(self.prev_centers):
        if prev_center.distance(self.centers[i], self.distance) != 0:
          same = False
          break
      return same

    def iterate():
      self.assign_to_centers()
      self.prev_centers = deepcopy(self.centers)
      self.recalculate_centers()

    if iterations == self.INFINITY: # infinite iterations
      done = False
      while not isDone():
        iterate()
    else:
      for i in xrange(iterations): # finite iterations
        print "ITERATION", i
        iterate()


  def print_clusters(self):
    for cluster in self.clusters:
      print "-" * 25
      for point in cluster:
        print point

  def print_centers(self):
    for center in self.centers:
      print center

  def assign_to_centers(self):
    """
    Assign the points to the cluster centers.  This will
    update the clusters.
    """

    points = sum(self.clusters, [])
    new_clusters = [[] for x in range(len(self.clusters))] # blank clusters

    for point in points:
      min_dist = self.INFINITY
      min_k = -1
      for x, center in enumerate(self.centers):
        dist = center.distance(point, self.distance)
        if dist < min_dist:
          min_dist = dist
          min_k = x
      new_clusters[min_k].append(point)
    self.clusters = new_clusters

  def recalculate_centers(self):
    """
    Recalculte the cluster centers based on the current clusters.
    """

    for i, cluster in enumerate(self.clusters):
      new_center = DataPoint()
      for point in cluster:
        new_center.add_data_counts(point)
      new_center.divide_by_constant(len(cluster))
      self.centers[i] = new_center

  def get_clusters(self):
    """
    Return the current clustering of the data.  The data structure
    returned should be a list of lists, specifically each cluster
    will be represented as a list of DataPoints and you'll be returning
    a list of clusters.
    """

    return self.clusters


  def get_centers(self):
    """ Return the current cluster centers as a list of DataPoints. """

    return self.centers