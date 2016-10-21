import React from 'react'
import ReactDOM from 'react-dom'
import { Checkbox, FormGroup } from 'react-bootstrap'
import InlineEdit from 'react-edit-inline';


var Hello = React.createClass ({
    render: function() {
        return (
            <h1>
            Hi, React!
            </h1>
        )
    }
})

var CheckboxBox = React.createClass ({
    render: function() {
        return (
        	 <form>
        	<FormGroup>
            <Checkbox></Checkbox>
            </FormGroup>
             </form>
        )
    }
});



//demo code for react inplaceedit

class MyParentComponent extends React.Component {
 
    constructor(props){
      super(props);
      this.dataChanged = this.dataChanged.bind(this);
      this.state = {
        message: 'ReactInline demo'
      }
    }
 
    dataChanged(data) {
        // data = { description: "New validated text comes here" } 
        // Update your model from here 
        console.log(data)
        this.setState({data})
    }
 
    customValidateText(text) {
      return (text.length > 0 && text.length < 64);
    }
 
    render() {
        return (<div>
            <h2>{this.state.message}</h2>
            <span>Edit me: </span>
            <InlineEdit
              validate={this.customValidateText}
              activeClassName="editing"
              text={this.state.message}
              paramName="message"
              change={this.dataChanged}
              style={{
                backgroundColor: 'yellow',
                minWidth: 150,
                display: 'inline-block',
                margin: 0,
                padding: 0,
                fontSize: 15,
                outline: 0,
                border: 0
              }}
            />
        </div>)
    }
}







