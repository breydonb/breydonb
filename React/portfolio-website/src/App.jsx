import React from 'react';
import Footer from './components/Footer';

import { Route, Routes } from 'react-router-dom';
import {LinkContainer} from 'react-router-bootstrap'
import { Container, Navbar, Nav, Offcanvas, NavDropdown } from 'react-bootstrap';

import Home from "./components/Home"
import About from "./components/About"
import Contact from "./components/Contact"
import ProjectPage from "./components/projects/ProjectPage"
import Blog from './components/blog/Blog';
import ErrorNotFound from './components/ErrorNotFound';

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/';
import './App.css';

import { BrowserRouter as Router} from "react-router-dom";

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
      <Navbar collapseOnSelect bg="dark" variant='dark' expand="lg">
        <Container>
          <Navbar.Brand>Breydon Brennan</Navbar.Brand>
          <Navbar.Toggle aria-controls="responsive-navbar-nav" />
          <Navbar.Collapse id="responsive-navbar-nav">
            <Nav className="me-auto">
              <LinkContainer to="/">
                <Nav.Link>Home</Nav.Link>
              </LinkContainer>
              <LinkContainer to="/projects">
                <Nav.Link >Projects</Nav.Link>
              </LinkContainer>
              <LinkContainer to="/about">
                <Nav.Link>About</Nav.Link>
              </LinkContainer>
              <LinkContainer to="/blogs">
                <Nav.Link>Blog Posts</Nav.Link>
              </LinkContainer>
              <LinkContainer to="/contact">
                <Nav.Link>Contact</Nav.Link>
              </LinkContainer>
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/projects" element={<ProjectPage />} />
        <Route path="/about" element={<About />} />
        <Route path="/contact" element={<Contact />} />
        <Route path="/blogs" element={<Blog />} />
        <Route path="*" element={<ErrorNotFound />} />
      </Routes>

      <Footer />

    </Router>

  )
}

export default App
