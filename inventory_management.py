```python
# Import necessary libraries
from google.cloud import bigquery
from google.cloud import aiplatform

def get_sales_data(project_id, dataset_id, table_id):
    """Fetches sales data from BigQuery."""
    client = bigquery.Client(project=project_id)
    table_ref = client.dataset(dataset_id).table(table_id)
    table = client.get_table(table_ref)

    # Fetch all rows from the table
    rows = client.list_rows(table)
    sales_data = [dict(row) for row in rows]

    return sales_data

def analyze_inventory(sales_data, project_id, model_id):
    """Analyzes sales data and predicts optimal inventory levels."""
    # Convert the sales data into a format that can be used for prediction
    instances = format_sales_data(sales_data)

    # Get the prediction
    prediction = aiplatform.gapic_v1beta1.PredictionServiceClient().predict(project_id, model_id, instances)

    # Print the optimal inventory levels
    for result in prediction.payload:
        print('Product: {}, Optimal Inventory Level: {}'.format(result.display_name, result.value))

def format_sales_data(sales_data):
    """Formats the sales data into a list of dictionaries that can be used for prediction."""
    instances = []
    for row in sales_data:
        instance = {}
        instance['product_id'] = row['product_id']
        instance['sales'] = row['sales']
        instance['inventory'] = row['inventory']
        instances.append(instance)
    return instances

# Test the function
sales_data = get_sales_data('your_project_id', 'your_dataset_id', 'your_table_id')
analyze_inventory(sales_data, 'your_project_id', 'your_model_id')
```

