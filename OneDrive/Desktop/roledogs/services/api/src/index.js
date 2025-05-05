require("dotenv").config();
const express = require("express");
const session = require("express-session");
const Keycloak = require("keycloak-connect");

const app = express();
const memoryStore = new session.MemoryStore();
app.use(
  session({
    secret: "roledogs-secret",
    resave: false,
    saveUninitialized: true,
    store: memoryStore,
  })
);

const keycloak = new Keycloak({ store: memoryStore });
app.use(keycloak.middleware());

app.get("/health", (req, res) => res.json({ status: "ok" }));

app.get("/profile", keycloak.protect(), (req, res) => {
  res.json({ user: req.kauth.grant.access_token.content.preferred_username });
});

const PORT = process.env.PORT || 4000;
app.listen(PORT, () => console.log(`API listening on ${PORT}`));
