import React from 'react';
import '../css/Service.css';
import logo1 from '../assets/logo/food.jpeg';
import logo2 from '../assets/logo/deliver.jpeg';
import logo3 from '../assets/logo/pizza.jpeg';

const Service = () => {
    const info = [
        [logo1, "HEALTHY FOODS", "Lorem ipsum dolor sit amet consectetur adipisicing elit. Non illo dolor aperiam quisquam tempore iure."],
        [logo2, "FASTED DELIVERY", "Lorem ipsum dolor sit amet consectetur adipisicing elit. Non illo dolor aperiam quisquam tempore iure."],
        [logo3, "ORIGINAL RECIPES", "Lorem ipsum dolor sit amet consectetur adipisicing elit. Non illo dolor aperiam quisquam tempore iure."]]
    
    return (
    <section className='service'>
        <div className="service_content">
            <div className="service_content_top">
                <h1>Our Service</h1>
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque aperiam unde mollitia, non facere ab? Perferendis quam unde cupiditate quidem.</p>
            </div>
            <div className="service_content_bottom">
               {info.forEach((data) => {
                     <div className="service_content_container">
                     <div className="service_container_top">
                         <div className="image">
                             <img className="img" src={data[0]}></img>
                         </div>
                     </div>
                     <div className="service_container_bottom">
                         <h1>data[1]</h1>
                         <p>data[2]</p>
                     </div>
                 </div>
               })}
                <div className="service_content_container">
                    <div className="service_container_top">
                        <div className="image">
                            <div className="img"></div>
                        </div>
                    </div>
                    <div className="service_container_bottom">
                        <h1>HEALTHY FOOD</h1>
                        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Non illo dolor aperiam quisquam tempore iure.</p>
                    </div>
                </div>
            </div>        
        </div>
    </section>
  )
}

export default Service