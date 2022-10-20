"""
This type stub file was generated by pyright.
"""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
from result import Result
from .uri_resolver import TryResolveUriOptions
from .uri_package_wrapper import UriPackageOrWrapper

if TYPE_CHECKING:
    ...
class UriResolverHandler(ABC):
    @abstractmethod
    async def try_resolve_uri(self, options: TryResolveUriOptions) -> Result[UriPackageOrWrapper, Exception]:
        ...
    


