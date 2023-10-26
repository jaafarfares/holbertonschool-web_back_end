# 0x14-queuing_system_in_js


Building a Redis-Powered Queue System with Express

In this project, we have developed a Redis-powered queue system using Node.js and Express. The project covers various aspects of working with Redis, including basic operations, handling async operations, storing hash values, and integrating a queue system using Kue.

How to Run a Redis Server on Your Machine
Installation:

Install Redis on your machine. You can find the installation instructions on the official Redis website.
Running Redis:

Start the Redis server using the appropriate command based on your operating system.
How to Run Simple Operations with the Redis Client
We used the redis package in Node.js to create a Redis client and demonstrated simple operations like setting and getting values.
How to Use a Redis Client with Node.js for Basic Operations
We showcased the basic usage of the Redis client in a Node.js environment, covering operations such as setting and getting values.
How to Store Hash Values in Redis
Utilizing Redis hash data type, we stored and retrieved values in a structured format.
How to Deal with Async Operations with Redis
We used the promisify utility to handle asynchronous operations with Redis, making use of async/await for cleaner code.
How to Use Kue as a Queue System
We introduced Kue, a powerful priority job queue for Node.js applications, to manage and process background jobs asynchronously.
How to Build a Basic Express App Interacting with a Redis Server
We built a basic Express application that interacts with a Redis server, exposing endpoints to get the number of available seats and reserve seats.
How to Build a Basic Express App Interacting with a Redis Server and Queue
We extended the Express app to include a queue system using Kue. The application allows clients to reserve seats, and a separate process handles the queue, updating seat availability accordingly.
This project provides a comprehensive overview of integrating Redis with Node.js and Express, showcasing both basic Redis functionality and the implementation of a powerful queue system for handling asynchronous tasks.




### Made by [Jaafar Fares](https://jaafarfares.github.io/) for [Holberton School](https://www.holbertonschool.com/)
