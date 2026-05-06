FROM jupyter/datascience-notebook:python-3.9

# System dependencies
USER root
RUN apt-get update && apt-get install -y \
    wget git build-essential

# Create directories (will download data later if needed)
RUN mkdir -p /usr/share/skyfield-data && \
    mkdir -p /home/jovyan/work/envisat

# Python packages
RUN pip install skyfield llama-cpp-python scipy boto3 matplotlib ipywidgets

# Fix permissions
RUN chown -R $NB_UID:$NB_GID /home/jovyan/work

# Jupyter config
RUN mkdir -p /home/jovyan/.jupyter && \
    echo "c.NotebookApp.token = ''" > /home/jovyan/.jupyter/jupyter_notebook_config.py

WORKDIR /home/jovyan/work
