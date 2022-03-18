import React, {useState} from 'react';
import TodoForm from './TodoForm';
import TodoList from './TodoList';

import { Button, ButtonGroup } from 'react-bootstrap';

import { Trash, PencilSquare } from 'react-bootstrap-icons';

export default function Todo({todos, completeTodo, removeTodo, updateTodo }) {

    const [edit, setEdit] = useState({
        id: null,
        value: '',
    });

    const submitUpdate = (value) => {
        updateTodo(edit.id, value);
        setEdit({
            id: null,
            value: ''
        })
    }

    if(edit.id){
        return <TodoForm edit={edit} onSubmit={submitUpdate} />
    }

    return todos.map((todo, index) =>(
        <div key={index} className='row p-3'>
            <div className='col-sm-8' key={todo.id} onClick={() => completeTodo(todo.id)}>
                {todo.text}
            </div>
            <ButtonGroup className='col-sm-2'>
                <Button variant='danger' onClick={() => removeTodo(todo.id)}>
                    <Trash size={25}/>
                </Button>
                <Button variant='primary' onClick={() => setEdit({id: todo.id, value: todo.text})}>
                    <PencilSquare size={20}/>
                </Button>
            </ButtonGroup>
        </div>
    ));
}