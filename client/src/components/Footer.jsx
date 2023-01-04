import React from 'react';
import '../css/Footer.css';
import {BsHeartFill, BsFillTelephoneFill} from 'react-icons/bs';
import { SlSocialInstagram, SlSocialFacebook, SlSocialTwitter } from 'react-icons/sl';
import {MdEmail, MdLocationPin} from 'react-icons/md';

const Footer = () => {
    return (
        <footer className='footer'>
            <div className="footer_container">
                <div className="footer_container_top">
                    <div className="footer_about">
                        <div className="footer_about_info">
                            <h1>About Us</h1>
                            <div className='footer_about_info_p'>
                                <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Praesentium sapiente neque totam veritatis, assumenda a libero cupiditate suscipit inventore ab?</p>
                            </div>
                        </div>
                        <div className="social_apps">
                            <div className='social_apps_circle'>
                                <SlSocialInstagram className="social_apps_icon" onClick={() => window.open("https://stackoverflow.com/questions/13071967/adding-an-onclick-function-to-go-to-url-in-javascript")} />
                            </div>
                            <div className='social_apps_circle'>
                                <SlSocialFacebook className="social_apps_icon" onClick={() => window.open("https://stackoverflow.com/questions/13071967/adding-an-onclick-function-to-go-to-url-in-javascript")} />
                            </div>
                            <div className='social_apps_circle'>
                                <SlSocialTwitter className="social_apps_icon" onClick={() => window.open("https://stackoverflow.com/questions/13071967/adding-an-onclick-function-to-go-to-url-in-javascript")} />
                            </div>
                        </div>
                    </div>
                    <div className="footer_services">
                        <h1>Services</h1>
                        <div className="footer_services_links">
                            <a href="#">Cooked</a>
                            <a href="#">Deliver</a>
                            <a href="#">Quality Foods</a>
                            <a href="#">Mixed</a>
                        </div>
                    </div>
                    <div className="footer_question">
                        <h1>Have a questions?</h1>
                        <div className="footer_questions_info">
                            <div className="footer_question_info_box">
                                <div className="footer_questions_icon">
                                    <MdLocationPin className ='content_logo' size='20px' color='#fffa' />
                                </div>
                                <div className="footer_question_p">
                                    <p>	203 Fake St. Mountain View, San Francisco, California, USA</p>
                                </div>
                            </div>
                            <div className="footer_question_info_box">
                                <div className="footer_questions_icon">
                                    <BsFillTelephoneFill className ='content_logo' size='20px' color='#fffa' />
                                </div>
                                <div className="footer_question_p"><a href="tel:8987116415">8 987 116-94-15</a></div>
                            </div>
                            <div className="footer_question_info_box">
                                <div className="footer_question_icon">
                                    <MdEmail className ='content_logo' size='20px' color='#fffa' />
                                </div>
                                <div className="footer_question_p"><p>ranil2086@bk.ru</p></div>
                            </div>
                        </div>
                    </div>
                </div>
                <div className="footer_container_bottom">
                    <p>Copyright ©2023 All rights reserved | This template is made with LOVE by AJAX</p>
                </div>
            </div>
        </footer>
    )
}

export default Footer