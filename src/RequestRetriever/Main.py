from src.RequestRetriever.Graph.graph import RequestGraph


# Create graph object

request_graph = RequestGraph()


def run_agent(query):

    # Execute LangGraph

    result = request_graph.run(query)

    return result