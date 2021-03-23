import * as React from "react";
import { useQuery } from "react-query";

const fetchTodos = async () => {
  const res = await fetch("http://127.0.0.1:8000/api/todos/");
  const finalData = await res.json();
  return finalData;
};

export default function TodosList() {
  const { isLoading, error, data, isFetching } = useQuery(
    "todoslist",
    fetchTodos
  );

  if (isLoading || isFetching) return <p> fetching todos....</p>;

  if (error)
    return (
      <p className="text-red-500 bg-red-200 text-center p-4 rounded-sm">
        Oops..something went wrong...give it a few minutes and try again soon{" "}
      </p>
    );

  return (
    <div>
      <h3 className="text-xl text-red-900 text-center"> TODOs </h3>
      {data?.map((todo) => (
        <div
          key={todo.id}
          className="flex flex-col items-center justify-center p-4 shadow-lg"
        >
          <span className="font-bold"> {todo.title} </span>
          <span> {todo.content}</span>
        </div>
      ))}
    </div>
  );
}
