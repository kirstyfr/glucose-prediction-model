from .load_data import import_json
from .preprocessing_data import calculate_moving_avg_and_count
from .preprocessing_data import filter_by_threshold_second_limit
from .linreg_model import *
from .visualisation import chart_actual_v_predicted
from .export_data import export_metrics

class CurrentGlucoseModel:
    def __init__(self):
        self.data = None
        self.data = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.regressor = None
        self.evaluation_metrics = None
        self.preprocess_params = {}  
        self.split_params = {}       
        self.model_params = {}       

    def import_json(self, file_path):
        """Load JSON file and convert to dataframe."""
        try:
            self.data = import_json(file_path)
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except ValueError as e:
            print(f"Error loading JSON: {e}")
    
    def preprocess_data(self, window, threshold, seconds_after):
        """Add in moving average and count of seconds columns since glucose was added. Filter to stable portions of data. """
        self.data = calculate_moving_avg_and_count(self.data, window)
        self.data = filter_by_threshold_second_limit(self.data, threshold, seconds_after)

        self.preprocess_params = {
            'window_size': window,
            'threshold': threshold,
            'seconds_after': seconds_after
        }


    def split_data(self, test_size, random_state):
        """Split data into training/testing sets."""
        self.X_train, self.X_test, self.y_train, self.y_test = split_data(self.data, test_size, random_state)
        # Store split parameters
        self.split_params = {
            'test_size': test_size,
            'random_state': random_state
        }

    def train_model(self):
        "Train linear regression model."
        self.regressor = train_model(self.X_train, self.y_train)

    def train_model(self, model=None):
        """Train a linear regression model or the specified model."""
        self.regressor = train_model(self.X_train, self.y_train, model)

    def evaluate_model(self):
        "Apply evaluation metrics and print their values."
        self.evaluation_metrics = evaluate_model(self.regressor, self.X_test, self.y_test)
        return self.evaluation_metrics
    
    def export_metrics(self, file_path="/data/model_performance_parameters.json"):
        """Export evaluation metrics and parameters (preprocessing, splitting, and model) to a JSON file."""
        if self.evaluation_metrics is None:
            raise ValueError("No evaluation metrics found.")
        
        # Combine preprocessing, split, and model parameters
        params = {
            'preprocessing': self.preprocess_params,
            'split': self.split_params,
            'model': self.model_params
        }

        # Use the export_metrics function from the export_data module
        export_metrics(self.evaluation_metrics, params, file_path)

    def chart_actual_v_predicted(self):
        """Visualise the actual vs. predicted values."""
        chart_actual_v_predicted(self.regressor, self.X_test, self.y_test)
    
    def get_data(self):
        return self.data