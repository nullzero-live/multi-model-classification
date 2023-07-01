
# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.11-slim

# Allow statements and log messages to immediately appear in the logs


# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install production dependencies.


RUN pip install --no-cache-dir -r ./app/requirements.txt

ENV PORT 8080
EXPOSE 8080



#Run streamlit server
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
CMD streamlit run ./app/main.py --server.port $PORT