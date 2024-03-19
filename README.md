To successfully run the example application, follow this step-by-step guide, which explains how to use the Python files 'send.py' and 'receive.py', and what they each accomplish.

## Running the Consumer File ('receive.py')
1. Open a Terminal: Navigate to the directory where your receive.py file is saved.
2. Execute the 'receive.py' File: Enter the following command and press Enter:
```
python receive.py
```

After execution, the Consumer will be waiting for incoming messages from the queue named hello. A message will be displayed indicating that the program is waiting for messages: [*] Waiting for messages. To exit press CTRL+C.

## Running the Producer File ('send.py')
The send.py file is used to send messages to the same RabbitMQ queue (hello) that the Consumer is reading from. Each time you run send.py, it sends a message to the queue.
1. Open a New Terminal: Navigate to the directory where your send.py file is saved. It's important to use a new terminal since the first terminal is already being used by the Consumer.
2. Execute the send.py File: Enter the following command and press Enter:
```
python send.py
```
After execution, this file sends the message "Hello World!" to the hello queue. In the Consumer's terminal, you will see an output confirming that the message was received: [x] Received 'Hello World!'.

## What Do These Files Do?
- Consumer (receive.py): Waits for and processes messages from a RabbitMQ queue. This simulates a service or application waiting for data from another part of the system. It demonstrates how to asynchronously respond to events or data without blocking the application.
- Producer (send.py): Sends messages to a RabbitMQ queue. This simulates sending data or events from one part of your system to another. It shows how messages can be effectively exchanged between different parts of an application or between different applications without requiring direct dependencies or tight coupling.

By running these two files, you demonstrate the basics of asynchronous communication between services using RabbitMQ, a powerful tool for message delivery and management.
