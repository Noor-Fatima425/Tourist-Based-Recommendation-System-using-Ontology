# Tourist-Based-Recommendation-System-using-Ontology
A personalized travel recommendation web app that uses semantic web technologies to suggest destinations to users based on their preferences. It leverages an RDF-based ontology(tourist_ontology.ttl), SPARQL queries, and a Python Flask backend to create intelligent tourist experiences.

-  Ontology-based knowledge model for destinations and tourists
-  Recommends destinations based on:
  Activity
  preferences
  Budget
  Season
  Transport preferences
- Bi-directional SPARQL querying using rdflib
- Web-based interface for entering preferences and viewing results

# Ontology Details (tourist_ontology.ttl)
The ontology defines key classes and relationships for tourism such as:
-Classes:
Tourist, Destination, Trip, Activity, Transport, Accommodation, Season, Weather, Cost
-Properties:
hasPreference, hasBudget, hasPreferredSeason, hasTransportPreference, hasActivity, etc.
-Instances:
Tourists: Noor,Toby etc.
Destinations: Manali, Paris, Goa, Bali, etc.
-Each destination is linked to seasonal/weather conditions, transport options, and possible activities.
