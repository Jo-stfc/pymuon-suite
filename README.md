# pymuon-suite
Collection of scripts and utilities for muon spectroscopy.

## Installation

Requires Python 3.7+. Install with pip or conda:

`pip install pymuonsuite`

`conda install pymuonsuite`

## Command line scripts

The following is a list of currently supported command line scripts. For any
of them, use `<script> --help` to see usage information.

* `pm-muairss`: generates a number of random muon structures for AIRSS
optimisation using Poisson spheres distribution and different calculators, as well as carries out their clustering analysis after the calculations have been done. Usage is `pm-muairss <structure file> <parameter file>`, with the additional option `-t w` when one desires to generate the structures instead of analysing the results. This is done to help avoid overwriting one's results by mistake;
* `pm-muairss-gen`: alias for `pm-muairss` with the `-t w` option on;
* `pm-uep-opt`: Unperturbed Electrostatic Potential optimisation for a single muon in a unit cell; it's used as `pm-uep-opt <parameter file>`;
* `pm-uep-plot`: Unperturbed Electrostatic Potential plotting for a given unit cell and specific lines or planes along it; it's used as `pm-uep-plot <parameter file>`;
* `pm-symmetry`: analyses the symmetry of a structure with `spglib` and identifies the Wyckoff points, which ones are occupied, and which ones can be uniquely identified as being extrema rather than saddle points, thus providing some candidates for stopping sites in crystals; it's used as `pm-symmetry <structure file>`;
* `pm-asephonons`: compute phonons for the given structure using ASE and DFTB+;
* `pm-nq`: generates input files for quantum effects using a phonon
approximation or analyses the results (work in progress)

For more in-depth information about each tool and their usage, [check the Wiki](https://github.com/muon-spectroscopy-computational-project/pymuon-suite/wiki).
