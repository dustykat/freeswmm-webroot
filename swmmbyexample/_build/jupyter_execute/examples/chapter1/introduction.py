#!/usr/bin/env python
# coding: utf-8

# # Introduction
# 
# ## How to Use This Book
# 
# This book is a collection of worked SWMM examples from a variety of sources, some real, most are pedagogical.  Most examples will have a set of files needed to replicate the example, you simply have to download the files, and run the SWMM model using the various files to replicate the examples.  Alternatively you can run the models on the FreeSWMM web interface.
# 
# ## FreeSWMM Web 
# 
# The FreeSWMM Web interface is simply a VPS hosted on AWS that is accessed using a web browser.  The browser will connect to a desktop (XFCE) environment which you can use to open SWMM and the associated files. Please remember to disconnect when you are done, and be aware the system is restarted from time to time so any files you save or damage for that matter are lost.
# 
# :::{note} Developer's Note.  The website is programmed to disconnect every hour on the hour via a root-level cron job.  The 
# crontable is
# 
# ```
# # m h  dom mon dow   command
# # kill current VNC desktop and connection
#   0 *  *   *   *     /home/antares/stopVNC.sh
# # start new VNC desktop and connection
#   1 *  *   *   *     /home/antares/startVNC.sh
# ```
# 
# This "hack" prevents the AWS server from wasting CPU cycles on an open, but idle connection.  The author has not tested with a lot of multiple concurrent connections, as the sample website exists as an illustration.  A formal short-course woul be best served by creating multiple AWS instances (one per participant) which can be done quickly. AWS has provisions to transfer instances to a new owner, so after the short course participants can take ownership of an instance or let the instructor kill it - all at a very manageable cost.  When developing short course budget suggest estimate cost of an instance as 2X the current AWS price for a 2GB Linux instance.
# :::

# In[ ]:




