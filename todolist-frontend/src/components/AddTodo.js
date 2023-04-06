import React, { useState } from 'react';
import axios from 'axios';

const AddTodo = ({ fetchTodos }) => {
  const [title, setTitle] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      await axios.post('http://localhost:8000/todos', { name: title, description: '', due_date: '' });

      setTitle('');
      fetchTodos();
    } catch (error) {
      console.error('Error adding todo:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Add new to-do"
        value={title}
        onChange={(event) => setTitle(event.target.value)}
      />
      <button type="submit">Add</button>
    </form>
  );
};

export default AddTodo;
