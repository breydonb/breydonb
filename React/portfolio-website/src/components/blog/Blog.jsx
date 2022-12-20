import { React, useEffect, useState} from 'react';
import { Container, Row, Col } from 'react-bootstrap';

import 'bootstrap/dist/css/bootstrap.css';

import '../../App.css';

<<<<<<< HEAD
function BlogStillDeveloped(){
=======
import { ErrorNotFound } from '../ErrorHandling/ErrorNotFound'

import { Button, Badge} from 'react-bootstrap';
import axios from 'axios';


function Blog(){
    const [ data, setData ] = useState([]);
    const [ error, setErrorCode ] = useState("");

    useEffect( () => {
        axios.get("https://localhost:44371/api/blog")
            .then(res => {
                // console.log(res.data)
                setData(res.data)
            })
            .catch(function (err) {
                if(err.response) {
                    console.log(err.response.data);
                    console.log(err.response.status);
                    console.log(err.response.headers);
                }
                else{
                    console.log(err)
                }
                setErrorCode(err)
            })
    }, [])


    if(error){
        return (
            <ErrorNotFound />
        )
    }
>>>>>>> b1492b5b8190b18eb70a91012a884fd60c3776d3
    return(
        <Container className='p-2'>
            <Row>
                <Col>
                    <p>We're still working on this page</p>
                </Col>
            </Row>
        </Container>
    )
}

export default BlogStillDeveloped