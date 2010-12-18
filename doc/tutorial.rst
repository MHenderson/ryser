.. Matthew Henderson, 18 December 2010

Tutorial
========

Completing partial latin squares
--------------------------------

Consider the following partial latin square.

.. math::
    
    \begin{array}{|c|c|c|}
      \hline a & . & c \\
      \hline b & c & . \\
      \hline . & a & b \\ \hline
    \end{array}

To make use of Rysa components for completing partial latin squares, you first
need to know how to create partial latin squares. The components for building
partial latin square objects lie in the :py:mod:`designs` module. So, we need to 
make names from that module available in the current workspace::

    >>> from rysa import designs
     
To build a partial latin square object we use a dictionary mapping cell labels
to symbols. The mapping is completely general, you can use whatever labels you
like and whatever symbols you like::     
     
    >>> P = { (0,0): 'a', (0,2): 'c', (1,0): 'b', (1,1): 'c', (2,1): 'a', (2,2): 'b' }
           
With this data in place we can now build a partial latin square object::
    
    >>> designs.latin(P, 3)
     
Notice how the dimensions of the latin square are given as a parameter to the
constructor.      

As an alternative, we can construct partial latin squares from strings::

    >>> S = 'a.cbc..ab'
    >>> designs.latin(S, 3, input = 'string', empty = '.') 

Testing Hall's condition in the cloud
-------------------------------------

In this section we demonstrate how to use cloud computing components to decide
whether Hall's condition is satisfied for a certain partial latin square.

Completing sudoku puzzles
-------------------------

In this section we discuss completing sudoku puzzles.

Enumerating shidoku puzzles
---------------------------

In this section we build a simple experiment script to enumerate shidoku.

Embedding latin rectangles
--------------------------

In this section we discuss embedding latin rectangles.

Constructing magic squares
--------------------------

In this section we discuss magic squares.

