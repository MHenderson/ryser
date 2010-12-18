.. Matthew Henderson, 18 December 2010

Tutorial
========

Completing partial latin squares
--------------------------------

To make use of RYSA components for completing partial latin squares, you first
need to know how to create partial latin squares. The components for building
partial latin square objects lie in the rysa.designs module. So, we need to 
make names from that module available in the current workspace::

     import rysa.designs
     
To build a partial latin square object we use a dictionary mapping cell labels
to symbols. The mapping is completely general, you can use whatever labels you
like and whatever symbols you like::     
     
     P = { (0,0): 'a', (0,1): '.', (0,2): 'c', \
           (1,0): 'b', (1,1): 'c', (1,2): '.', \
           (2,0): '.', (2,1): 'a', (2,2): 'b' }
           
With this data in place we can now build a partial latin square object::

     rysa.designs.latin(self.P, (3, 3), empty = '.')
     
Notice how the dimensions of the latin square are given as a parameter to the
constructor.      

As an alternative, we can construct partial latin squares from strings.          
     
Completing Sudoku puzzles
-------------------------

Embedding latin rectangles
--------------------------

Constructing magic squares
--------------------------

