#!/usr/bin/env python
# coding: utf-8

# # Flow Between Two Reservoirs
# 
# This example represents the situation where the total head is known at two points on a pipeline, and one wishes to determine the flow rate (or specify a flow rate and solve for a pipe diameter).   Like the prior example it is contrived, but follows the same general modeling process.
# 
# ## Problem Statement
# 
# > Using the Moody chart, and the energy equation, estimate the diameter of a cast-iron pipe needed to carry 60$^o$F water at a discharge of 10 cubic-feet per second (cfs) between two reservoirs 2 miles apart.  The elevation difference between the water surfaces in the two reservoirs is 20 feet.
# 
# As in the prior example, we will need to specify the pipe roughness terms, then solve by trial-and-error for the diameter required to carry the water at the desired flowrate.  Page 31 of the EPANET manual suggests that the roughness height for cast iron is 0.85 millifeet.
# 
# As before the steps to model the situation are:
# 
# ## Start EPANET
# 
# FIGURE HERE
# 
# ## Set defaults
# 
# FIGURE HERE
# 
# ## Add Node-Type Elements
# - Select the reservoir tool.  Put two reservoirs on the map.
# 
# FIGURE HERE
# 
# - Select the node tool, put a node on the map. **EPA NET needs one node!**
# 
# FIGURE HERE
# 
# ## Add Link-Type Elements
# - Select the link (pipe) tool, connect the two reservoirs to the node.  One link is the 2 mile pipe, the other is a short large diameter pipe (negligible head loss).
# 
# FIGURE HERE
# 
# ## Edit hydraulic element properties to parameterize the model
# - Set the total head each reservoir.
# - Set the pipe length and roughness height in the 2 mile pipe.
# - Guess a diameter.
# 
# FIGURE HERE
# 
# ## Save the input file and Run the program.   
# - Query the pipe and find the computed flow. 
# 
# FIGURE HERE
# 
# :::{note}
# If the flow is too large reduce the pipe diameter, if too small increase the pipe diameter.  Stop when within a few percent of the desired flow rate.  Use commercially available diameters in the trial-and-error process, so exact match is not anticipated.
# :::
# 
# ## References
# 
# ## Data Files
# 
# ## Videos
# 
# 

# In[ ]:




