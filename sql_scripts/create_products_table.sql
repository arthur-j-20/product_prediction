create table insurance.products.insur_products(
    product_id INT IDENTITY(1,1) PRIMARY KEY,
    cust_id INT,
    product_auto BIT,
    product_home BIT,
    product_life BIT,
    product_health BIT,
    FOREIGN KEY(cust_id) REFERENCES insurance.products.customers(CustomerID)
);