async function fetchData() {
  const url = "https://api.thingspeak.com/channels/3070629/feeds.json?api_key=27DHR8P0U9CD6H7I&results=10";

  try {
    const response = await fetch(url);
    const data = await response.json();
    console.log("Full ThingSpeak JSON:", data);  // 👈 check all fields

    const feeds = data.feeds;
    if (!feeds || feeds.length === 0) {
      console.error("No data found");
      return;
    }

    const latest = feeds[feeds.length - 1];
    console.log("Latest entry:", latest);  // 👈 see which fields have values

    // Temporarily print all fields
    for (let i = 1; i <= 8; i++) {
      console.log(`field${i}:`, latest[`field${i}`]);
    }

    // Update based on real mapping
    document.getElementById("ph").innerText = latest.field1 || "N/A";
    document.getElementById("turbidity").innerText = latest.field2 || "N/A";
    document.getElementById("color").innerText = latest.field3 || "N/A";

  } catch (error) {
    console.error("Error fetching data:", error);
  }
}

fetchData();
