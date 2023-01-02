import React from 'react';
import '../css/Footer.css';
import {BsHeartFill} from 'react-icons/bs';

const Footer = () => {
  return (
    <footer className='footer'>
        <div className="footer_container">
            <div className="footer_container_top"></div>
            <div className="footer_container_bottom">
                <p>Copyright ©2023 All rights reserved | This template is made with <BsHeartFill size='20px' color='e1e1e1'/> by AJAX</p>
            </div>
        </div>
    </footer>
  )
}

export default Footer