const express = require("express");
const app = express();

app.use(express.json());

app.post("/login", (req, res) => {
  console.log(req.body);

  res.json({
    message: "OK"
  });
});

app.listen(3000);
const express = require("express");
const app = express();

app.use(express.json());

app.get("/", (req, res) => {
  res.send("サーバー動いてる！");
});

app.post("/login", (req, res) => {
  console.log(req.body);

  res.json({
    message: "OK"
  });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT);
