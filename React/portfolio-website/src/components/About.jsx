import React from 'react';
import "../App.css";
import "react-responsive-carousel/lib/styles/carousel.min.css"; // requires a loader
import 'bootstrap/dist/css/bootstrap.css';

function about() {
    return (
        <div>
            <h2 className='text-center'>About Me</h2>
            {/* <div className='container'>
                <div className='row justify-content-around'>
                    <div className='col-sm'>
                        <img src='img/me-full.jpg' alt='my portrait' className='about-picture rounded-circle'/>
                    </div>
                    <div className='col-sm-6'>
                        <p className='text-justify'>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed faucibus turpis id ornare consequat. Praesent euismod metus est, et faucibus mi condimentum quis. Integer ullamcorper tincidunt facilisis. Praesent in erat vitae arcu pulvinar suscipit. Suspendisse consequat nec odio maximus interdum. Nullam porttitor velit diam, id semper metus tempor at. Sed ut dolor blandit, sagittis velit non, porttitor magna. Duis posuere sed quam nec commodo. In sed pulvinar nibh.</p>
                    </div>
                </div>
            </div> */}
            <div className='d-flex flex-column align-items-left justify-content-center p-4'>
                <div>
                    <img src='img/me-full.jpg' alt='my portrait' className='about-picture rounded-circle'/>
                </div>
                <p className='text-justify'>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed faucibus turpis id ornare consequat. Praesent euismod metus est, et faucibus mi condimentum quis. Integer ullamcorper tincidunt facilisis. Praesent in erat vitae arcu pulvinar suscipit. Suspendisse consequat nec odio maximus interdum. Nullam porttitor velit diam, id semper metus tempor at. Sed ut dolor blandit, sagittis velit non, porttitor magna. Duis posuere sed quam nec commodo. In sed pulvinar nibh.</p>
            </div>
        </div>
    )
}

export default about
