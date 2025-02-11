# Veeqo Kit/Bundle Creation Example

This repository contains an example of how to create kit/bundle products using the Veeqo API. A kit/bundle is a product that consists of multiple component products.

## Simple Kit/Bundle Creation (`create_simple_kit.py`)

This script demonstrates the basic usage of the Veeqo API to create a kit/bundle product. It's a straightforward implementation that creates a single kit/bundle with one component.

### Prerequisites

- Python 3.x
- A Veeqo API key

### Configuration

Before running the script, replace `YOUR_API_KEY_HERE` with your actual Veeqo API key:

```python
headers = {
    'Content-Type': 'application/json',
    'x-api-key': 'YOUR_API_KEY_HERE'  # Replace this with your API key
}
```

### Kit Structure

The script creates a kit with the following structure:
```json
{
    "product_variant_id": "310358061",  // The main kit product
    "contents": [
        {
            "product_variant_id": 310384020,  // Component product
            "quantity": 1  // Quantity of this component
        }
    ]
}
```

### Running the Script

```bash
python create_simple_kit.py
```

### Response

Upon successful creation, the script will print the API response, which includes details about the created kit.

## Bulk Kit Creation (`create_kit.py`)

For bulk creation of kits, see `create_kit.py` which can process multiple kits from a CSV file.

## Error Handling

The scripts include error handling for:
- HTTP errors (e.g., invalid API key, server errors)
- JSON parsing errors
- Network-related errors

## API Documentation

For more information about the Veeqo API, visit their official documentation.
