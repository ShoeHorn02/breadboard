import React from 'react';
import Card from '@material-ui/core/Card';
import Container from '@material-ui/core/Container';
import axios from "axios";
import 'react-bootstrap-table-next/dist/react-bootstrap-table2.min.css';
import 'react-bootstrap-table2-toolkit/dist/react-bootstrap-table2-toolkit.min.css';
import 'react-bootstrap-table2-paginator/dist/react-bootstrap-table2-paginator.min.css';
import {
  CardTitle,
	CardText,
	Form,
	Button,
} from "reactstrap";
import ReactJson from 'react-json-view'

const API_DESTINATIONS = 'http://localhost:8000/api/boardpost';

class Main extends React.Component {

	constructor(props) {
    super(props);
    this.state = {
			inputjson:  {
        "type": "resistor",
        "description": "abc",
        "tolerance" : 4,
        "stability": 6,
        "reliability": 8,
        "voltage_coefficient": 9,
        "noise": 10,
        "temperature_rating" : 9,
        "thermal_resistance": 7,
        "temperature_coefficient_of_resistance": 9
      },
			postresult: null
    };
  }

	postBoard = async (body) => {
	  await axios.post(`${API_DESTINATIONS}`,body,)
	  .then(res => {
				console.log(res.data)
				this.setState({postresult: 'SUCCESS!'})
	    })
	  .catch(error => {
				console.log(error.response.data)
				this.setState({postresult: 'ERROR! '  + error.response.data})
	    })
	};

	onChange = async (x) =>  {
		await console.log(x)
		await this.setState({inputjson: x})
	}

	onSubmit = (e) => {
	e.preventDefault();
	console.log(this.state.inputjson)
	this.postBoard(this.state.inputjson)
}

  render() {
    return (
			<React.Fragment>
				<Container maxWidth="md" component="main">
					<h1>Edit Your JSON</h1>
					 <Form onSubmit={this.onSubmit}>
					 <ReactJson
						 src={this.state.inputjson}
						 onAdd={(add)=>{this.setState({inputjson: add.updated_src})}}
						 onEdit={(edit)=>{this.setState({inputjson: edit.updated_src})}}
             onDelete={(destroy)=>{this.setState({inputjson: destroy.updated_src})}}
						 />

						 <Card body>
					     <CardTitle tag="h5">
					       Preview
					     </CardTitle>
					     <CardText>
								 { JSON.stringify(this.state.inputjson) }
					     </CardText>
					     <Button className="mt-1 mb-2">
					       Post Json
					     </Button>
					   </Card>

					   </Form>

					  <CardText>
							{this.state.postresult}
						</CardText>
				</Container>
			</React.Fragment>
    );
  }
}

export default Main
