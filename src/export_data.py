import json

def export_metrics(metrics, params, file_path='/results/model_performance_parameters.json'):

    data_to_export = {
        'parameters': params,            
        'evaluation_metrics': metrics   
    }

    try:
        with open(file_path, 'r') as f:
            existing_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # If the file does not exist or is empty, start with an empty list
        existing_data = []

    # Append the new data
    existing_data.append(data_to_export)
    
    # Write back the updated data
    with open(file_path, 'w') as f:
        json.dump(existing_data, f, indent=4)

    print(f"Metrics and parameters added to {file_path}")

    