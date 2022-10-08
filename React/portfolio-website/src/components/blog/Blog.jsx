import { React, useEffect, useState} from 'react';
import { axios } from 'axios';

import 'bootstrap/dist/css/bootstrap.css';

import '../../App.css';

import { ErrorNotFound } from '../ErrorNotFound'

import { API_VAR } from '../../api-var';
import { Button, Badge} from 'react-bootstrap';
import axios from 'axios';

function Blog(){
    const [ data, setData ] = useState([]);
    const [ error, setErrorCode ] = useState([""])

    useEffect( () => {
        loadBlogs()
    }, [])

    const loadBlogs = async () => {
        try{
            await fetch(API_VAR.BLOG_URL)
                .then(response => response.json())
                .then(receivedData => setData(receivedData))
        }
        catch(e){
            console.error(e)
        }
    }

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

export default Blog