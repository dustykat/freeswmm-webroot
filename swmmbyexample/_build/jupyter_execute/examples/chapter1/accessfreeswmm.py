#!/usr/bin/env python
# coding: utf-8

# # Accessing FreeSWMM
# 
# To access the FreeSWMM site use the link: [FreeSWMM (via NoVNC)](http://freeswmm.ddns.net:6082/vnc.html?host=freeswmm.ddns.net&port=6082) you will encounter the NoVNC interface pictured below:
# 
# :::{note}
# Additional links for maintenance and troubleshooting:
# > [Root (should return a grey screen of failure)](http://18.210.253.169:6081/vnc.html?host=18.210.253.169&port=6081)<br>
# > [User (same as below - might load a bit faster)](http://18.210.253.169:6082/vnc.html?host=18.210.253.169&port=6082)<br>
# > VNC Services (Run as root or sudo)<br>
# > sudo snap set novnc services.n6081.listen=6081 services.n6081.vnc=localhost:5901<br>
# > sudo snap set novnc services.n6082.listen=6082 services.n6082.vnc=localhost:5902<br>
# :::
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
# To start SWMM navigate to the WINE application and select SWMM 5.1.015 to launch the interface, as pictured below:
# 
# ![](swmm51015.png)
# 
# When SWMM starts you should be presented with a clean interface as pictured below:
# 
# ![](swmm2go.png)
# 
# :::{note}
# SWMM is running in the WINE application layer on a linux server, it is similar to windows in terms of file management, resizing and moving the window showing SWMM is accomplished by right-click in the application tab in the upper part of the web interface; otherwise it is ordinary SWMM as one would experience on a Windows computer
# :::

# ## Running Existing Examples
# 
# The existing examples are all stored in the SWMM-Files Directory on the XFCE desktop (as well as some pre-installed examples).  As new examples are added they will be located in that directory.  
# 
# :::{note}
# Moving files onto the remote server is non-trivial.  Although the clipboard tool in the NoVNC interface is useable for `.inp` files by opening the file, select all then paste into the clipboard - it works both ways so data can be moved either direction.   
# :::
# 
# ## Exiting FreeSWMM
# 
# When you are done using the application, save your work then exist SWMM in the usual fashion. 
# 
# ![](endswmm.png)
# 
# Then select disconnect to close the web interface as pictured below:
# 
# ![](disconnect.png)
# 
# :::{warning}
# Failure to exit SWMM before disconnecting will frequently stall the server.  It wont hurt anything, but is not end user fixable.
# :::
# 
# :::{note}
# The server is programmed to disconnect every hour and restart one minute later; if you are in the middle of something your work should be preserved, just wait the minute and reconnect.  This annoying behavior is to mitigate loss of CPU allocation on AWS because of an idle XFCE window being left open.   Please remember to disconnect your sessions, there are only about 2.4 hours/day of computation time available and the connection itself uses a fair portion of that allocation.
# :::

# In[ ]:




