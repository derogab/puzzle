FROM python:3-alpine
# Create app directory
WORKDIR /usr/src/app
# Copy app 
COPY . .
# Install app dependencies
RUN pip install -r requirements.txt && \
    pip install .
# Run the app
CMD python -u main.py