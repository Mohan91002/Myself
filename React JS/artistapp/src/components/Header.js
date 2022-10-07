import React from 'react';
import {Link} from 'react-router-dom';
import FormsComponent from './FormComponent';
const Header=()=>{
    return(
        <header>
            <Link to="/">Home</Link>
        <Link to ="/forms">forms</Link>
        </header>
    )
}
export default Header;