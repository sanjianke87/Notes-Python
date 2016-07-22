#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Cut SAC files before reading in ObsPy
#

from obspy import read

# first read SAC head only
st = read('obspy-cut-read-example.sac', headonly=True)
# Convert time marker T0 into UTCDateTime
T0 = st[0].stats.starttime - st[0].stats.sac.b + st[0].stats.sac.t0
# Read waveforms between T0 and T0+2
st += read('obspy-cut-read-example.sac', starttime=T0, endtime=T0+2)
st.plot()
