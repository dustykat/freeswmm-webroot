#!/usr/bin/env python
# coding: utf-8

# # Accessing FreeSWMM
# 
# To access the FreeSWMM site use the link: [FreeSWMM (via NoVNC)](http://freeswmm.ddns.net:6082/vnc.html?host=freeswmm.ddns.net&port=6082) you will encounter the NoVNC interface pictured below:
# 
# ![](novnc.png)
# 
# When you when you click on "Connect" you will encounter a simple password challenge as pictured below:
# 
# ![](challenge.png)
# 
# Enter the password **freeswmm** and select "SEND CREDENTIALS" 
# 
# :::{note}
# In most cases you should observe a security warning that obscures the password dialog, simply click on some part of the dialog to background the warning
# :::
# 
# Upon sucessful connection you will be attached to an XFCE desktop on the remote server as pictured below:
# 
# ![](xfcedesktop.png)
# 
# To start EPANET navigate to the WINE application and select EPANET 2.2 to launch the interface, as pictured below:
# 
# ![](epanet22.png)
# 
# When EPANET starts you should be presented with a clean interface as pictured below:
# 
# ![](epanet2go.png)
# 
# :::{note}
# EPANET is running in a WINE application layer on a linux server, it is similar to windows in terms of file management, resizing and moving the window showing EPANET is accomplished by right-click in the application tab in the upper part of the web interface; otherwise it is ordinary EPANET as one would experience on a Windows computer
# :::

# ## Running Existing Examples
# 
# The existing examples are all stored in the EPANET-Files Directory on the XFCE desktop (as well as some pre-installed examples).  As new examples are added they will be located in that directory.  
# 
# :::{note}
# Moving files onto the remote server is non-trivial.  Although the clipboard tool in the NoVNC interface is useable for ASCII files by opening the file, select all then paste into the clipboard - it works both ways so data can be moved either direction.  The `.net` binary files are not moveable by this method (although this conjecture is untested)
# :::
# 
# ## Exiting FreeSWMM
# 
# When you are done using the application, save your work then exit EPANET in the usual fashion. 
# 
# ![](endepanet.png)
# 
# Then select disconnect to close the web interface as pictured below:
# 
# ![](disconnect.png)
# 
# :::{warning}
# Failure to exit EPANET before disconnecting will stall the server.  It won't actually hurt anything, but it is not end user fixable. A semi-automated resolution method is under investigation.
# :::

# In[ ]:




