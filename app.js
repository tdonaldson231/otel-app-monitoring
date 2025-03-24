/*app.js*/
const express = require('express');

const PORT = parseInt(process.env.PORT || '8080');
const app = express();

function getRandomNumber(min, max) {
  return Math.floor(Math.random() * (max - min + 1) + min);
}

app.get('/health', (req, res) => {
  res.json({ status: "ok" });
});

app.get('/random', (req, res) => {
  res.send(getRandomNumber(1, 100).toString());
});

app.get('/quote', (req, res) => {
  res.send("The quick brown fox jumps over the lazy dog.");
});

app.listen(PORT, () => {
  console.log(`Listening for requests on http://localhost:${PORT}`);
});
