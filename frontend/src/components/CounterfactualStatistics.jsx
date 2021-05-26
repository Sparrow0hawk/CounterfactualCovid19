import Card from "react-bootstrap/Card";
import exact from "prop-types-exact";
import PropTypes from "prop-types";

const propTypes = exact({
  totalCasesCounterfactual: PropTypes.number,
  totalCasesReal: PropTypes.number,
  shiftFirstRestrictions: PropTypes.instanceOf(Date).isRequired,
  shiftLockdown: PropTypes.instanceOf(Date).isRequired,
});

const defaultProps = {};

const CounterfactualStatistics = (props) => {
  return (
    <Card
      style={{
        marginTop: "1%",
        marginBottom: "1%",
      }}
      bg={"light"}
    >
      <Card.Body>
        <Card.Title>Counterfactual Statistics</Card.Title>
        {!props.totalCasesCounterfactual ? null : (
          <Card.Text>
            {`Total COVID-19 Cases per Million: ${props.totalCasesCounterfactual
              .toFixed(0)
              .toString()} \n `}
          </Card.Text>
        )}
        {!(props.totalCasesCounterfactual & props.totalCasesReal) ? null : (
          <Card.Text>
            {`Reduction in total cases: ${(
              (1 - props.totalCasesCounterfactual / props.totalCasesReal) *
              100
            )
              .toFixed(1)
              .toString()} %`}
          </Card.Text>
        )}
      </Card.Body>
    </Card>
  );
};

CounterfactualStatistics.propTypes = propTypes;
CounterfactualStatistics.defaultProps = defaultProps;

export default CounterfactualStatistics;
