import React from 'react'
import ReactDOM from 'react-dom'


class Lists extends React.Component {

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
        if (this.state.data) {
            var listNodes = this.state.data.map((list, i) => {
            var listurl = '/gear/list_detail/'
            var deleteurl = '/gear/delete/'
            return (
                <div key={i} className="inner-box">
                    <h3>{list.title}</h3>
                    <a type="button" className="btn btn-primary" href={listurl + list.id}>
                            <i className="glyphicon glyphicon-eye-open"></i>
                        </a>
                    <a type="button" className="btn btn-danger" href={deleteurl + list.id}>
                        <i className="glyphicon glyphicon-trash"></i>
                    </a>

                </div>
            )
            })
        
        return (
            <div>
                <ul>
                    {listNodes}
                </ul>
            </div>
        )
      }
    }
}


ReactDOM.render(<Lists url='/api/v1/lists' pollInterval={15000} />, 
    document.getElementById('container'))
