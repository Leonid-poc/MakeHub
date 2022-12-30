import React from 'react';
import '../css/Main.css';

const Main = () => {
  return (
    <div className='main'>
        <div className="main cover">
          <div className="main_content">
            <h2>Welcome</h2>
            <h1>We cooked your desired pizza recipe</h1>
            <span>Lorem ipsum dolor sit amet consectetur adipisicing elit. Mollitia, illo.</span>
            <div className="main_content buttons">
              <div className="order_now">
                <a href="#1">Order Now</a>
              </div>
              <div className="view_menu">
                <a href="#2">View Menu</a>
              </div>
            </div>
          </div>
        </div>
    </div>

    // <div className='main'>
    // <div className="main cover">
    //   <div className="main_content">
    //     <h2>Welcome</h2>
    //     <h1>We cooked your desired pizza recipe</h1>
    //     <span>Lorem ipsum dolor sit amet consectetur adipisicing elit. Mollitia, illo.</span>
    //     <div className="main_content buttons">
    //       <div className="order_now">
    //         <a href="#1">Order Now</a>
    //       </div>
    //       <div className="view_menu">
    //         <a href="#2">View Menu</a>
    //       </div>
    //     </div>
    //   </div>
    // </div>
    // </div>
  )
}

export default Main