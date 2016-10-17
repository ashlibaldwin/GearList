import React from 'react'
import ReactDOM from 'react-dom'
import { Checkbox, FormGroup } from 'react-bootstrap'


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
})



ReactDOM.render(<CheckboxBox />, document.getElementById('checkbox'));



ReactDOM.render(<Hello />, document.getElementById('container'))
