Test Case 1 — Product Search (Valid Product)

Objective: Verify user can search for an existing product.

Steps

Open store homepage

Enter "t-shirt" in search bar

Click search

Expected Result

Relevant products containing t-shirt appear in results.

Test Case 2 — Product Search (Non-existent Product)

Objective: Verify system behavior for invalid product.

Steps

Enter "asdkjhaskjdh" in search

Click search

Expected Result

Message shown: No products found

Test Case 3 — Product Search (Partial Match)

Objective: Verify partial keyword search.

Steps

Enter "shirt"

Search

Expected Result

Products containing keyword shirt appear.

Test Case 4 — Add Product to Cart (Valid)

Objective: Verify user can add product to cart.

Steps

Open product page

Click Add to Cart

Expected Result

Product appears in cart

Cart count increases by 1

Test Case 5 — Add Multiple Quantity

Objective: Verify cart updates quantity.

Steps

Add same product twice

Expected Result

Cart shows quantity 2

Test Case 6 — Edge Case (Add Out-of-Stock Product)

Objective: Verify system prevents adding unavailable items.

Steps

Open out-of-stock product

Attempt add to cart

Expected Result

Add to Cart disabled OR error message displayed.
