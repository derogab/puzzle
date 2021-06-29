FROM python:3-alpine
# Create app directory
WORKDIR /usr/src/app
# Copy app 
COPY . .
# Install app dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install .
# Run the app
CMD pip install --upgrade pip && \
    if test -f /usr/src/app/plugins/requirements.txt; then \
        pip install -r /usr/src/app/plugins/requirements.txt >> /dev/null; \
    fi && \
    python -u main.py