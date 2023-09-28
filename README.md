# Taskify

![image](https://github.com/aj7tt/Legistify/assets/67835881/466fe13e-d3a8-409c-a0b0-1775c68a151d)


# Taskify API Documentation

Taskify is an application that allows users to manage tasks efficiently. This API documentation provides details on the available endpoints and how to interact with them. Taskify is built using FastAPI, JWT (JSON Web Tokens), SQLAlchemy, and Pydantic to ensure secure and efficient task management.

Taskify API follows RESTful API design principles effectively by:

- Organizing around resources. User , Task...
- Using appropriate HTTP methods.
- Naming endpoints descriptively. task/{task_id}
- Implementing authentication. using JWT
- Structuring documentation logically.
- Properly handling errors. using HTTPException & pydantic
- Summarizing the API's purpose.

## Table of Contents
1. [Introduction](#introduction)
2. [Authentication](#authentication)
    - [POST /register](#post-register)
    - [POST /login](#post-login)
    - [GET /token](#get-token)
3. [Health Check](#health-check)
    - [GET /health](#get-health)
4. [Task Management](#task-management)
    - [POST /tasks](#post-tasks)
    - [GET /tasks](#get-tasks)
    - [GET /tasks/{task_id}](#get-task)
    - [PUT /tasks/{task_id}](#put-task)
    - [DELETE /tasks/{task_id}](#delete-task)
    - [PATCH /tasks/{task_id}/status](#patch-task-status)

## Introduction

Taskify is a task management application that provides a set of RESTful API endpoints for creating, updating, and managing tasks. To use these endpoints, users need to register, login, and obtain an authentication token, which should be included in the request headers for authentication.

## Authentication

### POST /register

- **HTTP Method:** POST
- **Endpoint:** `/register`
- **Description:** Allows users to register for the Taskify app. Users must provide a username, password.

### POST /login

- **HTTP Method:** POST
- **Endpoint:** `/login`
- **Description:** Allows users to log in and obtain an authentication token, which is required to access task-related endpoints.

### GET /token

- **HTTP Method:** GET
- **Endpoint:** `/token`
- **Description:** Verifies a user's token, decodes it, and provides user ID, name, and token expiration time.

## Health Check

### GET /health

- **HTTP Method:** GET
- **Endpoint:** `/health`
- **Description:** Checks the health status of the application. A successful response indicates that the application is running smoothly.

## Task Management

### POST /tasks

- **HTTP Method:** POST
- **Endpoint:** `/tasks`
- **Description:** Enables users to create a new task by providing task details such as Task Name, Description, Due Date, and Status.

### GET /tasks

- **HTTP Method:** GET
- **Endpoint:** `/tasks`
- **Description:** Retrieves a list of all tasks created by the authenticated user.

### GET /tasks/{task_id}

- **HTTP Method:** GET
- **Endpoint:** `/tasks/{task_id}`
- **Description:** Retrieves a specific task by its unique ID. Users can access only their own tasks.

### PUT /tasks/{task_id}

- **HTTP Method:** PUT
- **Endpoint:** `/tasks/{task_id}`
- **Description:** Allows users to update a specific task by providing the task ID and updated task details.

### DELETE /tasks/{task_id}

- **HTTP Method:** DELETE
- **Endpoint:** `/tasks/{task_id}`
- **Description:** Enables users to delete a specific task by its ID.

### PATCH /tasks/{task_id}/status

- **HTTP Method:** PATCH
- **Endpoint:** `/tasks/{task_id}/status`
- **Description:** Allows users to update the status of a specific task. This endpoint is useful for marking tasks as completed or in progress.

## Conclusion

Taskify is a task management application that provides a straightforward API for managing tasks. Users can register, log in, and utilize various endpoints to create, retrieve, update, and delete tasks efficiently. The API ensures security through token-based authentication and follows RESTful API design principles for a user-friendly experience.


