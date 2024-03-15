# docker_assignment

these are the docker commands  for running a simple python application in a container.

Id CommandLine
-- -----------
1 docker build -t bd-a1-image .
2 docker start container
3 docker start bd-a1-container
4 docker cp load.py bd-a1-container:/home/doc-bd-a1/
5 docker cp dpre.py bd-a1-container:/home/doc-bd-a1/
6 docker cp eda.py bd-a1-container:/home/doc-bd-a1/
7 docker cp vis.py bd-a1-container:/home/doc-bd-a1/
8 docker cp model.py bd-a1-container:/home/doc-bd-a1/
9 docker cp final.sh bd-a1-container:/home/doc-bd-a1/
10 docker cp wc.csv bd-a1-container:/home/doc-bd-a1/
11 docker exec -it bd-a1-container bash
12 python3 load.py wc.csv
13 history
14 cd ..
15 git clone https://github.com/AhmedAmin10/docker_assignment.git
16 git add *
17 git commit -m "docker code"
18 git push
19 docker tag bd-a1-image:latest aamiin/bd-a1-image:latest
20 docker push aamiin/bd-a1-image:latest

the assignment focaused on how to use the docker container and to get a dataset and make a multiple proccess
1- load the dataset in load.py
2- make some data preprossesing  using dpre.py
3- do an EDA in eda.py file 
4- make a visualization in vis.py 
5-  create and train a machine learning model in model.py
6- run the shell script to call all functions from above files one by one
7- save the result of your analysis in service-results directory