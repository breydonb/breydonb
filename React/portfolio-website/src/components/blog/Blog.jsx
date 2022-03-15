import { React, useEffect, useState} from 'react';

import 'bootstrap/dist/css/bootstrap.css';

import '../../App.css';

import { API_VAR } from '../../api-var';
import { Button, Badge} from 'react-bootstrap';


function Blog(){
    const [ data, setData ] = useState([]);

    useEffect( () => {
        loadBlogs();
        // getData();
    }, [])

    const loadBlogs = async () => {
        try{
            await fetch(API_VAR.BLOG_URL)
                .then(response => response.json())
                .then(receivedData => setData(receivedData))
        }
        catch(e){
            console.log(e)
        }
    }


    console.log(data)

    return(
        <div className='blog-container'>
            {data.map(post =>(
                    <div className='blog-card'>
                        <img src="img/ph.svg" className='card-img' width='600'/>
                        <div className='card-body'>
                            <div className=''>
                                <Badge pill bg="primary">{post.PostCategory}</Badge>
                                <h4>{post.Title}</h4>
                            </div>
                            <p>{post.BlogDesc}</p>
                        </div>
                        <div className='card-footer d-flex justify-content-between align-items-center'>
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