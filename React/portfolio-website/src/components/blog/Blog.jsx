import { React, useEffect, useState} from 'react';
import { Container, Row, Col } from 'react-bootstrap';
import { FirestoreQueryContext } from '../../contexts/FirestoreContext';

import 'bootstrap/dist/css/bootstrap.css';

import '../../App.css';
import { doc } from 'firebase/firestore';



function Blog(){
    const { getDocuments, data} = FirestoreQueryContext();

    useEffect(() =>{
        try{
            getDocuments("blogs")
        }
        catch(e){
            console.log(e.message)
        }
    }, [])

    return(
        <Container>
            <Row>
                {data.map((blog)=>{
                    return(
                        <p>{blog.body}</p>
                    )
                })}
            </Row>
        </Container>
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

export default Blog