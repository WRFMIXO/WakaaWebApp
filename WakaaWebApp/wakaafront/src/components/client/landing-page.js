import React from 'react';
import {Nav} from 'react-bootstrap';
import '../../assets/landing-page.css';

function Homepage() {
    return (
        <Nav className='mainnav'>
            <ul>
                <li><a href='#'>Home</a></li>
                <li><a href='#'>About</a></li>
                <li><a href='#'>Our Agencies</a></li>
                <li><a href='#'>Reservation</a></li>
            </ul>
        </Nav>
        
    );
}

export default Homepage;