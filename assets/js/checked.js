import React from 'react'
import ReactDOM from 'react-dom'


class Items extends React.Component {

  constructor(props) {
    super(props)
    this.state = { data: [] }
  }

  loadListsFromServer() {
      $.ajax({
          url: this.props.url,
          datatype: 'json',
          success: (data) => {
              this.setState({data: data});
          },
      error: (xhr, status, err) => {
        console.error(this.props.url, status, err.toString());
      }
    });
  }

  componentDidMount() {  
      this.loadListsFromServer();
      setInterval(this.loadListsFromServer.bind(this), this.props.pollInterval);
  }

    render() {
       console.log(this.state.data)
        if (this.state.data) {
            var itemNodes = this.state.data.map((item, i) => {
            var deleteurl = '/gear/delete/'
            return (
                <div key={i} className="inner-box">
                    <h3>{item.title}</h3>
                    <a type="button" className="btn btn-danger" href={deleteurl + item.id}>
                        <i className="glyphicon glyphicon-trash"></i>
                    </a>

                </div>
            )
            })
        
        return (
            <div>
                <ul>
                    {itemNodes}
                </ul>
            </div>
        )
      }
    }
}


ReactDOM.render(<Items url='/api/v1/items' pollInterval={15000} />, 
    document.getElementById('container'))

//add handle click event for is_completed
//access the parent list somehow
//I think these componenets should be connected somehow

 


