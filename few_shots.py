few_shots = [
    {
        'Question': "How many Adidas products are there in total across all categories?",
        'SQLQuery': "SELECT SUM(stock_quantity) FROM (SELECT stock_quantity FROM t_shirts WHERE brand = 'Adidas' UNION ALL SELECT stock_quantity FROM hats WHERE brand = 'Adidas' UNION ALL SELECT stock_quantity FROM shoes WHERE brand = 'Adidas' UNION ALL SELECT stock_quantity FROM accessories WHERE brand = 'Adidas') as total_adidas",
        'SQLResult': "Result of the SQL query",
        'Answer': "356"
    },
    {
        'Question': "What is the total value of black shoes in our inventory?",
        'SQLQuery': "SELECT SUM(price * stock_quantity) FROM shoes WHERE color = 'Black'",
        'SQLResult': "Result of the SQL query",
        'Answer': "15230"
    },
    {
        'Question': "If we apply discounts, how much revenue will we generate from all Puma hats?",
        'SQLQuery': """SELECT SUM(total_revenue) AS total_revenue_generated
                        FROM (
                            SELECT 
                                hats.hat_id, 
                                hats.price * hats.stock_quantity * COALESCE((100 - discounts.pct_discount)/100, 1) AS total_revenue
                            FROM hats
                            LEFT JOIN discounts 
                                ON hats.hat_id = discounts.merchandise_id 
                                AND discounts.merchandise_type = 'Hat'
                            WHERE hats.brand = 'Puma'
                        ) AS revenue_table;""",
        'SQLResult': "Result of the SQL query",
        'Answer': "4993.00"
    },
    {
        'Question': "How many Ray-Ban sunglasses do we have in stock?",
        'SQLQuery': "SELECT SUM(stock_quantity) FROM accessories WHERE type = 'Sunglasses' AND brand = 'Ray-Ban'",
        'SQLResult': "Result of the SQL query",
        'Answer': "41"
    },
    {
        'Question': "What is the total price of size 10 Nike shoes?",
        'SQLQuery': "SELECT SUM(stock_quantity * price) FROM shoes WHERE size = 10 AND brand = 'Nike'",
        'SQLResult': "Result of the SQL query",
        'Answer': "2420"
    },
    {
        'Question': "If we sell all Levi products at the current price, what would be the total revenue?",
        'SQLQuery': """SELECT SUM(total_revenue) AS total_revenue_generated
                        FROM (
                            SELECT SUM(price * stock_quantity) AS total_revenue
                            FROM t_shirts
                            WHERE brand = 'Levi'
                            UNION ALL
                            SELECT SUM(price * stock_quantity)
                            FROM hats
                            WHERE brand = 'Levi'
                            UNION ALL
                            SELECT SUM(price * stock_quantity)
                            FROM shoes
                            WHERE brand = 'Levi'
                            UNION ALL
                            SELECT SUM(price * stock_quantity)
                            FROM accessories
                            WHERE brand = 'Levi'
                        ) AS revenue_table;""",
        'SQLResult': "The total revenue generated from selling all Levi products at the current price.",
        'Answer': "58388"
    },

    {
        'Question': "What is the total revenue potential for all shoes, assuming they are sold at a discount?",
        'SQLQuery': """SELECT SUM(a.total_price * ((100 - COALESCE(d.pct_discount, 0)) / 100)) as total_revenue
                       FROM (SELECT shoe_id, SUM(price * stock_quantity) as total_price FROM shoes GROUP BY shoe_id) a
                       LEFT JOIN discounts d ON a.shoe_id = d.merchandise_id AND d.merchandise_type = 'Shoe'""",
        'SQLResult': "Result of the SQL query",
        'Answer': "60605.0"
    },
    {
        'Question': "Name all the unique brands in each category of our inventory.",
        'SQLQuery': """SELECT 'T-Shirt' AS Category, brand FROM t_shirts GROUP BY brand
                       UNION
                       SELECT 'Hat' AS Category, brand FROM hats GROUP BY brand
                       UNION
                       SELECT 'Shoe' AS Category, brand FROM shoes GROUP BY brand
                       UNION
                       SELECT 'Accessory' AS Category, brand FROM accessories GROUP BY brand""",
        'SQLResult': "'T-Shirt', 'Van Huesen'\n'T-Shirt', 'Levi'\n'T-Shirt', 'Nike'\n'T-Shirt', 'Adidas'\n'Hat', 'New Era'\n'Hat', 'Nike'\n'Hat', 'Adidas'\n'Hat', 'Puma'\n'Shoe', 'Nike'\n'Shoe', 'Adidas'\n'Shoe', 'Puma'\n'Shoe', 'Reebok'\n'Accessory', 'Ray-Ban'\n'Accessory', 'Fossil'\n'Accessory', 'Levi'\n'Accessory', 'Casio'",
        'Answer': "T-Shirts: Van Huesen, Levi, Nike, Adidas; Hats: New Era, Nike, Adidas, Puma; Shoes: Nike, Adidas, Puma, Reebok; Accessories: Ray-Ban, Fossil, Levi, Casio"
    },
    {
        'Question': "Find the average price of all items in each category (t-shirts, hats, shoes, accessories) that have at least 50 items in stock.",
        'SQLQuery': """SELECT 'T-Shirts' as category, AVG(price) as avg_price FROM t_shirts WHERE stock_quantity >= 50
                       UNION ALL
                       SELECT 'Hats', AVG(price) FROM hats WHERE stock_quantity >= 50
                       UNION ALL
                       SELECT 'Shoes', AVG(price) FROM shoes WHERE stock_quantity >= 50
                       UNION ALL
                       SELECT 'Accessories', AVG(price) FROM accessories WHERE stock_quantity >= 50""",
        'SQLResult': "Result of the SQL query",
        'Answer': "Average prices: T-Shirts - $30.45, Hats - $7, Shoes - $82, Accessories - $11"
    },
    {
        'Question': "Which brand has the highest total stock quantity across all categories?",
        'SQLQuery': """SELECT brand, SUM(stock) as total_stock FROM
                       (SELECT brand, SUM(stock_quantity) as stock FROM t_shirts GROUP BY brand
                        UNION ALL
                        SELECT brand, SUM(stock_quantity) FROM hats GROUP BY brand
                        UNION ALL
                        SELECT brand, SUM(stock_quantity) FROM shoes GROUP BY brand
                        UNION ALL
                        SELECT brand, SUM(stock_quantity) FROM accessories GROUP BY brand) as all_items
                       GROUP BY brand ORDER BY total_stock DESC LIMIT 1""",
        'SQLResult': "Result of the SQL query",
        'Answer': "Nike with 1518 items"
    },
    {
        'Question': "How many different brands of 'Medium' sized hats do we have?",
        'SQLQuery': "SELECT COUNT(DISTINCT brand) FROM hats WHERE size = 'Medium'",
        'SQLResult': "Result of the SQL query",
        'Answer': "4"
    },
    {
        'Question': "What is the total number of items in stock for each color across all merchandise categories?",
        'SQLQuery': """SELECT color, SUM(stock) as total_stock FROM
                       (SELECT color, SUM(stock_quantity) as stock FROM t_shirts GROUP BY color
                        UNION ALL
                        SELECT color, SUM(stock_quantity) FROM hats GROUP BY color
                        UNION ALL
                        SELECT color, SUM(stock_quantity) FROM shoes GROUP BY color
                        UNION ALL
                        SELECT color, SUM(stock_quantity) FROM accessories GROUP BY color) as all_colors
                       GROUP BY color""",
        'SQLResult': "Result of the SQL query",
        'Answer': "Black: 1252, Blue: 1555, Red: 1693, White: 1733, Brown=439"
    },
   
    {
        'Question': "What are the top 5 items from each category based on stock quantity?",
        'SQLQuery': """SELECT category, brand, stock_quantity, rank_item
                       FROM (
                           SELECT category, brand, stock_quantity,
                                  RANK() OVER (PARTITION BY category ORDER BY stock_quantity DESC) as rank_item
                           FROM (
                               SELECT 'T-Shirt' as category, brand, stock_quantity FROM t_shirts
                               UNION ALL
                               SELECT 'Hat' as category, brand, stock_quantity FROM hats
                               UNION ALL
                               SELECT 'Shoe' as category, brand, stock_quantity FROM shoes
                               UNION ALL
                               SELECT 'Accessory' as category, brand, stock_quantity FROM accessories
                           ) as all_products
                       ) as ranked_products
                       WHERE rank_item <= 5;""",
        'SQLResult': "'Accessory', 'Fossil', '50', '1'\n'Accessory', 'Ray-Ban', '49', '2'\n'Accessory', 'Fossil', '48', '3'\n'Accessory', 'Levi', '46', '4'\n'Accessory', 'Levi', '45', '5'\n'Hat', 'New Era', '50', '1'\n'Hat', 'Adidas', '49', '2'\n'Hat', 'Puma', '49', '2'\n'Hat', 'Puma', '49', '2'\n'Hat', 'Nike', '46', '5'\n'Shoe', 'Adidas', '50', '1'\n'Shoe', 'Reebok', '48', '2'\n'Shoe', 'Puma', '47', '3'\n'Shoe', 'Puma', '47', '3'\n'Shoe', 'Nike', '45', '5'\n'T-Shirt', 'Nike', '100', '1'\n'T-Shirt', 'Van Huesen', '100', '1'\n'T-Shirt', 'Levi', '99', '3'\n'T-Shirt', 'Adidas', '98', '4'\n'T-Shirt', 'Adidas', '94', '5'",
        'Answer': "The top 5 items in each category, ranked by stock quantity, include: Accessories by Fossil and Ray-Ban; Hats by New Era, Adidas, and Puma; Shoes by Adidas, Reebok, and Puma; T-Shirts by Nike, Van Huesen, Levi, and Adidas."
    }
    
]
