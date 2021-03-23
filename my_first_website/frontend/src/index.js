import * as React from "react";
import ReactDOM from "react-dom";
import reportWebVitals from "../static/frontend/reportWebVitals";
import App from "./components/App";
import "../static/css/index.css";

const root = document.getElementById("root");

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  root
);

reportWebVitals();
