from typing import List, Union

from ..types import Client, Env, Uri


def get_env_from_uri_history(
    uri_history: List[Uri], client: Client
) -> Union[Env, None]:
    for uri in uri_history:
        return client.get_env_by_uri(uri)
