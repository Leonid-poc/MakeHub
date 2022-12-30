import React from 'react';
import classes from './Navbar.module.css';
import './Navbar.css';
import MobileNavigation from './MobileNavigation';
import Navigation from './Navigation';


const Navbar = () => {
  return (
    <nav className='main_nav'>
        <div className="icon">
            <h1 style={{color: "white"}}>ЧЛЕН</h1>
        </div>
        <div className={classes.NavBar}>
          <MobileNavigation />
          <Navigation />
        </div>
        {/* <div className="menu2" style={{display: "none"}}>MENU</div> */}
    </nav>
  )
}

export default Navbar