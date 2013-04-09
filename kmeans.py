"""
k-means clusterer

author: David Kauchak
date: April, 2013
"""

from random import randint

class KMeans:
  """
  A class for doing k-means clustering of a data set
  """

  INFINITY = 1.0e400

  # constants for different distance measures
  EUCLIDEAN = 1
  COSINE = 2

  def __init__(self, data, k, distance_metric=EUCLIDEAN):
    """
    Create a new k-means cluster to cluster *data* into *k*
    clusters.  By default the clustering will use euclidean
    distance, but cosine distance can also be used.

    data should be a list of DataPoints.

    clustering does NOT begin until the cluster method is called.
    """

    cls = self.clusters = []
    cens = self.centers = []

    cluster_indexes = []
    num_points = len(data)
    possible_indexes = range(num_points)

    for i in range(k):
      cls.append([])
      which_index = randint(0, num_points-i)
      cens.append(data[possible_indexes[which_index]])
      possible_indexes.remove(which_index)

    cls[0] = data

  def cluster(self, iterations=INFINITY):
    """
    Cluster the data and return the found clusters.

    By default, the clustering will continue until the clusters converge,
    i.e. don't change. Optionally, you can specify a fixed number of iterations.
    """

    for i in xrange(iterations):
      self.assign_to_centers()
      self.recalculate_centers()

  def assign_to_centers(self):
    """
    Assign the points to the cluster centers.  This will
    update the clusters.
    """

    points = sum(self.clusters, [])
    new_clusters = [[] for x in range(len(self.clusters))] # blank clusters

    for point in points:
      min_dist = INFINITY
      min_k = -1
      for x, center in enumerate(self.centers):
        dist = center.euclidean(point)
        if dist < min_dist:
          min_dist = dist
          min_k = x
      new_clusters[min_k].append(point)
    self.clusters = new_clusters 

  def recalculate_centers(self):
    """
    Recalculte the cluster centers based on the current clusters.
    """
    new_centers = []
    for cluster in clusters:
      dim_totals = {}
      for point in cluster:
        for key in point:
          if key in dim_totals:
            dim_totals[key] += point[key]
          else:
            dim_totals[key] = point[key]
        for key in dim_total:
          dim_total[key] = float(dim_total[key])/len(cluster)
      new_centers.append(DataPoint(dim_total))


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