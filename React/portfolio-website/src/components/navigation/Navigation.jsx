import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/';
import '../../App.css';
import NavLinks from './NavLinks';

import React, { useState } from 'react';

import { Sling as Hamburger } from 'hamburger-react';

/* 
    <Link to='/' className='navbar-brand'>Breydon Brennan</Link>
    <Link to='/projects' className='navbar-brand'>Projects</Link>
    <Link to='/about' className='navbar-brand'>About</Link>
    <Link to='/contact' className='navbar-brand'>Contact</Link>
*/

const Navigation = () =>{
    const [ open, setOpen ] = useState(false);
    

    return (
        <div>
            {/* <Hamburger 
                size={20}
                toggled={open} toggle={setOpen}
            />
            {open && <NavLinks />} */}

            <nav className='navbar navbar-light'>
                <div>
                    <Hamburger 
                        size={20}
                        toggled={open} toggle={setOpen}
                        className='snap-right'
                    />
                </div>
                {open && <NavLinks />}
            </nav>

        </div>
    )
}



export default Navigation
