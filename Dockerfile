FROM python:3.10-slim-buster
WORKDIR  /app
RUN pip3 install dagster dagstermill dagit
COPY . .
ENV DAGSTER_HOME=/app/daghome
RUN mkdir -p $DAGSTER_HOME
# dagit -h 0.0.0.0 -f /app/dag.py
CMD ["dagit", "-h", "0.0.0.0", "-f", "/app/dag.py"]