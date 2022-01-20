import React from 'react';
import {
    BrowserRouter as Router,
    Link
} from "react-router-dom";

const navlinks = () => {
    return (
        <Router>
            <div>
                <div className='d-inline-block justify-content-across align-items-center p-2'>
                    <Link to='/' className='navbar-brand'>
                        <img src='img/me-full.jpg' alt="Logo" width='30px' height='30px' class="d-inline-block align-top "/>
                        <div className='d-inline-block align-top ml-5'>Breydon Brennan</div>
                    </Link>
                </div>
                <div className='d-inline-block'>
                    <Link to='/projects' className='navbar-brand'>Projects</Link>
                    <Link to='/about' className='navbar-brand'>About</Link>
                    <Link to='/contact' className='navbar-brand'>Contact</Link>
                </div>
            </div>
        </Router>
    )
}

export default navlinks
