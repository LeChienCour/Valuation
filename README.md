# Valuation

Valuation is a software application designed to provide accurate and efficient valuation services. This README provides an overview of its functionality, instructions on how to build it using Docker Compose, and how to use it with Docker Attach.

## Functionality

- Provides accurate valuation services.
- Supports multiple valuation models.
- User-friendly interface for easy interaction.
- Scalable and efficient performance.

## Building with Docker Compose

To build the Valuation application using Docker Compose, follow these steps:

1. Ensure you have Docker and Docker Compose installed on your machine.
2. Clone the repository to your local machine:
    ```sh
    git clone https://github.com/LeChienCour/valuation.git
    cd valuation
    ```
3. Build and start the application using Docker Compose:
    ```sh
    docker-compose up --build
    ```

## Using with Docker Attach

To use the Valuation application with Docker Attach, follow these steps:

1. List the running Docker containers to find the container ID or name:
    ```sh
    docker ps
    ```
2. Attach to the running container:
    ```sh
    docker attach <container_id_or_name>
    ```

You can now interact with the Valuation application directly through the attached container.


