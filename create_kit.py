import csv
import json
from collections import defaultdict
import urllib.request
from time import sleep

# API configuration
API_KEY = 'API KEY'
API_URL = 'https://api.veeqo.com/kits'

headers = {
    'Content-Type': 'application/json',
    'x-api-key': API_KEY
}

def create_kit(product_variant_id, contents):
    """Create a kit using the Veeqo API"""
    data = {
        'product_variant_id': str(product_variant_id),
        'contents': contents
    }
    
    try:
        # Create request
        request = urllib.request.Request(
            API_URL,
            data=json.dumps(data).encode('utf-8'),
            headers=headers,
            method='POST'
        )
        
        # Send request and get response
        with urllib.request.urlopen(request) as response:
            response_data = json.loads(response.read().decode('utf-8'))
            print(f"Successfully created kit for product {product_variant_id}")
            return response_data
            
    except urllib.error.HTTPError as e:
        error_message = e.read().decode('utf-8')
        print(f"Error creating kit for product {product_variant_id}: {error_message}")
        return None
    except Exception as e:
        print(f"Unexpected error for product {product_variant_id}: {str(e)}")
        return None

def process_kits():
    # Dictionary to store components for each product
    product_components = defaultdict(list)
    
    # Read the CSV file
    print("Reading kits.csv file...")
    with open('kits.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            product_id = row['product_id']
            component = {
                'product_variant_id': int(row['component_id']),
                'quantity': int(row['quantity'])
            }
            product_components[product_id].append(component)
    
    # Create kits for each product
    total = len(product_components)
    print(f"Found {total} kits to create")
    
    for idx, (product_id, contents) in enumerate(product_components.items(), 1):
        print(f"\n=== Processing kit {idx}/{total} ===")
        print(f"Product ID: {product_id}")
        print(f"Components: {json.dumps(contents, indent=2)}")
        
        # Create the kit
        result = create_kit(product_id, contents)
        
        if result:
            print("Kit created successfully!")
        else:
            print("Failed to create kit")
        
        # Add a small delay to avoid rate limiting
        sleep(0.5)

if __name__ == '__main__':
    process_kits()
