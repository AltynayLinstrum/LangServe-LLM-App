from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

app=FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API server"
)

add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)

model=ChatOpenAI()
prompt1=ChatPromptTemplate.from_template("Write a 250 word essay about {topic}")
prompt2=ChatPromptTemplate.from_template("Write a 50 word poem about {topic}")


add_routes(
    app, 
    prompt1|model,
    path="/essay"
)

add_routes(
    app,
    prompt2|model,
    path="/poem"
)

if __name__=="__main__":
    uvicorn.run(app, host="localhost", port=8000)