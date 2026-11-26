
from pathlib import Path

from langgraph.graph import StateGraph, START, END

from src.RequestRetriever.State.state import RequestState
from src.RequestRetriever.Nodes.search_node import search_node


class RequestGraph:

    def __init__(self):

        # Step 1: Create StateGraph
        builder = StateGraph(RequestState)

        # Step 2: Add nodes
        builder.add_node("search_node", search_node)

        # Step 3: Define graph flow
        builder.add_edge(START, "search_node")
        builder.add_edge("search_node", END)

        # Step 4: Compile graph
        self.graph = builder.compile()

    # Execute graph
    def run(self, query):

        result = self.graph.invoke({
            "query": query,
            "file_name": None,
            "file_path": None,
            "file_content": None,
            "similarity_score": None,
            "error": None
        })

        return result

    # Generate Mermaid diagram
    def get_graph_diagram(self):

        return self.graph.get_graph().draw_mermaid()

    # Generate PNG image
    def save_graph_image(
        self,
        output_path="request_retriever_graph.png"
    ):

        png_data = self.graph.get_graph().draw_mermaid_png()

        output_path = Path(output_path)

        output_path.write_bytes(png_data)

        print(
            f"Graph image generated successfully: "
            f"{output_path.resolve()}"
        )

        return str(output_path.resolve())


# Create graph instance
request_graph = RequestGraph()


# Run directly to generate graph image
if __name__ == "__main__":

    print("\nLangGraph Architecture:\n")

    print(request_graph.get_graph_diagram())

    request_graph.save_graph_image()
