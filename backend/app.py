from flask import Flask, request, jsonify
from flask_cors import CORS
from rdflib import Graph, Namespace

app = Flask(__name__)
CORS(app)

g = Graph()
g.parse("tourism_ontology.ttl", format="turtle")

T = Namespace("http://example.org/tourism#")
g.bind("tourism", T)

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()
    tourist_name = data.get("tourist")
    weather = data.get("weather")

    if not tourist_name or not weather:
        return jsonify({"error": "Missing tourist name or weather"}), 400

    query = f"""
    PREFIX : <http://example.org/tourism#>

    SELECT DISTINCT ?destination WHERE {{
      ?tourist a :Tourist ;
               :name "{tourist_name}" ;
               :hasBudget ?budget ;
               :hasPreference ?activity ;
               :hasTransportPreference ?transport ;
               :hasPreferredSeason ?season .

      ?destination a :Destination ;
                   :hasWeather :{weather} ;
                   :hasActivity ?activity ;
                   :hasTransportOption ?transport ;
                   :hasSeason ?season ;
                   :hasAccommodation ?acc .
    }}
    """

    qres = g.query(query)

    destinations = [str(row.destination).split("#")[-1] for row in qres]

    if not destinations:
        return jsonify({"tourist": tourist_name, "weather": weather, "destinations": []}), 200

    return jsonify({"tourist": tourist_name, "weather": weather, "destinations": destinations})

    recommendations, note = recommend_places(user, g)
    if not recommendations:
        return jsonify({
        "recommendations": [],
        "message": note or "No recommendations found for the selected preferences."
    })
    else:
        return jsonify({
        "recommendations": recommendations,
        "message": "Recommendations retrieved successfully!"
    })
if __name__ == "__main__":
    app.run(debug=True)