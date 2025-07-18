from rdflib import RDFS

def get_label(graph, uri):
    """
    Returns rdfs:label of a URI if available; otherwise returns the last part of the URI.
    """
    label = graph.label(uri)
    return str(label) if label else uri.split("#")[-1]
