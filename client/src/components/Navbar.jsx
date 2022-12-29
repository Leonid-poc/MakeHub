import React from 'react';
import '../css/Navbar.css';
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav className='main_nav'>
        <div className="icon">
            <h1 style={{color: "white"}}>ЧЛЕН</h1>
        </div>
        <div className="menu">
            <Link className='link' to='/' >Home</Link>
            <Link className='link' to='/menu' >Menu</Link>
            <Link className='link' to="/service">Service</Link>
            <Link className='link' to="/blog">Blog</Link>
            <Link className='link' to="/about">About</Link>
            <Link className='link' to="/contact">Contact</Link>
        </div>
        <div className="menu2" style={{display: "none"}}>MENU</div>
    </nav>
  )
}

export default Navbar