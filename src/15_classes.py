# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon: 
    lat = 0.0
    lon = 0.0
      
    # parameterized constructor 
    def __init__(self, la, lo): 
        self.lat = la 
        self.lon = lo 
      
    def display(self): 
        print("Latitude = " + str(self.lat)) 
        print("Longitude = " + str(self.lon)) 
  
x = LatLon(41.70505, -121.51521)
#x.display()

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLon): 
    name = ""

    def __init__(self, la, lo, name):
        LatLon.__init__(self, la, lo)
        self.name = name
    
    def display(self): 
        print("Name = " + str(self.name)) 
        LatLon.display(self)

    def __str__(self):
        return("Name: " + self.name + ", Lat: " + str(self.lat) + ", Long: " + str(self.lon))

wp = Waypoint(41.999, -121.999, "somewhere")
#wp.display()

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
waypoint = Waypoint(41.70505, -121.51521, "Catacombs")

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE

# Print it--also make this print more nicely
# didn't feel like doing it right now
# print(geocache)
