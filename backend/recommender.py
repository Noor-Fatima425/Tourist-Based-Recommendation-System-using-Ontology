from rdflib import Graph, Namespace, RDF  # Make sure RDF is included!

def get_recommendations(tourist_name, weather):
    g = Graph()
    g.parse("tourism_ontology.ttl", format="turtle")

    T = Namespace("http://example.org/tourism#")

    tourist_uri = None
    weather = weather.capitalize()

    for t in g.subjects(RDF.type, T.Tourist):
        name = g.value(t, T.name)
        if name and str(name).lower() == tourist_name.lower():
            tourist_uri = t
            break

    if not tourist_uri:
        return {"error": f"Tourist '{tourist_name}' not found."}

    budget = g.value(tourist_uri, T.hasBudget)
    preferred_transports = set(g.objects(tourist_uri, T.hasTransportPreference))
    preferred_activities = set(g.objects(tourist_uri, T.hasPreference))
    preferred_seasons = set(g.objects(tourist_uri, T.hasPreferredSeason))  # multiple seasons

    budget_to_accommodation = {
        T.Low: [T.BudgetHotel],
        T.Medium: [T.BudgetHotel, T.FourStarHotel],
        T.High: [T.BudgetHotel, T.FourStarHotel, T.BeachResort]
    }

    allowed_accommodation = budget_to_accommodation.get(budget, [])

    recommendations = []

    for dest in g.subjects(RDF.type, T.Destination):
        dest_weather = g.value(dest, T.hasWeather)
        dest_season = g.value(dest, T.hasSeason)
        dest_transports = set(g.objects(dest, T.hasTransportOption))
        dest_accommodation = g.value(dest, T.hasAccommodation)
        dest_activities = set(g.objects(dest, T.hasActivity))

        if (
            dest_weather == T[weather] and
            dest_season in preferred_seasons and
            preferred_transports & dest_transports and
            dest_accommodation in allowed_accommodation and
            preferred_activities & dest_activities
        ):
            recommendations.append(dest.split("#")[-1])
            
    if not recommendations:
        fallback_message = "No exact match found for your preferences. You may consider exploring popular destinations like Manali or Munnar in winter."
    return [], fallback_message

    return recommendations, ""


    return {
        "tourist": tourist_name,
        "weather": weather,
        "destinations": recommendations
    }
