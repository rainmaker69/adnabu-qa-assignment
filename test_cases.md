# Test Case 1 – Product Search (Valid Product)

**Objective:**  
Verify user can search for an existing product.

**Steps:**
1. Open store homepage  
2. Enter “t-shirt” in search bar  
3. Click **Search**

**Expected Result:**  
Relevant products containing *t-shirt* appear in results.

---

# Test Case 2 – Product Search (Non‑existent Product)

**Objective:**  
Verify system behavior for invalid product.

**Steps:**
1. Enter `asdkjhaskjdh` in search  
2. Click **Search**

**Expected Result:**  
Message shown: _No products found_

---

# Test Case 3 – Product Search (Partial Match)

**Objective:**  
Verify partial keyword search.

**Steps:**
1. Enter “shirt”  
2. Click **Search**

**Expected Result:**  
Products containing keyword *shirt* appear.

---

# Test Case 4 – Add Product to Cart (Valid)

**Objective:**  
Verify user can add product to cart.

**Steps:**
1. Open product page  
2. Click **Add to Cart**

**Expected Result:**
- Product appears in cart  
- Cart count increases by 1

---

# Test Case 5 – Add Multiple Quantity

**Objective:**  
Verify cart updates quantity.

**Steps:**
1. Add the same product twice

**Expected Result:**  
Cart shows quantity **2**

---

# Test Case 6 – Edge Case (Add Out‑of‑Stock Product)

**Objective:**  
Verify system prevents adding unavailable items.

**Steps:**
1. Open out‑of‑stock product  
2. Attempt to add to cart

**Expected Result:**  
* Add to Cart disabled **or**  
* Error message displayed
