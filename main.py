from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse 
from pydantic import BaseModel
from typing import Optional
from ner_client import NamedEntityClient
import spacy

app = FastAPI()
app.mount('/static', StaticFiles(directory='static'))

ner = spacy.load("zh_core_web_sm")
ner = NamedEntityClient(ner)

class Data(BaseModel):
    sentence: Optional[str] = None

@app.get('/')
def main():
    return FileResponse('main.html')

@app.post('/ner')
def get_named_ents(data: Data):
    return ner.get_ents(data.sentence)