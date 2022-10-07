import React from 'react';
import { BrowserRouter,Routes,Route } from 'react-router-dom';
import ArtistDetails from './ArtistDetails';
import FormComponent from './FormComponent';
import Home from './Home';

const Routing=()=>{
    return(
        <div>
            <BrowserRouter>
            <Routes>
                <Route path="/" element={<Home />}></Route>
                <Route path="/artist/:id" element={<ArtistDetails />}></Route>
                <Route path="/forms" element={<FormComponent />}></Route>
            </Routes>
            </BrowserRouter>
        </div>
    )
}
export default Routing;