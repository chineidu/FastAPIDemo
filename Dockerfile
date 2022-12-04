# Entry point using a bash script
# Base Image
FROM python:3.10.8-bullseye

# Create work directory
WORKDIR /opt

# Create the user that will run the app
RUN adduser --disabled-password --gecos '' user1

# Copy the dependencies
COPY ./requirements.txt .
COPY ./test_requirements.txt .
COPY ./tests .
COPY ./run.sh .

# Install dependencies
RUN python3 -m pip install --upgrade pip \
    pip install --no-cache-dir --upgrade -r ./test_requirements.txt \
    && pip list

# Copy the source code
COPY ./src .

# Turn the script to an executable file
RUN chmod +x ./run.sh
# Change the ownership of the file
RUN chown -R user1:user1 ./

USER user1

EXPOSE 8000

# Run the app using a bash script
CMD ["bash", "./run.sh"]

