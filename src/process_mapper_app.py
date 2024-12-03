import streamlit as st
import graphviz
from typing import Dict, List
import json
from datetime import datetime
import os
from PIL import Image
import io
import requests
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def check_environment():
    """Check if required environment variables are set"""
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    
    if api_key:
        logger.debug(f"API Key found - Length: {len(api_key)}, First 4 chars: {api_key[:4]}...")
    else:
        logger.error("No API key found in environment!")
        logger.error("Environment variables present: %s", list(os.environ.keys()))
    
    if api_key and api_key.startswith("sk-"):
        logger.warning("API key starts with 'sk-' which is OpenAI format. Anthropic keys should start with 'sk-ant-'")
    
    if not api_key:
        st.error("ANTHROPIC_API_KEY environment variable is not set!")
        st.markdown("""
        ### Setup Instructions:
        1. Get your API key from [Anthropic Console](https://console.anthropic.com/)
        2. Set the environment variable using Windows System Settings:
           ```
           1. Search for 'Environment Variables' in Windows
           2. Click 'Edit the system environment variables'
           3. Click 'Environment Variables'
           4. Under 'User variables', click 'New'
           5. Variable name: ANTHROPIC_API_KEY
           6. Variable value: your-api-key
           7. Click 'OK' and restart your computer
           ```
        """)
        return False
    return True

[... rest of the file content ...]