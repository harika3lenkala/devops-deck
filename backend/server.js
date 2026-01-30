const express = require("express");

const app = express();
const PORT = 5000;

app.get("/", (req, res) => {
  res.send("🚀 DevOps Deck Backend is running!");
});

app.listen(PORT, () => {
  console.log(`DevOps Deck server running on port ${PORT}`);
});
