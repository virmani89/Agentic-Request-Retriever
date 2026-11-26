
from src.RequestRetriever.Tools.search_tool import search_query_files
from src.RequestRetriever.State.state import RequestState


def search_node(state: RequestState):

    print("Search Node Started")

    # Get user's query
    user_query = state["query"]

    # Call search tool
    result = search_query_files.invoke({
        "query": user_query
    })

    # Check for errors or empty results
    if result.get("error") or not result.get("results"):
        return {
            "file_name": "",
            "file_path": "",
            "file_content": "",
            "similarity_score": 0,
            "error": result.get("error") or "No matching files found."
        }

    # Get the best matching file (first result)
    best_match = result["results"][0]

    # Update graph state
    return {
        "file_name": best_match["file_name"],
        "file_path": best_match["file_path"],
        "file_content": best_match["file_content"],
        "similarity_score": best_match["similarity_score"],
        "error": None
    }

