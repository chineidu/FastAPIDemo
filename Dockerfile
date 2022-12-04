# Base Image
FROM python:3.10.8-bullseye

# Create work directory
WORKDIR /opt

# Copy the dependencies
COPY ./requirements.txt .
COPY ./test_requirements.txt .
COPY ./tox.ini .

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r ./test_requirements.txt \
    && pip list

# Copy the source code
COPY . .

# Run the app
CMD ["python", "./src/my_app/main.py"]

