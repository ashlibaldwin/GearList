var React = require('react')
var ReactDOM = require('react-dom')

var ListsList = React.createClass({
    loadListsFromServer: function(){
        $.ajax({
            url: this.props.url,
            datatype: 'json',
            cache: false,
            success: function(data) {
                this.setState({data: data});
            }.bind(this)
        })
    },

    getInitialState: function() {
        return {data: []};
    },

    componentDidMount: function() {
        this.loadListsFromServer();
        setInterval(this.loadListsFromServer, 
                    this.props.pollInterval)
    }, 
    render: function() {
        if (this.state.data) {
            //console.log('DATA!')
            var listNodes = this.state.data.map(function(list){
                var listurl = '/gear/list_detail/' 
                var deleteurl = '/gear/delete_list/'
                return (
                    <div className="inner-box">
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
        }
        return (
            <div>
                <ul>
                    {listNodes}
                </ul>
            </div>
        )
    }
})

ReactDOM.render(<ListsList url='/api/v1/lists' pollInterval={1000} />, 
    document.getElementById('container'))