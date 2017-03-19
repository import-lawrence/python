#!/usr/bin/env python

"""
Generates data with periodicity
"""
from random import randint

temp = 0
abs_max_temp = 100
max_period = 180
offset = 0

num_cyls = 0
num_cyls_added = 12

cylinder_profile = []
#id, periodicity, start phase, current phase, max_temp


for nidx in range(0, num_cyls_added) :

  period = randint(0,max_period)
  if (period < 30) :
    period = 0
    phase_offset = 0
  else :
    phase_offset = randint(0,period)

  max_temp = randint(0,abs_max_temp)

  cylinder_profile.append([ nidx, period, phase_offset,phase_offset, max_temp ])

  print "cyl %d , period %d, offset %d, max_temp %d" % (nidx, period, phase_offset, max_temp )


num_days = 360

for didx in range(0,num_days):

  for cidx in range(0,num_cyls + num_cyls_added):

    if ( cylinder_profile[cidx][1] == 0 ) :
      #Generate temp for an aperiodic cylinder
      max_temp =  cylinder_profile[cidx][4]
      temp = randint(0,max_temp)
    else :
      #Generate temp for a periodic cylinder
      period = cylinder_profile[cidx][1]
      cur_phase = cylinder_profile[cidx][3]
  

      if (cur_phase < period/2) :
        offset = cur_phase 
      else:
        offset = period - cur_phase 

      if (period == cur_phase) :
        # roll over
        cylinder_profile[cidx][3] = 0
      else :
        cylinder_profile[cidx][3] += 1
     
  
      max_temp =  cylinder_profile[cidx][4]
      temp = max_temp - offset 
      if (max_temp < offset ) :
        temp = 0
      else :
        temp = max_temp - offset 

      #print " period %d, offset %d, temp %d" %(period, offset, temp) 
   

    # Convert day to date

    print "%d,%d,%d" % (cidx,temp,didx)


