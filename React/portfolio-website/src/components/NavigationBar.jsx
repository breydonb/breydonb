import React, {useState} from 'react'
import { LinkContainer } from 'react-router-bootstrap'
import { Container, Navbar, Nav, Offcanvas, NavDropdown } from 'react-bootstrap';
import {UserAuth} from '../contexts/AuthContext'
import { useNavigate } from 'react-router-dom';

function NavigationBar() {

    const { user, logout } = UserAuth();
    const [error, setError] = useState('')
    
    const navigate = useNavigate();
    const handleLogout = async (e) =>{
        try{
            await logout()
            navigate('/')
        }catch(e){
            setError(e.message)
        }
        
    }

    return (
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
                        <Nav.Link>Projects</Nav.Link>
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
                <Nav>
                {user ?
                    
                    <NavDropdown menuVariant='dark' title={user && user.email}>
                        <NavDropdown.Item>
                            <LinkContainer to="/account">
                                <Nav.Link black>Account Settings</Nav.Link>
                            </LinkContainer>
                        </NavDropdown.Item>
                        <NavDropdown.Item onClick={handleLogout}>Logout</NavDropdown.Item>
                    </NavDropdown>
                     
                : 
                    <><LinkContainer to="/signup">
                                <Nav.Link>{user ? '' : "Sign Up"}</Nav.Link>
                            </LinkContainer><LinkContainer to="/login">
                                    <Nav.Link>{user ? '' : "Log In"}</Nav.Link>
                                </LinkContainer></>
                }
                </Nav>
            </Navbar.Collapse>
            </Container>
        </Navbar>
    )
}

export default NavigationBar