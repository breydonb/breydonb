import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/';
import '../App.css';

import { Sling as Hamburger } from 'hamburger-react';

import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link
  } from "react-router-dom";

/* 
    <Link to='/' className='navbar-brand'>Breydon Brennan</Link>
    <Link to='/projects' className='navbar-brand'>Projects</Link>
    <Link to='/about' className='navbar-brand'>About</Link>
    <Link to='/contact' className='navbar-brand'>Contact</Link>
*/

const navigation = () => {
    return (
        <Router>
            <nav className="navbar navbar-light bg-light">
                <div className='d-flex justify-content-between ml-5'>
                    <Link to='/' className='navbar-brand'>
                        <img src='img/me-full.jpg' alt="Logo" width='30px' height='30px' class="d-inline-block align-top "/>
                        <div className='d-inline-block align-top ml-5'>Breydon Brennan</div>
                    </Link>
                </div>
                <div className='d-flex align-items-center mr-5 navigation-element'>
                    <Link to='/projects' className='navbar-brand'>Projects</Link>
                    <Link to='/about' className='navbar-brand'>About</Link>
                    <Link to='/contact' className='navbar-brand'>Contact</Link>
                    <Hamburger 
                        size={20}
                        onToggle={toggle =>{
                            if(toggle){
                                handleClick()
                            }else{
                                handleClick()
                            }
                        }}
                        className='d-inline-flex'
                    />
                </div>
            </nav>
        </Router>
    )
}

function handleClick(){

}

export default navigation
