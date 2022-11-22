#!/usr/bin/env python
# coding: utf-8

# # Three Reservoirs 
# 
# This example illustrates loading a background image in addition to building a model.
# 
# ## Problem Statement
# 
# Reservoirs A, B, and C are connected as shown
# 
# ![](p230.bmp)
# 
# The water elevations in reservoirs A, B, and C are 100 m, 80 m, and 60 m.   The three pipes connecting the reservoirs meet at junction J, with pipe AJ being 900 m long, BJ being 800 m long, and CJ being 700 m long.  The diameters of all the pipes are
# 850 mm.  If all the pipes are ductile iron, and the water temperature is 293$^o$K, find the direction and magnitude of flow in each pipe.
# 
# :::{note}
# This problem is identical to Chin Problem 2.30, Pg. 92
# :::   
# 
# ## Start EPANET
# 
# FIGURE HERE
# 
# ## Set Defaults
# 
# ## Load the Background Image
# 
# FIGURE HERE
# 
# ## Add Node-Type Elements
# - Select the reservoir tool.  Put three reservoirs on the map.
# - Select the node tool, put a node on the map. **EPA NET needs one node!**
# 
# FIGURE HERE
# 
# ## Add Link-Type Elements
# - Select the link (pipe) tool, connect the three reservoirs to the node.
# 
# FIGURE HERE
# 
# ## Edit hydraulic element properties to parameterize the model
# - Set the total head each reservoir.
# - Set the pipe lengths, diameters, and roughness height.
# 
# FIGURE HERE
# 
# ## Save the input file and Run the program.   
# - Query the pipe and find the computed flow. 
# 
# FIGURE HERE
# 
# The pipes were originally straight segments, but a drawing tool in EPANET can be used to follow the shape of the underlying basemap.  The flowrates are in liters-per-second, divide by 1000 to obtain cubic-meters-per-second.
# 
# ## References
# 
# ## Data Files
# 
# ## Videos
# 

# In[ ]:




