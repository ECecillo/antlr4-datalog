# Datalog Project: Running the Environment with Docker

This document provides instructions for setting up and running the Datalog project environment using Docker.

# Installation

## Prerequisites

To run this project, you need to have Docker and Docker Compose installed on your machine. If you haven't already, you can follow the official installation guides for Docker [here](https://docs.docker.com/engine/install/) and Docker Compose [here](https://docs.docker.com/compose/install/).

## Setting up the Project with Docker.

(Most of the docker command below can be run using `npm`, I invite you to read the section "Why package.json" if you are already familiar)

1. Clone the project repository or unzip the project folder on your local machine.

2. Open a terminal and navigate to the root folder of the project.

3. Build the Docker container by running the following command:

```bash
docker-compose build
```

This command reads the `Dockerfile` and `requirements.txt` files in the project folder and builds a Docker container with the necessary libraries and configurations.

4. Once the build is complete, start the container using the following command:

```bash
docker-compose up
```

This command starts the container and runs the Python script specified in the `CMD` line of the `Dockerfile`. The output will be displayed in the terminal.

## Additional Instructions

### Modifying or Adding Files to the Project

The `docker-compose.yml` file maps the current directory on your host machine to the `/app` directory inside the container:

```yaml
volumes:
  - .:/app
```

This means that any changes you make to the files within the mapped directory on your host machine will be automatically reflected inside the container.

To modify or add files to the project:

1. Edit or create files directly in the project folder on your host machine.

2. To see the changes take effect, restart the container by running the following commands:

```bash
docker-compose down
docker-compose up
```

### Updating the Docker Configuration

If you need to modify the `Dockerfile` or `requirements.txt` file, such as changing the base image or adding/removing dependencies, you must rebuild the container to apply the updates:

1. Make the necessary changes to the `Dockerfile` or `requirements.txt` file.

2. Rebuild the container using the following command:

```bash
docker-compose build
```

3. Start the updated container with:

```bash
docker-compose up
```

### Stopping the Container

To stop the running container, press `Ctrl+C` in the terminal where the container is running, or use the following command in a separate terminal:

```bash
docker-compose down
```

This command stops and removes the container, allowing you to rebuild and restart it if needed.

## Why package.json?

This document explains the purpose of the `package.json` file included in the Datalog project and its role in simplifying the process of running custom commands and managing project dependencies.

The `package.json` file is a standard component in Node.js projects, serving as a manifest that provides metadata and configuration information about the project. In the context of the Datalog project, the file is used to define custom scripts and manage project dependencies, making it easier to execute various tasks and ensure a consistent development environment.

Although the project primarily uses Python and Docker, the inclusion of the `package.json` file offers a convenient way to organize and run custom commands, regardless of the programming language or technology stack used in the project.

## Custom Commands

The `scripts` section of the `package.json` file defines a set of custom commands that can be executed using the `npm run` command. These custom commands simplify the process of running frequent tasks or complex commands by providing a shorthand alias.

For example, in the Datalog project, you might have the following custom commands defined in the `scripts` section:

```json
"scripts": {
  "build": "docker-compose build",
  "start": "docker-compose up",
  "stop": "docker-compose down"
}
```

To execute any of these custom commands, simply run `npm run <command-name>` in the terminal. For instance, to build the Docker container, you would run:

```bash
npm run build
```

# Running the project

