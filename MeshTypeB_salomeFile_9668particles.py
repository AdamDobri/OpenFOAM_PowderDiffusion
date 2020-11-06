#!/usr/bin/env python

###
### This file is generated automatically by SALOME v9.4.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()
sys.path.insert(0, r'H:/Powders/salomeGeometries')

###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS
import time
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Start Time =", current_time)

x=[]
y=[]
z=[]
R=[]
import csv
with open(r'H:/Powders/salomeGeometries/sphereLocations.csv','r') as myFile:
  lines=csv.DictReader(myFile, delimiter=' ')
  for line in lines:
    x.append(line['xPos'])
    y.append(line['yPos'])
    z.append(line['zPos'])
    R.append(line['Radius'])

x = list(map(float,x)) 
y = list(map(float,y)) 
z = list(map(float,z)) 
R = list(map(float,R)) 

X = .8
Y = .8
Z = 1.6

geompy = geomBuilder.New()
   
O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
outerBox = geompy.MakeBoxDXDYDZ(X, Y, Z)
before = outerBox

Vertices = []
Spheres = []
Subgroups = []

stepSize = 500

t0= time.clock()
for jj in range(0,9001-stepSize,stepSize):
    t0i = time.clock()
    for ii in range(jj,jj+stepSize,1): 
        Vertices.append(geompy.MakeVertex(x[ii],y[ii],z[ii]))
        Spheres.append(geompy.MakeSpherePntR(Vertices[ii],R[ii]))
    Subgroups.append(geompy.MakeFuseList(Spheres[jj:jj+stepSize], False, False))
    
    t1=time.clock()
    print('Subgroup'  + str(jj) + ' to ' + str(jj+stepSize-1) + ' elapsed time = ', t1-t0i)

t0i = time.clock()
for ii in range(9000,9668,1): 
    #print(ii)
    Vertices.append(geompy.MakeVertex(x[ii],y[ii],z[ii]))
    Spheres.append(geompy.MakeSpherePntR(Vertices[ii],R[ii]))
Subgroups.append(geompy.MakeFuseList(Spheres[9000:9668], False, False))
t1=time.clock()
print('Subgroup'  + str(9000) + ' to ' + str(9668) + ' elapsed time = ', t1-t0i)
    
tf = time.clock()
print("Elapsed time (pre Boolean Cut): ", tf - t0 )
poreSpace = geompy.MakeCutList(outerBox, Subgroups, False)
tt = time.clock()
print("Boolean Elapsed Time: ", tt - tf )
print("Total Elapsed Time: ", tt - t0 )



geompy.ExportBREP(poreSpace, "H:/Powders/salomeGeometries/poreSpaceFull.brep" )

#now = datetime.now()
#current_time = now.strftime("%H:%M:%S")
#print("Export Completion at =", current_time)

if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
# 250, one shot = 0:31
# 500, one shot = 2:13
# 750, one shot = 6:30
# 1000, one shot = 12:30
# 1250, one shot = 18:19