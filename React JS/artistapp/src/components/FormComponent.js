import React,{Component} from 'react';
import Header from './Header';
const url="http://localhost:8900/artists";
class FormComponent extends Component{
    constructor()
    {
        super();
        this.state={
            name:'',
            cover:'',
            bio:''
        }
    
    this.handleChangeName=this.handleChangeName.bind(this);
    this.handleChangeCover=this.handleChangeCover.bind(this);
    this.handleChangeBio=this.handleChangeBio.bind(this);
    this.handleSubmit=this.handleSubmit.bind(this);
    }
    handleChangeName(event)
    {
        this.setState({name:event.target.value})
    }
    handleChangeCover(event)
    {
        this.setState({cover:event.target.value})
    }
    handleChangeBio(event)
    {
        this.setState({bio:event.target.value})
    }
    handleSubmit(){
  var random= Math.floor(Math.random()*1000)  
  var data={
      "id":random,
      "name":this.state.name,
      "cover":this.state.cover,
      "bio":this.state.bio,
      "albums": [
        {
          "albumId": "c1",
          "title": "Ain't No Grave",
          "year": 2010,
          "cover": "no_grave",
          "price": 20
        },
        {
          "albumId": "c2",
          "title": "Out Among the Stars",
          "year": 2014,
          "cover": "among_stars",
          "price": 25
        },
        {
          "albumId": "c3",
          "title": "Solitary Man",
          "year": 2000,
          "cover": "solitary_man",
          "price": 15
        },
        {
          "albumId": "c4",
          "title": "The Man Comes Around",
          "year": 2002,
          "cover": "man_comes_around",
          "price": 10
        }
      ],
      "genre": "pop"
  }   
  fetch(url,{
      method:'POST',
      headers:{
          'Accept':'application/json',
          'Content-Type':'application/json'
      },
      body:JSON.stringify(data)
  }) 
  .then((res)=>console.log("Data is posted"))
    }
    render(){
        return(
            <div>
            <Header />
            <div className="container">
            <div className="panel panel-primary">
                <div className="panel-heading">
                    <h3> Aritist Data</h3>
                </div>
                <div className="panel-body">
                    <div className="form-group">
                        <label>Name</label>
                        <input type="text" className="forms-control" id="name" value={this.state.name} onChange={this.handleChangeName} />
                    </div>
                    <div className="form-group">
                        <label>Cover</label>
                        <input type="text" className="forms-control" id="cover" value={this.state.cover} onChange={this.handleChangeCover} />
                    </div> 
                        <label>Bio</label>
                        <input type="text" className="forms-control" id="bio" value={this.state.bio} onChange={this.handleChangeBio} />
                    </div>
                </div>
                <button className="btn btn-success" onClick={this.handleSubmit}>
                Submit
                </button>
            </div>
            </div>
            
            
        )
    }

}

export default FormComponent;