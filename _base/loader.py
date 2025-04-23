from abc import ABC, abstractmethod

class IConfigLoader(ABC):
    """Abstract base class/interface for all configuration loaders"""
    
    @abstractmethod
    def get(self, key, default= None):
        """Get a configuration value"""
        pass
    
    @abstractmethod
    def get_int(self, key, default = None):
        """Get a configuration value as integer"""
        pass
    
    @abstractmethod
    def get_bool(self, key, default = None):
        """Get a configuration value as boolean"""
        pass
    
    @abstractmethod
    def prefixed_get(self, prefix):
        """Get all configuration values with a specific prefix"""
        pass