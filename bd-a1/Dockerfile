# Use Ubuntu as the base image
FROM ubuntu

# Install necessary packages
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip3 install pandas numpy seaborn matplotlib scikit-learn scipy

# Create a directory inside the container
RUN mkdir -p /home/doc-bd-a1/

# Move the dataset file to the container
COPY wc.csv /home/doc-bd-a1/

# Set the working directory
WORKDIR /home/doc-bd-a1/

# Mount a volume for output files
VOLUME /home/output

# Copy the final.sh script to the container
COPY final.sh /home/doc-bd-a1/

# Make final.sh executable
RUN chmod +x /home/doc-bd-a1/final.sh

