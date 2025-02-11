"""
Veeqo Kit Creation Example
-------------------------

This script demonstrates how to create a kit product in Veeqo using their API.
A kit is a product that consists of multiple components (other products).

Requirements:
- Python 3.x
- A valid Veeqo API key

Example Usage:
    python create_simple_kit.py

The script will create a kit with the following structure:
- Main product (product_variant_id): The kit itself
- Contents: List of components that make up the kit
  - Each component has its own product_variant_id and quantity
"""

import json
import urllib.request

def create_kit():
    # API configuration
    url = 'https://api.veeqo.com/kits'
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': 'YOUR_API_KEY_HERE'  # Replace with your API key
    }

    # Kit data
    data = {
        'product_variant_id': '310358061',  # The main kit product ID
        'contents': [
            {
                'product_variant_id': 310384020,  # Component product ID
                'quantity': 1  # Number of this component in the kit
            }
        ]
    }

    try:
        # Create request
        request = urllib.request.Request(
            url,
            data=json.dumps(data).encode('utf-8'),
            headers=headers,
            method='POST'
        )

        # Send request and get response
        with urllib.request.urlopen(request) as response:
            response_data = json.loads(response.read().decode('utf-8'))
            print('Kit created successfully!')
            print('Response:', json.dumps(response_data, indent=2))
            return response_data

    except urllib.error.HTTPError as e:
        print(f'Error creating kit: {e.read().decode("utf-8")}')
    except Exception as e:
        print(f'Unexpected error: {str(e)}')

if __name__ == '__main__':
    create_kit()
