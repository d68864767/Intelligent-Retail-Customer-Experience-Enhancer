```python
# Import necessary libraries
from google.cloud import automl_v1beta1 as automl
from google.cloud.automl_v1beta1.proto import service_pb2

def get_prediction(content, project_id, model_id):
    """Predicts the product recommendation based on customer behavior."""
    prediction_client = automl.PredictionServiceClient()

    name = 'projects/{}/locations/us-central1/models/{}'.format(project_id, model_id)
    payload = {'text_snippet': {'content': content, 'mime_type': 'text/plain' }}
    params = {}
    request = prediction_client.predict(name, payload, params)
    return request  # waits till request is returned

def analyze_customer_behavior_for_recommendation(path):
    """Analyzes customer behavior and predicts product recommendation."""
    # Call the function from vision_api.py to analyze customer behavior
    behavior_analysis = analyze_customer_behavior(path)

    # Convert the behavior analysis into a format that can be used for prediction
    content = format_behavior_analysis(behavior_analysis)

    # Get the prediction
    prediction = get_prediction(content, 'your_project_id', 'your_model_id')

    # Print the recommended product
    print('Recommended product: {}'.format(prediction.payload[0].display_name))

def format_behavior_analysis(behavior_analysis):
    """Formats the behavior analysis into a string that can be used for prediction."""
    formatted_behavior = ''
    for face in behavior_analysis:
        formatted_behavior += 'anger: {}\n'.format(face['anger'])
        formatted_behavior += 'joy: {}\n'.format(face['joy'])
        formatted_behavior += 'surprise: {}\n'.format(face['surprise'])
    return formatted_behavior

# Test the function
analyze_customer_behavior_for_recommendation('path_to_your_image')
```

