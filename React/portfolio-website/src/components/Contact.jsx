import React from 'react';

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/';
import '../App.css';

function Contact() {
    return (
        <div>
            <div className='d-flex flex-column p-4'>
                <h2 >Contact Me</h2>
                <p>Below includes the information needed to contact me along with my resume.</p>
            </div>
            <div className='d-flex justify-content-around'>
                <p>Email:</p>
                <p>spyvsspy1113@gmail.com</p>
            </div>
            <div className='container'>
                <div className='row'>
                    <div className='col'>
                    <iframe src="https://drive.google.com/file/d/1On5U8trFZsZeP6xofTm-xsiEDfGOE-_s/preview" width="100%" height="720" allow="autoplay"></iframe>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Contact
