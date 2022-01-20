import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/';
import '../../App.css';

import Home from "../Home";
import About from "../About";
import ProjectPage from "../projects/ProjectPage";
import Contact from '../Contact';

import React from 'react';


import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";


/* 
    <Link to='/' className='navbar-brand'>Breydon Brennan</Link>
    <Link to='/projects' className='navbar-brand'>Projects</Link>
    <Link to='/about' className='navbar-brand'>About</Link>
    <Link to='/contact' className='navbar-brand'>Contact</Link>
*/

function Navigation(){   
    return (
        <Router>
            <nav className='d-flex justify-content-around align-items-center'>
                <Link to='/' className='navbar-brand'>
                    <img src='img/me-full.jpg' alt="Logo" width='30px' height='30px' class="d-inline-block align-top "/>
                    <div className='d-inline-block align-top ml-5'>Breydon Brennan</div>
                </Link>
                <Link to='/projects' className='navbar-brand'>Projects</Link>
                <Link to='/about' className='navbar-brand'>About</Link>
                <Link to='/contact' className='navbar-brand'>Contact</Link>
            </nav>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/projects" element={<ProjectPage />} />
                <Route path="/about" element={<About />} />
                <Route path="/contact" element={<Contact />} />
                {/* <Route path="*" element={<About />} /> */}
            </Routes>
      </Router>
    )
}



export default Navigation
