import React from "react";
import Col from "react-bootstrap/Col";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Histogram from "./Histogram";
import Legend from "./Legend";
import Loading from "./Loading";
import WorldMap from "./WorldMap";
import loadInitialMapItems from "../tasks/LoadInitialMapItemsTask";

export default class MainGrid extends React.Component {
  constructor(props) {
    super(props);

    // Initialize state first
    this.state = {
      countries: [],
      selectedCountry: null,
      currentTotalCases: null,
      sizeMapComponent: "90vh",
    };

    // Bind the `handleCountryChange` function to allow it to be used by other objects
    this.handleCountryChange = this.handleCountryChange.bind(this);
  }

  // This runs when the component is first loaded
  async componentDidMount() {
    try {
      const initialMapItems = await loadInitialMapItems();
      this.setState({ countries: initialMapItems });
    } catch (error) {
      console.log(error);
    }
  }

  // Update the state for a new country
  handleCountryChange(iso_code, currentTotalCases) {
    console.log(`Selected country is ${iso_code}`);

    if (iso_code === this.state.selectedCountry) {
      this.setState({ selectedCountry: null });
      this.setState({ currentTotalCases: null });
      this.setState({ sizeMapComponent: "90vh" });
    } else {
      this.setState({ selectedCountry: iso_code });
      this.setState({ currentTotalCases: currentTotalCases });
      this.setState({ sizeMapComponent: "65vh" });
    }
  }

  // This is evaluated whenever the component is rendered
  render() {
    return (
      <div>
        {this.state.countries.length === 0 ? (
          <Loading />
        ) : (
          <Container fluid>
            <Row style={{ height: this.state.sizeMapComponent }}>
              <Col xs={10} style={{ padding: "0px" }}>
                <WorldMap
                  countries={this.state.countries}
                  onCountrySelect={this.handleCountryChange}
                />
              </Col>
              <Col style={{ padding: "0px" }}>
                <Legend />
              </Col>
            </Row>
            <Row style={{ height: 1 - this.state.sizeMapComponent }}>
              <Col>
                <Histogram
                  selectedCountry={this.state.selectedCountry}
                  currentTotalCases={this.state.currentTotalCases}
                />
              </Col>
            </Row>
          </Container>
        )}
      </div>
    );
  }
}
