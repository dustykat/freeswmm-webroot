#!/usr/bin/env python
# coding: utf-8

# # Simple Pipelines
# 
# The examples in this section are simple pipelines. EPANET is overkill for these examples, but they are a place to start.
# 
# In these examples a modeling protocol is repeated to serve as a simple way to organize work within the program.  The protocol is roughly:
# 
# 1. Start EPANET
# 2. Set defaults
# 3. Import the background image (optional).
# 4. Add Node-Type elements to the map
# 5. Add Link-Type elements to the map
# 6. Use hydraulic object dialogs to parameterize the model
#   - Set the total head each reservoir.
#   - Set the pipe length, roughness height, and diameter in each pipe.
#   - Set pumps, valves, and other elements
# 7. Save the input file.
# 8. Run the program. 
# 9. Check and interpret the results.
# 
# :::{note}
# The protocol follows the guidance in the user manual 
# :::

# In[ ]:




