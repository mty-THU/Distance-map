# Distance-map
This is a script that I am using to make a distance map for the selected chain.

The script reads the selected PDB file, extracts the information for each chain, and creates a new PDB file for it.

Select the chain to be analyzed and draw the distance map. 

Principle: If a residue has CB atom, use CB atom; otherwise, use Ca atom. If the residue does not have CB and Ca atoms, ignore this residue.

## How to use
Put the script(Distance map.py) in the same directory as the PDB files, and run the script with
‘python Distance map.py’
