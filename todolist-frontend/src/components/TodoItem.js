import React from 'react';
import axios from 'axios';

const TodoItem = ({ todo, fetchTodos }) => {
  const completeTodo = async () => {
    try {
      await axios.put(`http://localhost:8000/todos/${todo.id}`, {
        completed: !todo.completed,
      });
      fetchTodos();
    } catch (error) {
      console.error('Error updating todo:', error);
    }
  };

  const deleteTodo = async () => {
    try {
      await axios.delete(`http://localhost:8000/todos/${todo.id}`);
      fetchTodos();
    } catch (error) {
      console.error('Error deleting todo:', error);
    }
  };

  return (
    <li>
      <input
        type="checkbox"
        checked={todo.completed}
        onChange={completeTodo}
      />
      <span style={{ textDecoration: todo.completed ? 'line-through' : '' }}>
        {todo.name}
      </span>
      <button onClick={deleteTodo}>Delete</button>
    </li>
  );
};

export default TodoItem;
