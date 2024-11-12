

# command to run on container start

# base image
FROM python:3.12-slim

# setup working directory in container
WORKDIR /inventory_management_system

# copy all files to inventory_management_system directory
COPY . /inventory_management_system/

# Install Poetry
RUN pip install poetry

# Install dependencies via Poetry
RUN poetry install

# Install MyPy for type-checking
RUN poetry add --dev mypy

# command to run on container start
#CMD ["poetry", "run", "python", "inventory_management_system/main.py"]

# Add a command to run MyPy before the main script, if desired
CMD ["poetry", "run", "mypy", "inventory_management_system/main.py", "&&", "poetry", "run", "python", "inventory_management_system/main.py"]