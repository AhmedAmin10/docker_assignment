#!/bin/bash

# Print information about the source files
echo "Source files:"
ls -l /home/doc-bd-a1/

# Print information about the destination directory
echo "Destination directory:"
ls -l "/mnt/host/C/Users/Ahmed/Desktop/BIg Data/Assignment/bd-a1/service-result/"

# Copy the output files to the local machine
#!/bin/bash

# Copy the output files to the local machine
docker cp  /home/doc-bd-a1/res_dpre.csv "/mnt/host/C/Users/Ahmed/Desktop/BIg Data/Assignment/bd-a1/service-result/"
docker cp  /home/doc-bd-a1/eda-in-1.txt "/mnt/host/C/Users/Ahmed/Desktop/BIg Data/Assignment/bd-a1/service-result/"
docker cp  /home/doc-bd-a1/eda-in-2.txt "/mnt/host/C/Users/Ahmed/Desktop/BIg Data/Assignment/bd-a1/service-result/"
docker cp  /home/doc-bd-a1/eda-in-3.txt "/mnt/host/C/Users/Ahmed/Desktop/BIg Data/Assignment/bd-a1/service-result/"
docker cp  /home/doc-bd-a1/vis.png "/mnt/host/C/Users/Ahmed/Desktop/BIg Data/Assignment/bd-a1/service-result/"
docker cp  /home/doc-bd-a1/k.txt "/mnt/host/C/Users/Ahmed/Desktop/BIg Data/Assignment/bd-a1/service-result/"

# Print "finished"
echo "finished"

# Print "finished"
echo "finished"
