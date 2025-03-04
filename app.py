from fastapi import FastAPI, HTTPException, Query, Response
from fastapi.middleware.cors import CORSMiddleware
import os
import requests
import subprocess
import json
from dotenv import load_dotenv
from datetime import datetime
from dateutil import parser
from typing import Dict, Any
import base64
import numpy as np
import pandas as pd
import sqlite3, duckdb, httpx

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# from sentence_transformers import SentenceTransformer
# from sklearn.metrics.pairwise import cosine_similarity

load_dotenv() 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

AIPROXY_TOKEN = os.getenv("AIPROXY_TOKEN")


