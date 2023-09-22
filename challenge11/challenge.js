const express = require('express');
const app = express();

app.get('/.env', (req, res) => {
  res.sendFile(path.join(__dirname, '.env'));
});


app.get('/config', (req, res) => {
  res.send('Configurations go here.');
});

app.listen(3000);
