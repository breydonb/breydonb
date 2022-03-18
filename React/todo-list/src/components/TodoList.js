import React, {useState} from 'react';
import Todo from './Todo';
import TodoForm from './TodoForm';

export default function TodoList() {

    const [todos, setTodos] = useState([]);

    const addTodos = (todo) => {
        if(!todo.text || /^\s*$/.test(todo.text)){
            return;
        }

        const newTodos = [todo, ...todos];
        setTodos(newTodos);
        console.log(...todos);
    }

    const updateTodo = (todoId, newValue) =>{
        if(!newValue.text || /^\s*$/.test(newValue.text)){
            return;
        }
        setTodos(prev => prev.map(item => (item.id === todoId ? newValue : item)))
    }

    const completeTodo = (id) => {
        let updatedTodos = todos.map(todo =>{
            if(todo.id === id){
                todo.isComplete = !todo.isComplete;
            }
            return todo;
        })
        setTodos(updatedTodos);
    }

    const removeTodo = (id) =>{
        const removeArr = [...todos].filter(todo => todo.id !== id );

        setTodos(removeArr);
    }

    

    return (
        <div>
            <h1>Add Task</h1>
            <TodoForm onSubmit={addTodos}/>
            <div className='container'>
                <Todo todos={todos} completeTodo={completeTodo} removeTodo={removeTodo} updateTodo={updateTodo}/>
            </div>
            
        </div>
    )
}