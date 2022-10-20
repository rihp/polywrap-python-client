"""
This type stub file was generated by pyright.
"""

from abc import ABC, abstractmethod

class IFileReader(ABC):
    @abstractmethod
    async def read_file(self, file_path: str) -> bytearray:
        ...
    


