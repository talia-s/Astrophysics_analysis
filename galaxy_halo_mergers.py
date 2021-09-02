#Press shift-enter to run this code
import matplotlib
import math
import numpy as np
import sys


#merger tree column descriptions
#scale(0) id(1) desc_scale(2) desc_id(3) num_prog(4) pid(5) upid(6) desc_pid(7) phantom(8) sam_mvir(9)
#mvir(10) rvir(11) rs(12) vrms(13) mmp?(14) scale_of_last_MM(15) vmax(16) x(17) y(18) z(19) vx(20) vy(21) vz(22)
#Jx(23) Jy(24) Jz(25) Spin(26) Breadth_first_ID(27) Depth_first_ID(28) Tree_root_ID(29) Orig_halo_ID(30) Snap_num(31)
#Next_coprogenitor_depthfirst_ID(32) Last_progenitor_depthfirst_ID(33) Last_mainleaf_depthfirst_ID(34)

#A few lines from a merger tree
rawtree = [
"1.0000 6441 0.0000 -1 2 -1 -1 -1 0 6.79700e+12 6.79700e+12 395.926000 100.895000 307.790000 1 0.4813 280.540000 32.70826 18.61240 12.03681 373.830 119.510 172.730 -1.808e+13 7.431e+13 -1.366e+13 0.14095 0 0 6441 35881 6800 63",
"0.9805 6442 1.0000 6441 1 -1 -1 -1 0 6.20900e+12 6.43200e+12 392.286000 141.459000 299.310000 1 0.4813 269.840000 32.63636 18.59150 11.99945 365.610 122.470 181.990 -1.648e+13 6.987e+13 -1.724e+13 0.15506 1 1 6441 33736 6800 62",
"0.9805 6791 1.0000 6441 1 6340 6442 -1 0 2.58200e+09 2.58200e+09 28.937000 3.426000 33.050000 0 0.0000 23.000000 32.51299 18.54580 11.78540 153.180 -32.520 373.550 3.600e+08 1.171e+08 -5.067e+08 0.81860 2 350 6441 33727 6800 62"
]

#turn the raw lines above into arrays of numbers
tree = np.array([np.fromstring(halo, dtype=float, sep=' ') for halo in rawtree])

#Print out halo IDs, halo descendant IDs, and halo masses
for halo in tree:
    print("Scale: %.3f; ID: %d -> %d; Mass: %.2e Msun/h" % (halo[0], halo[1], halo[3], halo[10])) 
    
#Merger tree columns:
#scale(0) id(1) desc_scale(2) desc_id(3) num_prog(4) pid(5) upid(6) desc_pid(7) phantom(8) sam_mvir(9)
#mvir(10) rvir(11) rs(12) vrms(13) mmp?(14) scale_of_last_MM(15) vmax(16) x(17) y(18) z(19) vx(20) vy(21) vz(22)
#Jx(23) Jy(24) Jz(25) Spin(26) Breadth_first_ID(27) Depth_first_ID(28) Tree_root_ID(29) Orig_halo_ID(30) Snap_num(31)
#Next_coprogenitor_depthfirst_ID(32) Last_progenitor_depthfirst_ID(33) Last_mainleaf_depthfirst_ID(34)

#If we use numpy's dtype, we can have it name all the fields for us:
#f4 is a real number; i8 is an integer
dt = np.dtype([('scale', 'f4'), ('id', 'i8'), ('desc_scale', 'f4'), ('desc_id', 'i8'), ('num_prog', 'i8'), 
               ('pid', 'i8'), ('upid', 'i8'), ('desc_pid', 'i8'), ('phantom', 'i8'), ('sam_mvir', 'f4'), 
               ('mvir', 'f4'), ('rvir', 'f4'), ('rs', 'f4'), ('vrms', 'f4'), ('mmp?', 'i8'), 
               ('scale_of_last_MM', 'f4'), ('vmax', 'f4'), ('x', 'f4'), ('y', 'f4'), ('z', 'f4'), ('vx', 'f4'), 
               ('vy', 'f4'), ('vz', 'f4'), ('Jx', 'f4'), ('Jy', 'f4'), ('Jz', 'f4'), ('Spin', 'f4'), 
               ('Breadth_first_ID', 'i8'), ('Depth_first_ID', 'i8'), ('Tree_root_ID', 'i8'), ('Orig_halo_ID', 'i8'), 
               ('Snap_num', 'i8'), ('Next_coprogenitor_depthfirst_ID', 'i8'), 
               ('Last_progenitor_depthfirst_ID', 'i8'), ('Last_mainleaf_depthfirst_ID', 'i8')])
                    
#This loads in the tree, skipping over the header lines as well as the first non-commented line,
#which has the total number of trees
print("Loading the trees... (this will take a few minutes)")
trees = np.loadtxt("tree_0_0_0.dat",skiprows=35,dtype=dt)

#it also takes forever, so let's save the tree as a binary file
np.save('tree.npy', trees)

#After the first time you run this, then you can comment out the loadtxt and save commands above and just do
trees = np.load('tree.npy')
print("Loaded the trees!")

#Let's grab just the halos at z=0 (a=1)
scale = 1
z0_halos = [x for (x) in trees if (x['scale']==1.0)]

print("There are", len(z0_halos), "halos at z=0")