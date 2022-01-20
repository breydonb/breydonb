import React from 'react';
import Home from "./components/Home"
import About from "./components/About"
import ProjectPage from "./components/projects/ProjectPage"

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/';
import './App.css';

import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Contact from './components/Contact';


function App (){
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
        <Route path="*" element={<About />} />
      </Routes>
    </Router>
  )
}

export default App
