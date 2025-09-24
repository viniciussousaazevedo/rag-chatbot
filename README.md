# RAG ChatBot
This is a simple GPT-oss ChatBot that can answer questions based on documents and instructions previously declared for the model to operate on.

## Tech Stack:
- Python
- Flask
- LangChain
- Milvus
- Groq
- Gradio

## Local Setup (Unix)

1. Copy and fill the environment variables template:
```bash
cp .env.sample .env
```

2. Start a MongoDB container:
```bash
docker run -d --name mongodb -p 27017:27017 --env-file .env -v mongo_data:/data/db --restart always mongo:8.0.13
```
3. Install Python dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

```bash
python src/app/app.py
```

## Docker Setup

### Local Compose

```bash
docker compose -f ./docker/docker-compose.yaml --env-file ./.env up -d
```

## Architecture Decisions and Patterns

* The application was implemented as a monolith following the MVC pattern and strong SOLID principles.
* Objects considered as main entities in the application logic inherit from the `Entity` model, and may have their own repositories that handle database operations in an abstract and polymorphic way.
* A custom logger was implemented for the most important functions. You can enable detailed log tracing by setting the environment variable `ENABLE_LOGS=true`.
* Incremental testing was applied as new features were developed. Overall, the project achieved an average test coverage of \~90% across the whole application.
