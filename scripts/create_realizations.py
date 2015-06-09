from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import libstempo as t2
import libstempo.toasim as ts
import glob
import sys
import os

import argparse

parser = argparse.ArgumentParser(description = 'Create simulated tim files with GWB')

# options
parser.add_argument('--delaydir', dest='delaydir', action='store', type=str, 
                    required=True, help='Full path to delay files')
parser.add_argument('--pta', dest='pta', action='store', type=str, default='open1',
                   help='Which PTA (default open1)')
parser.add_argument('--rms', dest='rms', action='store', type=float, default=100,
                   help='White Noise RMS [ns] (default 100 ns')
parser.add_argument('--seed', dest='seed', action='store', type=float, default=55,
                   help='Random number seed for noise (default 55)')

# parse arguments
args = parser.parse_args()

# read in delay files
delays = glob.glob(args.delaydir + '/*_delay.txt')

# read in par files
parfiles = glob.glob('../parfiles/' + args.pta + '/*.par')

# sort
delays.sort()
parfiles.sort()

# make directory for par and tim files
sim = args.delaydir.split('/')[-2]
real = args.delaydir.split('/')[-1]
outdir = '../mock_data/' + args.pta + '/' + sim + '/' + real + '/'
if not os.path.exists(outdir):
        try:
            os.makedirs(outdir)
        except OSError:
            pass


for d, p in zip(delays, parfiles):
    print 'Using {0} delay with parfile {1}.'.format(d.split('/')[-1], p.split('/')[-1])

    d = np.loadtxt(d)
    toas, res = d[:,0], d[:,1]

    err = np.ones(len(toas)) * args.rms * 1e-3

    # make fake observations
    psr = ts.fakepulsar(p, toas, err)

    # makes perfect residuals (i.e. no noise)
    ts.make_ideal(psr)

    # add GWB delays
    psr.stoas[:] += res
    
    # adds white noise at level of defined uncertainties above
    ts.add_efac(psr, 1, seed=args.seed)

    # fit
    psr.fit()

    # save par and tim file
    psr.savepar(outdir + '/' + psr.name + '.par')
    psr.savetim(outdir + '/' + psr.name + '.tim')
