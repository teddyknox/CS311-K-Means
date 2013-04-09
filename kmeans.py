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

    #########
    # TODO: Add your code to initialize the K-means cluster

  def cluster(self, iterations=INFINITY):
    """
    Cluster the data and return the found clusters.

    By default, the clustering will continue until the clusters converge,
    i.e. don't change. Optionally, you can specify a fixed number of iterations.
    """

    #########
    # TODO: code to run k-means

  def assign_to_centers(self):
    """
    Assign the points to the cluster centers.  This will
    update the clusters.
    """
    #########
    # TODO: code to reassign data points

  def recalculate_centers(self):
    """
    Recalculte the cluster centers based on the current clusters.
    """
    #########
    # TODO: code to recalculate centers


  def get_clusters(self):
    """
    Return the current clustering of the data.  The data structure
    returned should be a list of lists, specifically each cluster
    will be represented as a list of DataPoints and you'll be returning
    a list of clusters.
    """

    #########
    # TODO


  def get_centers(self):
    """ Return the current cluster centers as a list of DataPoints. """

    #########
    # TODO