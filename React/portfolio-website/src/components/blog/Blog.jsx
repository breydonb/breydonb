import  React, {useEffect, useState} from 'react';
import { Container, Row, Col, Card } from 'react-bootstrap';
import { FirestoreQueryContext } from '../../contexts/FirestoreContext';
import { StorageQueryContext } from '../../contexts/StorageContext';


import 'bootstrap/dist/css/bootstrap.css';

import '../../App.css';


function Blog(){
    const { getDocuments, data} = FirestoreQueryContext();
    const { getImages, urlRef } = StorageQueryContext();
    const [isRendering, setRendering] = useState(false)

    useEffect(() =>{
        try{
            getDocuments("blogs")
            if(data.length > 1) {
                getImages()
            } else{
                // console.log("case 0")
                setRendering(!isRendering)
            }
            
        }
        catch(e){
            console.log(e.message)
        }
    },[data.current, isRendering])

    const renderPhotos = () => {
        urlRef.current.map((url) =>{
            return <Card.Img src={url} />
        })
    }

    return(
        <Container className='p-3'>
            <Row>
                {data.map((blog, index)=>{
                    return(
                        <Col md={4} key={blog.id} className="p-3">
                            <Card>
                                <Card.Img src={urlRef.current[index]} />
                                <Card.Body>
                                    <Card.Title>{blog.title}</Card.Title>
                                    <Card.Text>{blog.desc}</Card.Text>
                                </Card.Body>
                                
                            </Card>
                        </Col>
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