import React from 'react'
import ReactDOM from 'react-dom'

var items = ['ashli', 'andrew', 'riley', 'carson']

var List = React.createClass ({

	//getInitialState() {},

    render: function() {
    	console.log(items)
        return (

		<div className="row text-center">
		<table>
		<tbody>
		{items.map((items, i) => (
			<tr key={i}>
					<td>
				   		<input type="checkbox" className="strikethrough"  />
				   		<span className="item">{items}</span>   		
				   	</td>

				   	<td>
						<a type="button" className="btn btn-danger pull-right" href="{% url 'gear:delete_item' item.id %}"><i className="glyphicon glyphicon-trash"></i></a>
					</td>
				</tr>
			))  
		}
		</tbody>
		</table>
		</div>

		        )
    }
})
 

const Checkbox = React.createClass ({
	
  getInitialState() {
    return { isChecked: false};
  },

  toggleChange() {
    this.setState({
      isChecked: !this.state.isChecked // flip boolean value
    }, function() {
      console.log(this.state);
    }.bind(this));
  },
  render: function() {
    return (
      <label>
        <input
          type="checkbox"
          checked={this.state.isChecked}
          onChange={this.toggleChange} />
        Check Me!
      </label>
    );
  }
});

