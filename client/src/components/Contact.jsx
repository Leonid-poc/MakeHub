import React from 'react';
import '../css/Contact.css';
import SimpleMap from './items/map';
import Fade from 'react-reveal/Fade';

const Contact = () => {
  return (
    <section className='contact'>
      <div className="map_section">
        <SimpleMap />
      </div>
      <div className="contact_section">
        <Fade bottom>
          <div className="contact_h1">
            <h1>Contact Us</h1>
          </div>    
        </Fade>
        <div className="contact_form">
          <Fade bottom><input type="text" placeholder='First Name'/></Fade>
          <Fade bottom><input type="text" placeholder='Second Name'/></Fade>
          <Fade bottom><input type="tel" placeholder='Phone Number'/></Fade>
          <Fade bottom><input type="text" placeholder='Message'/></Fade>
        </div> 
        <div className='contact_button'>
          <a href="#">Send</a>
        </div>
      </div>
    </section>
  )
}

export default Contact