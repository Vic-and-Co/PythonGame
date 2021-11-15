'''
The world class: dictates the stages/ areas
'''

class World:
    def __init__(self, area):
        self.area = 0 #0 pertains to starting area, other stages are their individual stage numbers
        
        #Detection Boundaries
        self.upSquare = 0