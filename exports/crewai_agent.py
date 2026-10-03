from crewai import Agent

synthetic_graph_topology_generator = Agent(
    role="Synthetic Graph Topology Generator",
    goal="Deliver high-precision autonomous Synthetic Graph Topology Generator operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
