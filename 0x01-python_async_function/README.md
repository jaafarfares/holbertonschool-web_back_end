# 0x01. Python - Async

## Description
This is a Python script that demonstrates the use of async functionality in Python, specifically in the context of concurrency, measuring execution time, and ordering the result.

## Tasks
0. The basics of async
This task involves writing an asynchronous coroutine called wait_random that takes in an optional integer argument max_delay (with a default value of 10) and waits for a random delay between 0 and max_delay seconds before returning the delay value.

##### 1. Let's execute multiple coroutines at the same time with async
This task involves importing the wait_random function from the previous task and using it to write an async routine called wait_n. wait_n takes in two integer arguments, n and max_delay, and spawns wait_random n times with the specified max_delay. It should return a list of all the delays (float values) in ascending order.

#### 2. Measure the runtime
This task involves importing the wait_n function from the previous task and using it to create a function called measure_time that takes in two integer arguments, n and max_delay. The function measures the total execution time for wait_n(n, max_delay) and returns the average time per execution by dividing the total time by n. The function should return a float.

#### 3. Concurrently wait for n coroutines
This task involves writing an async function called wait_n that takes in two arguments: n and max_delay. The function should spawn n coroutines that call wait_random(max_delay) concurrently, and return a list of the n results, in the order that they are ready.


#### 5. return the list of all the delays
Take the code from wait_n and alter it into a new function task_wait_n. The code is nearly identical to wait_n except task_wait_random is being called.
