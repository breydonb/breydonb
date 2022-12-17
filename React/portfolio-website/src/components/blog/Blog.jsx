import { React, useEffect, useState} from 'react';
import { Container, Row, Col } from 'react-bootstrap';

import 'bootstrap/dist/css/bootstrap.css';

import '../../App.css';

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