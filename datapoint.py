"""
Representation for a data point.  Two classes:
- DataPoint: a generic data Representation
- WordDataPoint: an extension of DataPoint to handle "documents" data points

Author: David Kauchak
Date: April, 2013
"""

import math
import re
import random

class DataPoint:
  """
  Sparse representation of a data point.
  """
  # Because these should be here
  EUCLIDEAN = 1
  COSINE = 2

  def __init__(self, sparse_vector = None):
    """
    Create a new data point.

    If no dictionary is specified, creates an empty data point.

    If a dictionary is specified, creates a sparse data point.  The supplied
    dictionary specifies a mapping from dimension name/feature to value.  For example:
      DataPoint(dict(x=1, y=1))

    would create a sparse vector with x=1 and y=1.
    """

    if sparse_vector:
      self.counts = sparse_vector
    else:
      self.counts = {}

    self.set_length()

  def __str__(self):
    return str(self.counts)

  def __eq__(self, other):
    return self.counts == other.counts

  def __ne__(self, other):
    return self.counts != other.counts  

  def get_val(self, dimension):
    """
    Get the value of a particular dimension, e.g.:
    d = DataPoint(dict(x=1, y=2))
    d.get_val("x") # would return 1
    """
    return self.counts[dimension]

  def set_length(self):
    """ 
    Calculate the L2 length of this data point if the data point were interpreted
    as a vector.  Specifically, self.length = \sqrt(\sum xi^2)

    This generally should NOT be called outside this class.
    """

    # calculate the length
    self.length = 0

    for key in self.counts:
      self.length += self.counts[key]**2

    self.length = math.sqrt(self.length)

  def add_data_counts(self, other_point):
    """
    Add the DataPoint other_point to this DataPoint

    This is done by adding each individual dimensions
    """

    for key in other_point.counts:
      self.counts[key] = self.counts.get(key, 0) + other_point.counts[key]

    self.set_length()

  def divide_by_constant(self, val):
    """
    Divide each dimension in this data point by val
    """

    for key in self.counts:
      self.counts[key] /= float(val)

    self.set_length()

  def distance(self, other_point, distance_metric):
    if distance_metric == self.EUCLIDEAN:
      fn = self.euclidean_distance
    elif distance_metric == self.COSINE:
      fn = self.euclidean_distance

    return fn(other_point)

  def cosine_distance(self, other_point):
    """ return the cosine distance between this point and other_point """

    sum = 0

    # do the distance from the shorter of the two
    if len(self.counts) < len(other_point.counts):
      short = self.counts
      long = other_point.counts
    else:
      short = other_point.counts
      long = self.counts

    for key in short:
      if key in long:
        # intersection
        sum += short[key] * long[key]

    # return 1 - the cosine similarity to get a distance metric
    return 1 - float(sum)/(self.length * other_point.length)

  def euclidean_distance(self, other_point):
    """ return the euclidean distance between this point and other_point """

    #########
    # TODO: fill in the euclidean distance metric calculating the distance
    #       between this point and another point. The actual values for 
    #       a data point are stored in a dictionary called "counts".  You
    #       can look at cosine_distance to see an example of how you can
    #       calculate the distance metric.  However, *BE CAREFUL*, the cosine
    #       distance only needs to look at those dimensions that are non-zero
    #       for BOTH points (i.e. intersection).  For the euclidean measure, 
    #       you will need to look at  those dimensions that are non-zero for 
    #       EITHER of the points (i.e. union).
    #
    #       Make sure you understand this distinction and how we are representing
    #       the data points.

    sum = 0

    # do the distance from the shorter of the two
    if len(self.counts) < len(other_point.counts):
      short = self.counts
      long = other_point.counts
    else:
      short = other_point.counts
      long = self.counts

    for key in long:
      if key in short:
        # intersection
        sum += ((short[key] - long[key]) ** 2)
      else:
        sum += (long[key] ** 2)
    for key in short:
      if key in long:
        sum += 0
      else:
        sum += (short[key] ** 2)


    # return 1 - the cosine similarity to get a distance metric
    return math.sqrt(sum)

class WordDataPoint(DataPoint):
  """
  An extension of DataPoint that allows a data point to be created
  from a list of words.  The data point consists of frequency counts
  for the words.
  """

  def __init__(self, words, label=""):
    """
    Create a new data point using a list of words.  You may optionally
    specify the class label.  This does not change the representation,
    but stores it for later use if you want to check the quality of a
    clustering by examining the mix of the different classes/labels within
    a cluster.
    """

    self.counts = {}
    self.label = label

    for word in words:
      self.counts[word] = self.counts.get(word, 0) + 1

    self.set_length()

  def __str__(self):
    return "Counts: " + str(self.counts)

  def get_label(self):
    """ Get the label/class associated with this data point """
    return self.label


# --------------------------------------
# Helper functions
# 
def gen_random_data(num_centers, num, min=0, max=40, sigma=2):
  """
  Generates *num* points around *num_centers* distributed as a
  gaussian with deviation *sigma*.  min and max specify the range
  for the cluster centers.
  """
  # pick the random centers
  centers = []

  for i in range(num_centers):
      centers.append([random.randint(min+3*sigma, max-3*sigma), 
        random.randint(min+3*sigma, max-3*sigma)])

  data = []

  for i in range(num):
    # pick a random center
    center = centers[random.randint(0, len(centers)-1)]

    # generate a random point around this center
    x=random.gauss(center[0], sigma)
    y=random.gauss(center[1], sigma)

    while x < min and x > max and y < min and y > max:
      x=random.gauss(center[0], sigma)
      y=random.gauss(center[1], sigma)
    
    data.append(DataPoint(dict(x=x, y=y)))

  return data