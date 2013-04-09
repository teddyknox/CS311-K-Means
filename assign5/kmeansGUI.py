"""
A GUI for visualizing the KMeans algorithm.

author: David Kauchak
date: April, 2013
"""

from Tkinter import *
from datapoint import *
import kmeans

class KMeansGUI(Frame):
  """ A GUI for visualizing the KMeans algorithm. """

  # for displaying/distributing points over the space
  # of the window
  SCALAR = 10
  SIZE = 5 # the size of the points

  # possible cluster center colors
  COLORS = ["blue", "green", "red", "magenta", "yellow", "cyan"]

  def __init__(self, data, kmeans):
    """
    Create a new KMeansGUI visualizer.  data should be the same list of 
    DataPoints that were used to initialize the KMeans classifier.  kmeans
    should be a KMeans object that has NOT had the cluter method run yet.
    """
    self.parent = Tk()

    Frame.__init__(self, self.parent) 
    self.parent.geometry("450x450+300+300")

    self.kmeans = kmeans
    self.centers_to_id = {}
    self.initUI(data)

    self.parent.mainloop()  
    
  def initUI(self, data):
    """ Create the buttons and plot the original points in black. """ 
    self.parent.title("K-means clustering")    
    self.canvas = Canvas(self)
    self.pack(fill=BOTH, expand=1)
    
    # add the buttons
    centersButton = Button(self.parent, text="AssignToCenters", 
      command=self.assign_to_centers)
    centersButton.pack(side=RIGHT, padx=5, pady=5)
    
    stepButton = Button(self.parent, text="OneIteration",
      command = self.iterate)
    stepButton.pack(side=RIGHT, padx=5, pady=5)

    recalcButton = Button(self.parent, text="RecalculateCenters",
      command=self.recalculate_centers)
    recalcButton.pack(side=RIGHT, padx=5, pady=5)

    # draw the points and save their IDs
    self.data_to_id = {}

    for point in data:
      # should have x and y vals otherwise, this will fail
      x = point.get_val("x")
      y = point.get_val("y")

      id = self.canvas.create_oval(x*self.SCALAR, y*self.SCALAR, 
          x*self.SCALAR + self.SIZE, y*self.SCALAR + self.SIZE, 
          fill="black")

      self.data_to_id[str(point)] = id

    self.canvas.pack(fill=BOTH, expand=1)


  def iterate(self):
    """ Perform and update visuals for one iteration of k-means """
    self.assign_to_centers()
    self.recalculate_centers()

  def assign_to_centers(self):
    """ Perform the assign_to_centers step in k-means and update visual """
    self.kmeans.assign_to_centers()
    clusters = self.kmeans.get_clusters()

    for i in range(len(clusters)):
      for point in clusters[i]:
        # get the ID and update its color
        self.canvas.itemconfig(self.data_to_id[str(point)], fill=self.COLORS[i])
     
    self.canvas.pack(fill=BOTH, expand=1)

  def recalculate_centers(self):
    """ Perform the recalculate_centers step in k-means and update visual """
    self.kmeans.recalculate_centers()
    centers = self.kmeans.get_centers()

    # delete old centers
    for id_str in self.centers_to_id.keys():
      self.canvas.delete(self.centers_to_id[id_str])
      del self.centers_to_id[id_str]

    for i in range(len(centers)):
      center = centers[i]

      # should have x and y vals otherwise, this will fail
      x = center.get_val("x")
      y = center.get_val("y")

      id = self.canvas.create_rectangle(x*self.SCALAR, y*self.SCALAR,
        x*self.SCALAR+self.SIZE*2, y*self.SCALAR + self.SIZE*2,
        fill=self.COLORS[i])

      self.centers_to_id[str(center)] = id
    
    self.canvas.pack(fill=BOTH, expand=1)