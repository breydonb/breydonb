import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';

import data from "./data/data.json";

import { React, useState } from 'react';
import TodoList from './components/TodoList';

function App() {

  const [tasks, setList] = useState(data);

  return (
    <div className='text-center'>
      <TodoList />
    </div>
  );
}

export default App;
