# Project Name: Toxicity-detection-serice

## Project Description
The Toxicity Detection Service is a machine learning-powered application that analyzes text messages for toxicity. It utilizes FastAPI for web service, Celery for asynchronous task processing, RabbitMQ for message queuing, and Redis for caching. This service efficiently predicts the toxicity of text messages, making it valuable for content moderation and similar use cases. Additionally, it's designed to leverage GPU resources for faster processing when available.

## Project Structure

```
.
├── docker-compose.yml
├── Dockerfile
├── README.md
├── requirements.txt
└── src
    ├── main.py
    └── task.py
                                                          Worker
                                                        ┌──────────┐
          API server                queue               │          │
         ┌───────────┐        ┌──────────────────┐   ┌──┴──────┐   │
   GET   │           │        │                  │   │         │   │
─────────►  FastAPI  ├────────►     RabbitMQ     ├───►  Celery ├───┘
         │           │        │                  │   │         │
         └─┬───────▲─┘        └──────────────────┘   └─────────┘
           │       │
           │       │
           │       │
         Hash    Cache
           │       │
           │       │
           │       │
         ┌─▼───────┴─┐
         │           │
         │   Redis   │
         │           │
         └───────────┘
```
## Installation

To run this project, you will need [Docker](https://www.docker.com/) installed on your system.

1. Unzip project:
   ```bash
   unzip file.zip
   cd toxicity-detection-service
2. Build and start the project with Docker Compose:
    ```bash 
    docker-compose up --build
3. The FastAPI web server will be available at http://localhost:8000.

## Usage

Toxicity prediction can be accessed by making a GET request to the /predict/{message} endpoint, where {message} is the text you want to analyze for toxicity. The prediction is calculated using a SHA-256 hash of the message, and results are cached in Redis for future use.


Example usage:

curl http://localhost:8000/predict/This%20is%20a%20test%20message

## Configuration

No additional configuration is required for the project. GPU resources are utilized automatically if available.

## Credits

- [FastAPI](https://fastapi.tiangolo.com/)
- [Celery](https://docs.celeryproject.org/en/stable/)
- [RabbitMQ](https://www.rabbitmq.com/)
- [Redis](https://redis.io/)
- [Detoxify](https://github.com/unitaryai/detoxify)



# Question 
 ## 1. Describe your solution. What tradeoffs did you make while designing it, and why?

The Toxicity Detection Service is a tool that analyzes text messages for harmful content. It operates using the following components:

- **FastAPI for Web Service:** Utilizes FastAPI for creating a fast and efficient web service for text toxicity prediction.

- **Celery for Background Tasks:** Employs Celery for processing text toxicity predictions in the background, ensuring a smooth user experience.

- **RabbitMQ for Communication:** Utilizes RabbitMQ to enable communication between the web service and Celery for reliable task distribution.

- **Redis for Caching:** Employs Redis to store previously predicted results, reducing response times for similar queries.

**Tradeoffs:**

- **Speed vs. Resources:** Leveraging GPU resources for prediction enhances speed at the potential cost of increased system resource consumption.

- **Caching vs. Storage:** Caching accelerates responses but may require additional storage space.

- **Simplicity vs. Complexity:** Focuses solely on toxicity detection, avoiding the inclusion of complex features like sentiment analysis.

- **Dependency Choices:** The chosen technologies prioritize performance and scalability, though they may entail some setup and management.

## 2. If this were a real project, how would you improve it further? 
- **Logging and Monitoring:** Implement robust logging and monitoring to track service health, detect issues, and troubleshoot problems effectively. Consider using tools like Prometheus and Grafana for monitoring.

- **Testing:** Develop a comprehensive suite of unit tests, integration tests, and end-to-end tests to ensure the service's reliability and correctness.

- **Scaling:** Implement automatic scaling to handle varying levels of traffic. Use container orchestration tools like Kubernetes to manage scaling efficiently.

- **Error Handling:** Improve error handling and provide meaningful error messages to users. Implement retries and fallback mechanisms for enhanced fault tolerance.
- **Docker Image Optimization:** Optimize the Docker image size to reduce resource consumption and speed up deployment.

- **Configuration Management:** Implement a robust configuration management system to manage environment-specific configurations and secrets securely.
- **Backup and Recovery:** Set up regular data backups and establish disaster recovery procedures to minimize data loss in case of failures.

- **Compliance:** Ensure compliance with relevant data protection regulations and industry standards, such as GDPR or HIPAA, if applicable.

- **Feedback Mechanism:** Implement a feedback mechanism to collect user feedback and continuously improve the service based on user needs.

- **Community and Support:** Create a community around the project, providing support forums, documentation, and tutorials to help users and contributors.

- **Cost Optimization:** Regularly analyze and optimize resource usage to control operational costs, especially when using cloud services.

- **Performance Tuning:** Continuously monitor and optimize the service's performance, identifying and resolving bottlenecks.

## 3.  Imagine users were allowed to upload pictures to the chat and one more case for your system now is to identify nudity, how would you approach the problem? 
Make a separate endpoint to handle images and build a similar infrastructure to what we already have for text messages, separate queue and workers. Most likely need to reconsider the caching strategy, since it would be handling much more data. It would make sense to add a persistent database to store these images instead of Redis.
## 4.  What should you take into account after previous point?
Since a completely new and separate service is built to handle images, we don't need to change the original one. The only thing is to change the routing on the API gateway if it exists to direct requests with text messages to the original service and ones with images to the new one.
## 5.  What metrics would you consider to make sure your system works well?
- **Accuracy Metrics:**
    - Accuracy
    - Precision
    - Recall
    - F1 Score:

- **Efficiency Metrics:**
    - Latency
    - Throughput
    - Resource Utilization

- **User Experience Metrics:**
    -User Feedback

    

- **Operational Metrics:**
    - System Uptime
    - Resource Costs
    - Error Rates