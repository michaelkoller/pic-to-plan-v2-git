import pydot
graph = pydot.graph_from_dot_file("nx_11440.dot")

# SHOW as an image
import tempfile
fout = tempfile.NamedTemporaryFile(suffix=".png")
graph.write(fout.name,format="png")
