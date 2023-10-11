#Write a function called linear_search_product that takes the list of products and a target product name as input. The function should perform a linear search to find the target product in the list and return a list of indices of all occurrences of the product if found, or an empty list if the product is not found

def linear_search_product(product_list, target_product):
    indices = []
    
    for index, product in enumerate(product_list):
        if product == target_product:
            indices.append(index)
    
    return indices

# Example list of products
products = ["apple", "banana", "orange", "apple", "grape"]

# Target product to search for
target_product = "apple"

# Perform linear search
result = linear_search_product(products, target_product)

if result:
    print(f"The product '{target_product}' was found at indices: {result}")
else:
    print(f"The product '{target_product}' was not found in the list.")