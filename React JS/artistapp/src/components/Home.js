
import React, { Component } from 'react';

const url = "http://localhost:8900/artists";
import Banner from './Banner';
import ArtistList from './ArtistList';
class Home extends Component {
    constructor() {
        super();
        this.state = {
            artists: ''
        }
    }
    componentDidMount() {
        fetch(url,
            {
                method: 'GET'
            }).then((response) => response.json())
            .then((data) => {
                this.setState({ artists: data })
            })
    }
    render() {
        console.log(this.state.artists)
        return (
            <div>
                <Banner />

                <ArtistList artistData={this.state.artists} />
            </div>


        )
    }

}
export default Home;