from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import libstempo as t2
import libstempo.toasim as ts
import scipy.integrate as si
import glob
import sys
import os

import argparse

parser = argparse.ArgumentParser(description = 'Create GWB delay files')

# options
parser.add_argument('--sim', dest='sim', action='store', type=str, default='pop_e0',
                   help='Which simulation (default pop_e0)')
parser.add_argument('--pta', dest='pta', action='store', type=str, default='open1',
                   help='Which PTA (default open1)')
parser.add_argument('--Tspan', dest='Tspan', action='store', type=float, default=10,
                   help='Time span of observations [yr] (default 10 yr)')
parser.add_argument('--cadence', dest='cadence', action='store', type=float, default=26,
                   help='Cadence of observations[pt/yr] (default 26 pt/yr)')
parser.add_argument('--seed', dest='seed', action='store', type=float, default=55,
                   help='Random number seed (default 55)')

# parse arguments
args = parser.parse_args()


def get_redshifted_values(mc, z):
    """
    Return redshifted chirp mass and luminosity distance.
    
    :param mc: Chirp mass in Solar masses
    :param z: Redshift
    
    :returns: mc(1+z), dL
    """
    
    # constants
    H0 = 71 * 1000      # Hubble constant in (m/s)/Mpc
    Ol = 0.73           # Omega lambda
    Om = 0.27           # Omega matter
    G = 6.67e-11        # Gravitational constant in SI units
    c = 3.0e8           # Speed of light in SI units

    # proper distance function
    properDistance = lambda z: c/H0/np.sqrt(Ol+Om*(1+z)**3)
    
    # carry out numerical integration
    Dp = si.quad(properDistance, 0 ,z)[0]
    Dl = (1+z) * Dp
    
    return mc*(1+z), Dl 

def create_gw_delays(parfile, popfile, T=10, cadence=26, seed=55, outdir='./'):
    """
    Create a file with delays due to the summed GW sources
    from a population.
    
    :param pardir: parfile to be used for simulation
    :param popfile: name of the poulation file from Alberto's sims
    :param T: Timespan of simulated observations [yr]
    :param cadence: Cadence of observations [pts/yr]
    :param seed: Random number seed for binary orientation parameters
    :param outdir: Output directory to place delay files
    
    """
    
    if not os.path.exists(outdir):
        try:
            os.makedirs(outdir)
        except OSError:
            pass
    
    # read in data
    data = np.loadtxt(popfile)
    
    # get number of sources from file
    ns = data.shape[0]
    
    # set random number seed and draw orientation parameters
    np.random.seed(seed)
    
    theta = np.arccos(np.random.uniform(-1, 1, ns))
    phi = np.random.uniform(0, 2*np.pi, ns)
    psi = np.random.uniform(0, np.pi, ns)
    l0 = np.random.uniform(0, 2*np.pi, ns)
    gamma0 = np.random.uniform(0, 2*np.pi, ns)
    
    ###### initialize pulsar class #####
    
    # toas (evenly spaced)
    toas = np.linspace(0, T*3.16e7, int(T*cadence))
    toas /= 86400    # need to be in units of days
    toas += 53000    # start at MJD 53000
    
    # uncertainties (mu s) Don't matter here but need them for toasim
    err = np.ones(len(toas)) * 0.05
  
    # make fake observations
    psr = ts.fakepulsar(parfile, toas, err)
    
    # ideal toas
    ts.make_ideal(psr)
    
    # setup index array to grab values from datafile
    ind = np.array([0, 1, 2, 3, 4, 8])
    
    # write seed, T, and cadence to file
    np.savetxt(outdir + 'setup.txt', np.array([seed, T, cadence]))
    
    # open output file for source parameters
    fout = open(outdir + '/sources.txt', 'w')
    
    # loop over sources
    for ii in range(ns):
        
        # get values from file
        lmc, q, z, lf, e, inc = data[ii, ind]
        
        # get redshifted values
        mc, dl = get_redshifted_values(10**lmc, z)
        F = 10**lf/2
        
        # injection
        ts.add_ecc_cgw(psr, theta[ii], phi[ii], mc, dl, F, inc,
                       psi[ii], gamma0[ii], e, l0[ii], q, 
                       nmax=100, pd=1.0, psrTerm=True,
                       tref=53000*86400, check=False, 
                       useFile=True)
        
        
        # write parameters to file
        fout.write('%g %g %g %g %g %g %g %g %g %g %g\n' %
                   (theta[ii], phi[ii], np.log10(mc), np.log10(dl),
                    np.log10(F), inc, psi[ii], gamma0[ii], e,
                    l0[ii], q))
        
        sys.stdout.write('\r')
        sys.stdout.write('Finished %2.2f percent of Injections.' % ((ii+1)/ns * 100))
        sys.stdout.flush()
        
    fout.close()
    
    # save GW delays
    np.savetxt(outdir + '/' + psr.name + '_delay.txt',
               np.array([psr.stoas[:], psr.residuals()/86400]).T)   

# grab simulations and par files
sims = glob.glob('../models_sesana_7_6_2015/models_for_injection/' + args.sim + '/*')
parfiles = glob.glob('../parfiles/' + args.pta + '/*.par')

for sim in sims:
    s1 = sim.split('/')[-2]
    s2 = sim.split('/')[-1].split('.out')[0]
    outdir = '../delays/' + s1 + '/' + s2 + '/'
    for p in parfiles:
        create_gw_delays(p, sim, T=args.Tspan, cadence=args.cadence, 
                         seed=args.seed, outdir=outdir)
