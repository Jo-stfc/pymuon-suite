"""
Author: Simone Sturniolo and Adam Laverack
"""

# Python 2-to-3 compatibility code
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import random

import numpy as np
import scipy.constants as cnst
from ase import Atoms

def calc_wavefunction(R, grid_n, write_table = True, filename = ''):
    """
    Calculate harmonic oscillator wavefunction

    | Args:
    |   R(Numpy float array, shape:(axes)): Displacement amplitude along each
    |       axis
    |   grid_n(int): Number of grid points along each axis
    |   write_table: Write out table of probability densities in format:
    |       Displacement | Prob. Density
    |   filename (str): Filename of file to write to, required for write_table
    |
    | Returns:
    |   prob_dens (Numpy float, shape:(grid_n*3)): Probability density of
    |       harmonic oscillator at each displacement
    """
    R_axes = np.array([np.linspace(-3*Ri, 3*Ri, grid_n)
                       for Ri in R])

    # Wavefunction
    psi_norm = (1.0/(np.prod(R)**2*np.pi**3))**0.25
    # And along the three axes
    psi = psi_norm*np.exp(-(R_axes/R[:, None])**2/2.0)
    # Save the densities
    if write_table:
        psi_table = np.concatenate(
            (R_axes, psi**2), axis=0)
        np.savetxt(filename, psi_table.T)
    # And average
    r2psi2 = R_axes**2*np.abs(psi)**2

    # Convert to portable output format
    prob_dens = np.zeros((grid_n*3))
    for i, axis in enumerate(r2psi2):
        for j, point in enumerate(axis):
            prob_dens[j + i*grid_n] = point

    return prob_dens

def tl_disp_generator(norm_coords, evecs, num_atoms):
    displacements = np.zeros((num_atoms, 3))
    coefficients = np.zeros(np.size(norm_coords))
    for i in range(np.size(coefficients)):
        coefficients[i] = random.choice([-1, 1])
    therm_line = norm_coords*coefficients

    for atom in range(num_atoms):
        for mode in range(np.size(norm_coords)):
            displacements[atom] += therm_line[mode]*evecs[mode][atom].real*1e10

    return displacements

def weighted_tens_avg(tensors, weight):
    """
    Given a set of 3x3 tensors resulting from the sampling of a property on an
    N point grid for a set of atoms, calculate a weighted average of the tensors
    for each atom using a given weight for each grid point.

    | Args:
    |   tensors(Numpy float array, shape:(N,Atoms,3,3)): For each grid point,
    |       a set of 3x3 tensors for each atom.
    |   weight(Numpy float array, shape:(N)): A weighting for each point
    |       on the grid.
    |
    | Returns:
    |   tens_avg(Numpy float array, shape:(Atoms,3,3)): The averaged tensor for
    |       each atom.
    """
    num_atoms = np.size(tensors, 1)
    tens_avg = np.zeros((num_atoms, 3, 3))
    tensors = tensors*weight[:, None, None, None]
    for i in range(num_atoms):
        tens_avg[i] = np.sum(tensors[:, i], axis=0)/np.sum(weight)
    return tens_avg

def wf_disp_generator(disp_factor, maj_evecs, grid_n):
    """
    Generate a set of displacements of an atom for the wavefunction sampling
    method.

    | Args:
    |   disp_factor(float(3)): A displacement factor for each of the 3 major
    |       phonon modes of the atom.
    |   maj_evecs(Numpy float array(3, 3)): The eigenvectors of the 3 major
    |       phonon modes of the atom.
    |   grid_n(int): The number of desired grid points along each mode.
    |
    | Returns:
    |   displacements(Numpy float array(grid_n*3, 3)): Array containing the
    |       amount the atom should be displaced by at each grid point. The first
    |       <grid_n> elements are for the first mode, the second <grid_n> for
    |       the second mode, etc.
    """
    displacements = np.zeros((grid_n*3, 3))
    max_disp = 3*maj_evecs*disp_factor[:, None]
    for mode in range(3):
        for n, t in enumerate(np.linspace(-1, 1, grid_n)):
            displacements[n + mode*grid_n] = t*max_disp[mode]

    return displacements
