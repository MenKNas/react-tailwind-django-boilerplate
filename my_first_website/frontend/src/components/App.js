import * as React from "react";
import Header from "./Header/Header";
import TodosList from "./Todos/TodosList";

export default function App() {
  return (
    <div className="App">
      <Header />
      <div className="p-4 space-y-4">
        <h2> Welcome to our Django-React application</h2>
        <p> This is an amazing django react app</p>
        <p className="text-red-800">
          The author of this amazing application is: <i> Menelaos Nasies </i>
        </p>
        <p className="text-lg font-bold"> We LOVE TailwindCSS ! </p>
        <TodosList />
      </div>
    </div>
  );
}
