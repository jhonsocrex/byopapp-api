
import numpy

from nearpy import Engine
from nearpy.hashes import RandomBinaryProjections

class PointCalculator():  
    
    def __init__(self, pointList, point):
        self.__configureCalculator(pointList, point)
        
    def __configureCalculator(self, pointList, point ):
        # Dimension of our vector space
        self.__dimension__ = 2 
        
        # Create a random binary hash with 10 bits
        self.__rbp__ = RandomBinaryProjections('rbp', 10)

        # Create engine with pipeline configuration
        self.__engine__ = Engine(self.__dimension__, lshashes=[self.__rbp__])
        self.setSearchingPointList( pointList )
        self.setQueryPoint(point)
        
    def __loadPointListInEngine(self):
        for index in xrange(0,len(self.__pointList__)):
            v = numpy.array(self.__pointList__[index])
            self.__engine__.store_vector(v, 'data_%d' % index)
    
    def setSearchingPointList(self, pointList ):
        self.__pointList__ = pointList
        self.__loadPointListInEngine()
        
    def setQueryPoint(self, point ):
        self.__point__ = point
    
    def getNearestPoint(self):
        return self.__engine__.neighbours(numpy.array(self.__point__))


    