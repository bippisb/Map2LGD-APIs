from flask import Flask, Blueprint, request, jsonify
import pandas as pd
import io
import sqlite3

# Create a Flask application
app = Flask(__name__)

# Create a Blueprint
api = Blueprint('api', __name__)

# Define a route for the API endpoint
@api.route('/process_json', methods=['POST'])
def process_json_route():
    """
    Process a JSON request and return a subset of the data.

    This function is a route handler for the '/process_json' endpoint. It accepts a JSON
    payload via a POST request, processes the data, and returns a JSON response.

    Parameters:
        None

    Returns:
        If the JSON data contains any of the specified columns, a JSON response will be
        returned containing only those columns. Otherwise, a 500 error response will be
        returned with an error message.

    Raises:
        ValueError: If none of the specified columns are present in the JSON data.

    Note:
        This function uses the Flask request object to extract the JSON data from the
        request payload. It then uses the pandas library to create a DataFrame from the
        JSON data. The specified columns are extracted from the DataFrame and returned as
        a JSON response.
    """
    try:
        json_data = request.get_json()

        if json_data:
            df = pd.DataFrame(json_data)

            specified_columns = ["state_name", "district_name", "sub_district_name", "block_name", "gp_name", "village_name"]
            present_columns = list(set(specified_columns).intersection(df.columns))

            if not present_columns:
                raise ValueError("None of the specified columns are present in the JSON data.")

            df = df[present_columns]

            return df.to_json()

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/state_mappings', methods=['GET'])
def get_state_mappings_api():
    """
    Retrieves the state mappings from the 'states' table in the 'lgd_database.db' SQLite database.
    Returns a JSON object containing the mapping of state names and their respective codes.

    Parameters:
    None

    Returns:
    jsonify(mapping_dict): A JSON object containing the mapping of state names and their respective codes.
                           The keys of the JSON object are the lowercase state names and variants,
                           and the values are the corresponding state codes.

    Raises:
    Exception: If there is an error while retrieving the state mappings from the database.
    
    HTTP Status Code 500: If there is an error while retrieving the state mappings from the database.
    """
    try:
        with sqlite3.connect('lgd_database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT entityName, entityLGDCode, entityNameVariants FROM states")
            data = cursor.fetchall()

        mapping_dict = {}
        for state_name, state_code, state_variants in data:
            mapping_dict[state_name.lower()] = state_code
            if state_variants:
                for variant in state_variants.split(','):
                    mapping_dict[variant.strip().lower()] = state_code

        return jsonify(mapping_dict)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/create_mapped_dataset', methods=['POST'])
def create_mapped_dataset_api():
    """
    Create a mapped dataset based on the provided dataset and mapping.

    Parameters:
    -----------
    None

    Returns:
    --------
    dict: A JSON response containing the mapped dataset.

    Raises:
    -------
    ValueError: If either 'dataset' or 'mapping' is missing from the request JSON.

    Exception: If any other error occurs during the processing of the request.
    """
    try:
        request_data = request.get_json()

        dataset = request_data.get('dataset')
        mapping = request_data.get('mapping')

        if not dataset or not mapping:
            raise ValueError("Both 'dataset' and 'mapping' are required in the request JSON.")

        dataset['state_name'] = dataset['state_name'].str.strip()
        dataset['state_code'] = dataset['state_name'].str.lower().map(mapping)
        dataset.loc[dataset['state_code'].isnull(), 'state_code'] = -2

        return jsonify(dataset.to_dict(orient='records'))

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Register the Blueprint with the Flask application
app.register_blueprint(api)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
