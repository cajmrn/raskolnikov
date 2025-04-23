from abc import ABC, abstractmethod
from typing import Optional, Dict, Any
import os
from dotenv import load_dotenv
import logging

class EnvConfigLoader(IConfigLoader):
    """Environment variables and .env file loader"""
    
    def __init__(self, env_file=None, raise_on_missing=False):
        self._raise_on_missing = raise_on_missing
        self._loaded_values = {}
        
        if env_file:
            if not os.path.exists(env_file):
                raise FileNotFoundError(f"Env file not found: {env_file}")
            load_dotenv(env_file)
    
    def get(self, key, default=None):
        if key in self._loaded_values:
            return self._loaded_values[key]
            
        value = os.getenv(key, default)
        
        if value is None and self._raise_on_missing:
            raise ValueError(f"Required configuration key '{key}' not found")
            
        self._loaded_values[key] = value
        return value
    
    def get_int(self, key, default=None):
        value = self.get(key, default)
        return int(value) if value is not None else None
    
    def get_bool(self, key, default=None):
        value = self.get(key, default)
        if isinstance(value, bool):
            return value
        if value is None:
            return None
        return value.lower() in ('true', '1', 't', 'y', 'yes')
    
    def prefixed_get(self, prefix):
        prefix = prefix.upper()
        return {
            key: value 
            for key, value in os.environ.items() 
            if key.startswith(prefix)
        }