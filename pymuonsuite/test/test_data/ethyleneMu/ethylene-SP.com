%chk=ethylene-SP.chk
%nprocshared=16
#P B3LYP/EPR-III

Gaussian input prepared by ASE

0 2
C       0.00000000       0.00000000       0.66748000 
C       0.00000000       0.00000000      -0.66748000 
H       0.00000000       0.92283200       1.23769500 
H       0.00000000      -0.92283200       1.23769500 
H       0.00000000       0.92283200      -1.23769500 
H       0.00000000      -0.92283200      -1.23769500
TV 		10 				0					0
TV      0				10					0
TV		0				0					10 

