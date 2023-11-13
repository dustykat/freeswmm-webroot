#!/usr/bin/env python
# coding: utf-8

# # Flow in a Single Pipe
# 
# A simple model to consider is from a typical pipeline exercise in most hydraulics books.
# 
# > A 5-foot diameter, enamel coated, steel pipe carries 60$^o$F water at a discharge of
# 295 cubic-feet per second (cfs). Using the Moody chart, estimate the head loss
# in a 10,000 foot length of this pipe
# 
# In EPA-NET we will start the program, build a tank-pipe system and find the head loss in
# a 10,000 foot length of the pipe. The program will compute the friction factor for us (and
# we can check on the Moody chart if we wish).
# 
# The main trick in EPA-NET is going to be the friction coefficient, in the EPA-NET manual
# on page 30 and 31, the author indicates that the program expects a roughness coefficient
# based on the head loss equation. The units of the roughness coefficient for a steel pipe are
# $0.15 \times 10^{−3}$ feet. On page 71 of the user manual the author states that roughness coefficients
# are in millifeet (millimeters) when the Darcy-Weisbach head loss model is used. So keeping
# that in mind we proceed with the example.
# 
# ## Start the Program
# 
# Figure 1 is a screen capture of the EPA-NET program after installing the program. The
# program starts as a blank slate and we will select a reservoir and a node from the tool bar
# at the top and place these onto the design canvas.
# 
# FIGURE HERE
# 
# ## Set Defaults
# 
# Figure 1 is a screen capture of the EPA-NET program after setting defaults for the simulation.
# Failure to set correct units for your problem are sometimes hard to detect (if the model runs),
# so best to make it a habit to set defaults for all new projects. 
# 
# FIGURE HERE
# 
# ## Add Node-type elements
# 
# Next we add the reservoir and the node. Figure 3 is a screen capture after the reservoir and node are placed. 
# 
# FIGURE HERE
# 
# We will specify a total head at the reservoir (value is unimportant as long as it is big enough to overcome
# the head loss and not result in a negative pressure at the node. We will specify the demand at the node equal to the desired flow in the pipe.
# 
# :::{note}
# This is probably not the usual way to specify a demand value, but in this case we are trying to force a particular flowrate
# :::
# 
# ## Add Link-type elements
# 
# Next we will add the pipe. Figure 4 is a screen capture after the pipe is placed. 
# 
# FIGURE HERE
# 
# The sense of flow in this example is from reservoir to node, but if we had it backwards we could either accept a negative flow in
# the pipe, or right-click the pipe and reverse the start and end node connections.
# 
# ## Edit hydraulic element properties to parameterize the model
# 
# Now we can go back to each hydraulic element in the model and edit the properties. We supply pipe properties (diameter, length, roughness height) as in Figure 5.
# 
# FIGURE HERE
# 
# :::{note}
# With a little experience the creates and edits can be done at the same time
# :::
# 
# We supply the reservoir total head as in Figure 6
# 
# FIGURE HERE
# 
# We set the demand node elevation and the actual desired flow rate as in Figure 7.
# 
# FIGURE HERE
# 
# ## Save all the inputs and Run the Simulation
# The program is now ready to run, next step would be to save the input file (File/Save/Name), then run the program.
# 
# Run the program by selecting the lighting bolt looking thing (kind of channeling Zeus here) and the program will start. If the nodal connectivity is OK and there are no computed negative pressures the program will run. Figure 8 is the appearance of the program after
# the run is complete (the annotations are mine!). 
# 
# FIGURE HERE
# 
# A successful run means the program found an answer to the problem you provided – whether it is the correct answer to your problem
# requires the engineer to interpret results and decide if they make sense. The more common
# conceptualization errors are incorrect units and head loss equation for the supplied roughness
# values, missed connections, and forgetting demand somewhere. With practice these kind of
# errors are straightforward to detect. In the present example we select the pipe and the
# solution values are reported at the bottom of a dialog box.
# 
# Figure 9 is the result of turning on the computed head values at the node (and reservoir)
# and the flow value for the pipe. The dialog box reports about 7.2 feet of head loss per 1000
# feet of pipe for a total of 72 feet of head loss in the system. The total head at the demnad
# node is about 28 feet, so the head loss plus remaining head at the node is equal to the 100
# feet of head at the reservoir, the anticipated result.
# The computed friction factor is 0.010, which we could check against the Moody chart if we
# wished to adjust the model to agree with some other known friction factor.
# 
# ## References
# 
# ## Data Files
# 
# ## Videos
# 
