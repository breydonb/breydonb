import React, { useState, useEffect, useRef } from 'react';
import { Card } from 'react-bootstrap';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import { UserAuth } from '../../contexts/AuthContext';
import { Link, useNavigate } from 'react-router-dom';
import ErrorAlert from '../ErrorHandling/ErrorAlert';


function SignUp() {

    const[email, setEmail] = useState('');
    const[password, setPassword] = useState('');
    const[confirmPassword, setConfirmPassword] = useState('');
    const[error, setError] = useState('');
    const[isMatch, setIsMatch] = useState(false);

    const { createUser } = UserAuth();
    const navigate = useNavigate()

    const handleConfirmPassword = (e) =>{
        setConfirmPassword(e.target.value)
    }

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError('');
        try{
            await createUser(email, password);
            navigate('/');
        }catch(e){
            setError(e.message);
            console.log(error);
        }
        
    }

    useEffect(() =>{
        if(password === confirmPassword){
            setIsMatch(true);
        }
        else{
            setIsMatch(false);
        }
    })

    return (
    <Card className='d-flex align-items-center justify-content-center'>
        <h2>Sign Up</h2>
        <p>Already have an account? <Link to="/login" className='underline'>Login</Link> here</p>
        <Form onSubmit={handleSubmit}>
            <Form.Group className='mb-3' controlId='formEmailAddress'>
                <Form.Label>Email Address</Form.Label>
                <Form.Control
                    type='email'
                    placeholder='Enter email'
                    value={email}
                    onChange={(e) => {setEmail(e.target.value)}}
                />
            </Form.Group>
            <Form.Group className='mb-3' controlId='formPassword'>
                <Form.Label>Password</Form.Label>
                <Form.Control
                    type='password'
                    placeholder='Enter password'
                    value={password}
                    onChange={(e) => {setPassword(e.target.value)}}/>
            </Form.Group>
            <Form.Group className='mb-3' controlId='formConfirmPassword'>
                <Form.Label>Confirm Your Password</Form.Label>
                <Form.Control
                    type='password'
                    placeholder='Confirm your password'
                    value={confirmPassword}
                    onChange={handleConfirmPassword}
                />
            </Form.Group>
            {isMatch ? '' : <div>Passwords must match</div>}
            <p>Your information will never be sent to any third-party sites</p>
            <Button variant='primary' type='submit' disabled={!isMatch} >Submit</Button>
            {error ? <ErrorAlert errorMessage={error}/> : ''}
        </Form>
    </Card>
    
    )
}

export default SignUp;