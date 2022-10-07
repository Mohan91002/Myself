import React,{Component} from 'react';
import axios from 'axios';
import Header from './Header';
import Albums from './Albums';
const url="http://localhost:8900/artists";
class ArtistDetails extends Component{
    constructor(props)
    {
        super(props);
        this.state={
            details:''
        }
    }
    componentDidMount()
    {
        axios.get('${url}/${this.props.match.params.id}')
        .then((response)=>{
            this.setState({details:response.data})
        })
    }
    render()
    {
        const mydata=this.state.details;
        return(
            <div>
  <Header />
  <div className="artist_bio">
      <div className="artist_image">
          <h3> {mydata.name}</h3>
          <div className="bio_text">
              {mydata.bio}
          </div>
          <Albums albumd={mydata.albums}></Albums>
      </div>
  </div>
            </div>
          
        )
    }
}

export default ArtistDetails;