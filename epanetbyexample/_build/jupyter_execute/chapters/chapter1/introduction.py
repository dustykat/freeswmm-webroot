#!/usr/bin/env python
# coding: utf-8

# # Introduction
# 
# ## How to Use This Book
# 
# This book is a collection of worked EPANET examples from a variety of sources, some real, many pedagogical.  Most examples will have the set of files needed to replicate the example, you simply have to download the files, and run the EPANET model using the various files to replicate the examples.  Alternatively you can run the models on the FreeSWMM web interface.
# 
# ## FreeSWMM Web 
# 
# The FreeSWMM Web interface is a VPS hosted on AWS that is accessed using a web browser.  The browser will connect to a desktop (XFCE) environment which you can use to open EPANET and the associated files. Please remember to disconnect when you are done, and be aware the system is restarted from time to time so any files you save or damage for that matter are lost.  
# 
# :::{warning}
# **FreeSWMM is optional** Most people will be better served to download and install a current version of EPANET.  The examples can still be followed by downloading the input files in the references for each example, or manual building of the smaller problems.  
# :::
# 
# ## About EPANET
# 
# EPANET is a computer program that performs hydraulics computations in pressure-pipe systems. 
# The version of EPANET in this JupyterBook is 2.2. All the versions so far include a capacity to read an ASCII input file to direct the computations.
# 
# > A GUI Interface is available that runs in Windows that is quite popular and useful, professional software companies add GIS interfaces to access the computation engine. Many users dispense with the interface entirely and operate the model using custom-built (or general) wrapper programs to call various DLLs (or Shared Object Libraries).  Wrappers exist in **R**, Python, Delphi (the Legacy GUI), and probably PERL and Ruby.
# 
# The remainder of this book shows how to use EPANET by a series of representative examples.  These examples are at best a subset of the capabilities of the program, but should be enough to get one started.   The program requires some hydraulic insight to interpret the results as well as detect data entry or conceptualization errors.
# 
# :::{note}
# This JupyterBook is evolved from [Cleveland, T.G., Tay, C.C., and Neale, C.N. 2015. EPANET by Example. Department of Civil and Environmental Engineering, Texas Tech University.](http://freeswmm.ddns.net/freeswmm-webroot/epanetbyexample/chapters/EPANETbyExampleV1.pdf)
# :::

# In[ ]:




