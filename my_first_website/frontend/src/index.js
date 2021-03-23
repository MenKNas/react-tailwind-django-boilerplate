import * as React from "react";
import ReactDOM from "react-dom";
import reportWebVitals from "../static/frontend/reportWebVitals";
import App from "./components/App";
import "../static/css/index.css";
import { QueryClient, QueryClientProvider } from "react-query";

const root = document.getElementById("root");

const queryClient = new QueryClient();

ReactDOM.render(
  <React.StrictMode>
    <QueryClientProvider client={queryClient}>
      <App />
    </QueryClientProvider>
  </React.StrictMode>,
  root
);

reportWebVitals();
