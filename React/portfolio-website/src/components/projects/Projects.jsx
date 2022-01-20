import 'bootstrap/dist/css/bootstrap.css';
import '../../App.css'
import React from 'react';

import Data from '../data/Project.json';

function Projects(){
    return(
        <>
        <div className="album bg-dark">
        <div className='spacer layer-wave d-block'></div>
        <div className='spacer layer-peak d-block'></div>
            <h1 className='text-light text-center position-relative'>My Favorite Projects</h1>
            <br />
            <div className='container'>
                <div className='row'>
                    {Data.map(project =>{
                        return(
                            <div className='col-md-4'>
                                <div className='card mb-4 box shadow'>
                                    <img className='card-img-top' src={project.img} alt={project.alt} />
                                    <div className='card-body'>
                                        <h5 class="card-title">{project.title}</h5>
                                        <p className='card-text'>{project.desc}</p>
                                        <a href={project.link} class="btn btn-primary btn-lg active" role="button" aria-pressed="true">See the Source Code!</a>
                                    </div>
                                </div>
                            </div>
                        )
                    })}
                </div>
            </div>
        </div>
        </>
    )
}
export default Projects
