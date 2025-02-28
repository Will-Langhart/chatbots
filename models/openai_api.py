# models/openai_api.py

def get_response(message):
    """
    Generate a chatbot response that helps the user choose the perfect RAG architecture.
    
    This implementation analyzes the user input to determine key requirements—such as:
      - Enterprise scalability and performance
      - Simplicity and ease-of-use
      - Advanced search and analytics
      - Property management specifics
      - Maintenance and lease management
      - Multilingual/global deployments
      - Custom or niche solutions
      - Cost-effectiveness
      - Innovation and experimental features
      - Security and privacy needs
      - Microservices/distributed architecture
      - Asynchronous processing
    
    Based on the detected keywords, the function returns a detailed recommendation.
    
    Parameters:
        message (str): The user's input message.
    
    Returns:
        str: A detailed recommendation message for choosing the right architecture.
    """
    # Normalize the message for case-insensitive matching
    message = message.lower()

    # Enterprise, scalability, performance
    if any(keyword in message for keyword in ["enterprise", "scalable", "high load", "robust", "performance"]):
        return (
            "Based on your need for enterprise-level scalability and robust data retrieval, "
            "I recommend Architecture 4 or Architecture 17. These designs offer multi-LLM fallback, "
            "SQL-based data retrieval, and containerized deployments with Docker/Kubernetes for long-term growth."
        )
    
    # Simplicity, basic setup
    elif any(keyword in message for keyword in ["simple", "basic", "starter", "beginner", "easy"]):
        return (
            "If you're looking for a straightforward solution, Architecture 1 is an excellent choice. "
            "It uses OpenAI for completions and Pinecone for embeddings, making it quick to set up and ideal for smaller projects or prototypes."
        )
    
    # Advanced search, analytics, and retrieval
    elif any(keyword in message for keyword in ["search", "analytics", "retrieval", "data"]):
        return (
            "For sophisticated search and analytics capabilities, consider Architecture 6. "
            "This solution integrates ElasticSearch, LangChain, and Pinecone to deliver precise, context-aware data retrieval."
        )
    
    # Property management and real estate applications
    elif any(keyword in message for keyword in ["property", "real estate", "rental", "tenant"]):
        return (
            "For property management applications, Architecture 21 is tailored to provide real-time property insights and AI analytics, "
            "helping you make informed decisions in the real estate domain."
        )
    
    # Lease management, maintenance, scheduling, document processing
    elif any(keyword in message for keyword in ["maintenance", "lease", "scheduling", "renewal", "document"]):
        return (
            "If your focus is on lease management or maintenance scheduling, Architectures 22 and 23 offer specialized modules "
            "for document parsing, data extraction, and scheduling automation to streamline your workflows."
        )
    
    # Multilingual and global deployment
    elif any(keyword in message for keyword in ["multilingual", "translation", "global"]):
        return (
            "For global deployments requiring multilingual support, Architecture 15 integrates DeepL for translation along with OpenAI and Pinecone, "
            "ensuring effective communication in multiple languages."
        )
    
    # Custom or niche solutions
    elif any(keyword in message for keyword in ["custom", "unique", "niche", "specialized"]):
        return (
            "For niche or specialized applications, Architecture 13 is designed to incorporate a custom ML model alongside OpenAI and Pinecone, "
            "delivering tailored, domain-specific responses."
        )
    
    # Cost and budget considerations
    elif any(keyword in message for keyword in ["cost", "budget", "price"]):
        return (
            "If cost-effectiveness is a priority, you might consider a simpler architecture such as Architecture 1, or a hybrid approach like Architecture 12, "
            "which leverages caching to reduce operational costs while maintaining performance."
        )
    
    # Innovation, experimental, or future-proof solutions
    elif any(keyword in message for keyword in ["innovation", "experimental", "future"]):
        return (
            "For cutting-edge, experimental solutions, Architecture 11 or Architecture 16 offer advanced integration of multiple AI models and custom retrieval logic, "
            "pushing the boundaries of traditional RAG implementations."
        )
    
    # Security, privacy, compliance
    elif any(keyword in message for keyword in ["security", "privacy", "compliance"]):
        return (
            "If security and privacy are critical, Architecture 9 is ideal. It incorporates robust OAuth authentication and RBAC for secure, enterprise-grade operations."
        )
    
    # Microservices or distributed architecture
    elif any(keyword in message for keyword in ["microservices", "distributed", "modular"]):
        return (
            "For scalable and decoupled deployments, Architecture 7 offers a microservices-based design that distributes functionality across dedicated services, "
            "facilitating independent scaling and easier maintenance."
        )
    
    # Asynchronous processing and background tasks
    elif any(keyword in message for keyword in ["asynchronous", "background", "celery"]):
        return (
            "For handling long-running tasks asynchronously, Architecture 10 utilizes Celery to manage background processes efficiently, ensuring high performance under load."
        )
    
    # Federated or aggregated solutions
    elif any(keyword in message for keyword in ["federated", "aggregated", "unified"]):
        return (
            "For a comprehensive solution that consolidates multiple AI outputs, the Federated Search architecture provides a unified interface to leverage various models simultaneously."
        )
    
    # If no condition matches, ask for more details.
    else:
        return (
            "Could you please provide more details about your requirements? For example, are you focused on scalability, "
            "simplicity, advanced search, multilingual support, or a specialized domain? More context will help me recommend the best RAG architecture for your needs."
        )
