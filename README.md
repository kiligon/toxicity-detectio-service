
# Architecture 
```
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
         │  FastAPI  │
         │           │
         └───────────┘
```

# Question 
- Describe your solution. What tradeoffs did you make while designing it, and why? 
- If this were a real project, how would you improve it further? 
- Imagine users were allowed to upload pictures to the chat and one more case for your system now is to identify nudity, how would you approach the problem? 
- What should you take into account after previous point?
- What metrics would you consider to make sure your system works well?
