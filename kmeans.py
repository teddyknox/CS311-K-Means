"""
k-means clusterer

author: David Kauchak
date: April, 2013
"""

from random import randint, uniform
from datapoint import DataPoint
from copy import deepcopy

class KMeans:
  """
  A class for doing k-means clustering of a data set
  """

  INFINITY = 1.0e400
  EPSILON = 0.3

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

    def init_existing_points(k):
      cluster_indexes = []
      num_points = len(data)
      possible_indexes = range(num_points)
      for i in range(1, k+1):
        self.clusters.append([])
        which_index = randint(0, num_points-i)
        self.centers.append(data[possible_indexes[which_index]])
        possible_indexes.pop(which_index)
      self.clusters[0] = data

    def init_generate_points(k):
      cluster_indexes = []

      dim_ranges = {}
      for point in data:
        for dim, val in point.counts.items():
          dim_ranges[dim] = [self.INFINITY, -self.INFINITY]

      for point in data:
        for dim, vals in dim_ranges.items():
          if dim in point.counts:
            # checking against min, max
            dim_ranges[dim][0] = min(vals[0], point.counts[dim])
            dim_ranges[dim][1] = max(vals[1], point.counts[dim])
          else:
            dim_ranges[dim][0] = min(vals[0], 0)
            dim_ranges[dim][1] = max(vals[1], 0)

      for i in range(k):
        self.clusters.append([])
        vector = {}
        for dim, val in dim_ranges.items():
          vector[dim] = uniform(*val)
        self.centers.append(DataPoint(vector))
      self.clusters[0] = data

    init_generate_points(k)

  #   self.lower_bound = {}
  #   for point in sum(self.clusters, []):
  #     self.lower_bound[k][point] = 


  # def get_


  def cluster(self, iterations=INFINITY):
    """
    Cluster the data and return the found clusters.

    By default, the clustering will continue until the clusters converge,
    i.e. don't change. Optionally, you can specify a fixed number of iterations.
    """

    def isDone():
      if self.prev_centers:
        center_delta = 0
        for i, prev_center in enumerate(self.prev_centers):
          center_delta += prev_center.distance(self.centers[i], self.distance)
        print "CENTROID TOTAL CHANGE", center_delta
        return center_delta < self.EPSILON
      else: return False

    def iterate():
      self.assign_to_centers()
      self.prev_centers = deepcopy(self.centers)
      self.recalculate_centers()

    if iterations == self.INFINITY: # infinite iterations
      while not isDone():
        print "Next Iteration" 
        self.print_cluster_lens()
        iterate()
    else:
      for i in xrange(iterations): # finite iterations
        iterate()


  def print_clusters(self):
    for cluster in self.clusters:
      print "-" * 25
      for point in cluster:
        print point
    else:
      print "no clusters"


  def print_cluster_lens(self):
    for i,cluster in enumerate(self.clusters):
      print i, len(cluster)

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