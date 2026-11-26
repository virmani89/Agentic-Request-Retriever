from typing import TypedDict, Optional


class RequestState(TypedDict):

    query: str

    file_name: Optional[str]

    file_path: Optional[str]

    file_content: Optional[str]

    similarity_score: Optional[float]

    error: Optional[str]