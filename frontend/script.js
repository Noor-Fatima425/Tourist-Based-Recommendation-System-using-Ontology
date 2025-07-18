async function getRecommendations() {
  const tourist = document.getElementById("tourist").value;
  const weather = document.getElementById("weather").value;

  const responseArea = document.getElementById("output");
  responseArea.innerHTML = `<span style="color: #2980b9;">Fetching your personalized recommendations...</span>`;

  try {
    const response = await fetch("http://127.0.0.1:5000/recommend", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ tourist, weather })
    });

    if (!response.ok) {
      let errorMessage = "Unknown error occurred.";
      try {
        const error = await response.json();
        errorMessage = error.error || errorMessage;
      } catch (_) {}
      responseArea.innerHTML = `<span style="color: red;">Error: ${errorMessage}</span>`;
      return;
    }

    const data = await response.json();

    if (data.destinations && data.destinations.length > 0) {
      responseArea.innerHTML = `
        <div style="background: #eafaf1; padding: 15px; border-radius: 8px; color: #2c3e50;">
          <p>🌍 <strong>Tourist:</strong> ${data.tourist}</p>
          <p>☁️ <strong>Weather:</strong> ${data.weather}</p>
          <p>📍 <strong>Recommended Destinations:</strong><br> 
            <ul style="list-style-type: square; text-align: left; display: inline-block;">
              ${data.destinations.map(d => `<li>${d}</li>`).join("")}
            </ul>
          </p>
        </div>
      `;
    } else {
      responseArea.innerHTML = `<span style="color: orange;">❄️ No exact match found for your preferences. You may consider exploring popular destinations like Manali or Munnar in winter.</span>`;
    }
  } catch (error) {
    responseArea.innerHTML = `<span style="color: red;">Network Error: ${error.message}</span>`;
  }
} 