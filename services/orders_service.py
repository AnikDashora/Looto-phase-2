import streamlit as st
import os
import sys
import pymysql
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)


from database.database_connection import SqlConnection

class OrderServices:
    @staticmethod
    def create_ids(order_id):
        """
        Create formatted order ID with 'o' prefix and zero padding
        
        Args:
            order_id (int): Numeric order ID
            
        Returns:
            str: Formatted order ID (e.g., 'o0001', 'o0025', 'o12345')
            
        Raises:
            ValueError: If order_id is not an integer
        """
        if isinstance(order_id, str):
            raise ValueError("Order ID must be an integer, not string")
        
        id_len = 4
        if len(str(order_id)) <= 4:
            prefix_len = id_len - len(str(order_id))
            return "o" + "0" * prefix_len + str(order_id)
        else:
            return "o" + str(order_id)

    @staticmethod
    def generate_order_id():
        """
        Generate a new order ID by checking the database for existing orders
        
        Returns:
            str: Next available formatted order ID (e.g., 'o0001')
            
        Raises:
            Exception: If database connection fails or other database errors occur
        """
        connect = SqlConnection()
        
        try:
            if not connect.connect():
                raise Exception("Failed to connect to database")
            
            # Check if orders table exists
            table_check_sql = "SHOW TABLES LIKE 'orders'"
            with connect.connection.cursor() as cursor:
                cursor.execute(table_check_sql)
                table_exists = cursor.fetchone()
                
                if not table_exists:
                    raise Exception("Orders table does not exist in database")
            
            # Get the count of existing orders
            count_sql = "SELECT COUNT(*) as count FROM orders"
            with connect.connection.cursor() as cursor:
                cursor.execute(count_sql)
                result = cursor.fetchone()
                
                if result:
                    order_count = result['count']
                    order_count += 1
                    order_id = order_count
                else:
                    order_id = 1
                    
            return OrderServices.create_ids(order_id)
            
        except Exception as e:
            print(f"Error generating order ID: {e}")
            raise e
            
        finally:
            connect.disconnect()
    
    @staticmethod
    def buy_now(user_id, products, orders_obj=None):
        """
        Process buy now order - create order and order items
        
        Args:
            user_id (str): User ID placing the order
            products (dict): Dictionary with {product_id: quantity}
            orders_obj (Orders): Orders class object to update order_ids list
            
        Returns:
            str: Order ID if successful, None if failed
        """
        connect = SqlConnection()
        
        try:
            if not products or not isinstance(products, dict):
                st.error("Invalid products data")
                return None
            
            if connect.connect():
                # Start transaction
                connect.connection.begin()
                
                # Generate new order ID
                order_id = OrderServices.generate_order_id()
                
                # Calculate total amount by fetching product prices
                total_amount = 0
                product_details = []
                
                for product_id, quantity in products.items():
                    # Get product details
                    product_sql = "SELECT price, discount FROM products WHERE product_id = %s"
                    with connect.connection.cursor() as cursor:
                        cursor.execute(product_sql, (product_id,))
                        product = cursor.fetchone()
                        
                        if not product:
                            st.error(f"Product {product_id} not found")
                            connect.connection.rollback()
                            return None
                        
                        # Calculate price with discount
                        base_price = float(product['price'])
                        discount = product['discount'] or 0
                        
                        if discount > 0:
                            discounted_price = base_price * (100 - discount) / 100
                        else:
                            discounted_price = base_price
                        
                        item_total = discounted_price * quantity
                        total_amount += item_total
                        
                        product_details.append({
                            'product_id': product_id,
                            'quantity': quantity,
                            'price_each': discounted_price
                        })
                
                # Insert into orders table
                order_sql = """
                INSERT INTO orders (order_id, user_id, status, total_amount) 
                VALUES (%s, %s, %s, %s)
                """
                
                with connect.connection.cursor() as cursor:
                    cursor.execute(order_sql, (order_id, user_id, 'Ordered', total_amount))
                
                # Insert into order_items table
                order_items_sql = """
                INSERT INTO order_items (order_id, product_id, quantity, price_each) 
                VALUES (%s, %s, %s, %s)
                """
                
                with connect.connection.cursor() as cursor:
                    for item in product_details:
                        cursor.execute(order_items_sql, (
                            order_id,
                            item['product_id'],
                            item['quantity'],
                            item['price_each']
                        ))
                
                # Commit transaction
                connect.connection.commit()
                
                # Add order_id to Orders object if provided
                if orders_obj and hasattr(orders_obj, 'order_ids'):
                    orders_obj.order_ids.append(order_id)               
                
                return order_id
                
        except pymysql.Error as e:
            st.error(f"Database error while placing order: {str(e)}")
            if connect.connection:
                connect.connection.rollback()
            return None
        except Exception as e:
            st.error(f"Unexpected error while placing order: {str(e)}")
            if connect.connection:
                connect.connection.rollback()
            return None
            
        finally:
            connect.disconnect()
        
        return None
    
    @staticmethod
    def find_order_date(user_id, order_id):
        """
        Find the order date for a given user_id and order_id
        
        Args:
            user_id (str): The user ID who placed the order
            order_id (str): The order ID to look up
            
        Returns:
            str: Order date in 'dd/mm/yyyy' format if found, None otherwise
        """
        connect = SqlConnection()
        
        try:
            if connect.connect():
                sql = """
                SELECT ordered_at 
                FROM orders 
                WHERE user_id = %s AND order_id = %s
                """
                
                with connect.connection.cursor() as cursor:
                    cursor.execute(sql, (user_id, order_id))
                    result = cursor.fetchone()
                    
                    if result and result['ordered_at']:
                        order_date = result['ordered_at']
                        # Format date to dd/mm/yyyy
                        formatted_date = order_date.strftime("%d/%m/%Y")
                        return formatted_date
                    else:
                        st.warning(f"No order found with ID {order_id} for user {user_id}")
                        return None
            else:
                st.error("Failed to connect to database")
                return None
            
        except pymysql.Error as e:
            st.error(f"Database error while fetching order date: {str(e)}")
            return None
        except Exception as e:
            st.error(f"Unexpected error while fetching order date: {str(e)}")
            return None
            
        finally:
            connect.disconnect()

    @staticmethod
    def find_total_amount(user_id, order_id):
        """
        Find the total amount for a specific order
        
        Args:
            user_id (str): User ID who placed the order
            order_id (str): Order ID to find total amount for
            
        Returns:
            int: Total amount rounded to integer, None if not found
        """
        connect = SqlConnection()
        
        try:
            if not user_id or not order_id:
                st.error("User ID and Order ID are required")
                return None
            
            if connect.connect():
                sql = "SELECT total_amount FROM orders WHERE user_id = %s AND order_id = %s"
                
                with connect.connection.cursor() as cursor:
                    cursor.execute(sql, (user_id, order_id))
                    result = cursor.fetchone()
                    
                    if result and result['total_amount']:
                        # Round and convert to integer
                        total_amount = round(float(result['total_amount']))
                        return int(total_amount)
                    else:
                        st.warning(f"Order {order_id} not found for user {user_id}")
                        return None
            else:
                st.error("Failed to connect to database")
                return None
                
        except pymysql.Error as e:
            st.error(f"Database error while fetching total amount: {str(e)}")
            return None
        except Exception as e:
            st.error(f"Unexpected error while fetching total amount: {str(e)}")
            return None
            
        finally:
            connect.disconnect()
        
        return None


    @staticmethod
    def find_status(user_id, order_id):
        """
        Find the status for a specific order
        
        Args:
            user_id (str): User ID who placed the order
            order_id (str): Order ID to find status for
            
        Returns:
            str: Order status, None if not found
        """
        connect = SqlConnection()
        
        try:
            if not user_id or not order_id:
                st.error("User ID and Order ID are required")
                return None
            
            if connect.connect():
                sql = "SELECT status FROM orders WHERE user_id = %s AND order_id = %s"
                
                with connect.connection.cursor() as cursor:
                    cursor.execute(sql, (user_id, order_id))
                    result = cursor.fetchone()
                    
                    if result and result['status']:
                        return result['status']
                    else:
                        st.warning(f"Order {order_id} not found for user {user_id}")
                        return None
            else:
                st.error("Failed to connect to database")
                return None
                
        except pymysql.Error as e:
            st.error(f"Database error while fetching order status: {str(e)}")
            return None
        except Exception as e:
            st.error(f"Unexpected error while fetching order status: {str(e)}")
            return None
            
        finally:
            connect.disconnect()
        
        return None
    
    @staticmethod
    def find_all_orders(order_id):
        """
        Find all products in an order based on order_id
        
        Args:
            order_id (str): Order ID to find products for
            
        Returns:
            list: List of dictionaries containing order item details, empty list if not found
        """
        connect = SqlConnection()
        
        try:
            if not order_id:
                st.error("Order ID is required")
                return []
            
            if connect.connect():
                sql = "SELECT * FROM order_items WHERE order_id = %s"
                
                with connect.connection.cursor() as cursor:
                    cursor.execute(sql, (order_id,))
                    results = cursor.fetchall()
                    
                    if results:
                        # Convert price_each to int and format the data
                        order_items = []
                        for item in results:
                            order_items.append({
                                'order_id': item['order_id'],
                                'product_id': item['product_id'],
                                'quantity': int(item['quantity']),
                                'price_each': int(round(float(item['price_each']))),
                                'item_total': int(round(float(item['price_each']))) * int(item['quantity'])
                            })
                        
                        return order_items
                    else:
                        st.info(f"No items found for order {order_id}")
                        return []
            else:
                st.error("Failed to connect to database")
                return []
                
        except pymysql.Error as e:
            st.error(f"Database error while fetching order items: {str(e)}")
            return []
        except Exception as e:
            st.error(f"Unexpected error while fetching order items: {str(e)}")
            return []
            
        finally:
            connect.disconnect()
        
        return []
