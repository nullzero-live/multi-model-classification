
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
ENV WANDB_API_KEY=1e66f6bcbee6295454fb2a9cb4fbf3638024b969
ENV PORT 8080

#Run streamlit server
#ENTRYPOINT exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
CMD streamlit run main.py --server.port $PORT