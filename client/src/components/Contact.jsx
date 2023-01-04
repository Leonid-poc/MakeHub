import React, {useState} from 'react';
import '../css/Contact.css';
import SimpleMap from './items/map';
import Fade from 'react-reveal/Fade';

const Contact = () => {
  const [input1, setInput1] = useState('');
  const [input2, setInput2] = useState('');
  const [input3, setInput3] = useState('');
  const [input4, setInput4] = useState('');

  return (
    <section className='contact'>
      <div className="map_section">
        <SimpleMap />
      </div>
      <div className="contact_section">
        <Fade top>
          <div className="contact_h1">
            <h1>Contact Us</h1>
          </div>    
        </Fade>
        <div className="contact_form">
          <Fade right><input type="text" placeholder='First Name' onChange={e => setInput1(e.target.value)} style={input1 != "" ? {borderBottom: '1px solid #fac564'} : null}/></Fade>
          <Fade right><input type="text" placeholder='Second Name' onChange={e => setInput2(e.target.value)} style={input2 != "" ? {borderBottom: '1px solid #fac564'} : null}/></Fade>
          <Fade right><input type="tel" placeholder='Phone Number' onChange={e => setInput3(e.target.value)} style={input3 != "" ? {borderBottom: '1px solid #fac564'} : null} /></Fade>
          <Fade right><input type="text" placeholder='Message' onChange={e => setInput4(e.target.value)} style={input4 != "" ? {borderBottom: '1px solid #fac564'} : null}/></Fade>
        </div> 
        <Fade bottom>
          <div className='contact_button'>
            <a href="#">Send</a>
          </div>
        </Fade>
      </div>
    </section>
  )
}

export default Contact