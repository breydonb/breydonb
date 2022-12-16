import { React, useEffect, useState} from 'react';

import 'bootstrap/dist/css/bootstrap.css';

import '../../App.css';

import { ErrorNotFound } from '../ErrorNotFound'

import { API_VAR } from '../../api-var';
import { Button, Badge, Container, Row, Col} from 'react-bootstrap';
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
    return(

        <div className='blog-container'>
            {data.map(post =>(
                    <div className='blog-card' key={post.BlogId}>
                        <img src="img/ph.svg" className='card-img' width='600'/>
                        <div className='card-body p-2'>
                            <div className=''>
                                <Badge pill bg="primary">{post.PostCategory}</Badge>
                                <h4>{post.Title}</h4>
                            </div>
                            <p>{post.BlogDesc}</p>
                        </div>
                        <div className='card-footer d-flex justify-content-between align-items-center p-2'>
                            <small>{post.PublishDate}</small>
                            <Button 
                                variant="primary">Read More</Button>
                        </div>
                    </div>
            ))}

        </div>
    )
}

function BlogStillDeveloped(){
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