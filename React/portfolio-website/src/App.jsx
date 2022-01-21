import React from 'react';
import Home from "./components/Home"
import About from "./components/About"
import ProjectPage from "./components/projects/ProjectPage"

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/';
import './App.css';

import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Contact from './components/Contact';

import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";

const firebaseConfig = {
  apiKey: "AIzaSyBx5iO2zA3DnWx7swuU6uvJFTnUo48GztE",
  authDomain: "portfolio-breydonb.firebaseapp.com",
  projectId: "portfolio-breydonb",
  storageBucket: "portfolio-breydonb.appspot.com",
  messagingSenderId: "395264269390",
  appId: "1:395264269390:web:2d9bf8d4ddc24a6977371f",
  measurementId: "G-P821T6KLCS"
};

const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

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
