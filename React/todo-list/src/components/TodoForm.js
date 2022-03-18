import { Button, ButtonGroup, Form } from 'react-bootstrap';
import { Plus, ArrowRepeat } from 'react-bootstrap-icons';

import React, {useState, useEffect, useRef} from 'react';

export default function TodoForm(props) {

    const [input, setInput] = useState(props.edit ? props.edit.value : '');
    
    const inputRef = useRef(null);

    useEffect(() => {
        inputRef.current.focus()
    })

    const handleSubmit = (e) => {
        e.preventDefault();

        props.onSubmit({
            id: Math.floor(Math.random() * 1000),
            text: input,
        });

        setInput("");
    }

    const handleChange = (e) =>{
        setInput(e.target.value);
    }

    return(  
        <Form className='containter' onSubmit={handleSubmit}> 
            <Form.Group controlId='formAddTask' className='row p-3'>

            {props.edit ? (
                <>
                    <Form.Control type="name" placeholder="Edit" className="col-sm" value={input} onChange={handleChange} ref={inputRef}/>
                    <Button variant='primary' className='col-sm-2'>
                        <ArrowRepeat size={25} />
                    </Button>
                </>
            ) : (
                <>
                    <Form.Label className="d-flex col-sm-4 justify-content-center align-items-center">Task Name</Form.Label>
                    <Form.Control type="name" placeholder="Enter Task Name" className="col-sm" value={input} onChange={handleChange} ref={inputRef}/>
                    <ButtonGroup className='col-sm-2' size='sm'>
                        <Button variant='primary' type='submit' value='submit'>
                            <Plus size={25}/>
                        </Button>
                    </ButtonGroup>
                </>
            )}         

            </Form.Group>
            
        </Form>
    )
}