//! Python bindings for CircuitParser using PyO3

use pyo3::prelude::*;
use pyo3::exceptions::PyRuntimeError;
use crate::CircuitParser;

#[pyclass]
pub struct PyCircuitParser {
    parser: CircuitParser,
}

#[pymethods]
impl PyCircuitParser {
    #[new]
    fn new(input_file_path: String, output_file_path: String) -> Self {
        PyCircuitParser {
            parser: CircuitParser::new(input_file_path, output_file_path),
        }
    }

    fn process(&mut self) -> PyResult<()> {
        self.parser.process()
            .map_err(|e| PyRuntimeError::new_err(format!("Processing error: {}", e)))
    }
}

#[pymodule]
fn circuit_parser_rust(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<PyCircuitParser>()?;
    Ok(())
}
