FROM python:3.11-slim
WORKDIR /app

# create a non-root user
RUN adduser --disabled-password --gecos "" appuser

# change ownership of /app to appuser
RUN chown -R appuser:appuser /app

# switch to the non-root user
USER appuser

# set up environment variables
ENV PATH="/home/appuser/.local/bin:$PATH"

# install ADK
RUN pip install google-adk==1.2.1

# copy agent
COPY "assistant/" "/app/assistant/"

EXPOSE 8080

ENTRYPOINT ["adk", "web", "--port", "8080", "--host", "0.0.0.0", "/app/"]
