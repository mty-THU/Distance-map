#!/usr/bin/env python
# coding: utf-8
"""
Created on Fri, 05 Mar 2021 20:07:37
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Bio.PDB import *
from scipy.spatial.distance import pdist, squareform

#Input PDBID
PDB_ID = input('Enter PDB ID:')

#Creat a pdbparser
p = PDBParser() 
io = PDBIO()
structure = p.get_structure('X', PDB_ID +'.pdb')
model = structure[0]

#Extract each chain information and save it to a PDB file
for chain in structure.get_chains():
        io.set_structure(chain)
        io.save(chain.get_id() + '.pdb')
        print('This protein has chain:' + chain.get_id())

#Select a chain to analyse
chain_choose = input('Select the chain to be analyzed:')

#Extract atomic coordinates 
arry_coor = []

for residue in model[chain_choose]:
    if residue.has_id('CB'):
        for atom in residue:
            if atom.get_name() == "CB":
                x = atom.get_coord()
                arry_coor.append({'X':x[0],'Y':x[1],'Z':x[2]})
                break
    else:
        if residue.has_id('CA'):
            for atom in residue:
                if atom.get_name() == "CA":
                    x = atom.get_coord()
                    arry_coor.append({'X':x[0],'Y':x[1],'Z':x[2]})
                    break
                else:
                    continue
                        
#Transform array to dataframe
atom_coor = pd.DataFrame(arry_coor)

#Calculate the distance matrix
distance_matrix = squareform(pdist(atom_coor))

#Draw the heat map
def heatmap(matrix):
    plt.imshow(matrix,cmap='viridis')
    plt.colorbar()
    plt.savefig(PDB_ID + '_' + chain_choose)

heatmap(distance_matrix)
