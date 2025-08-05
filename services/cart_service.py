import pymysql
import streamlit as st
import os 
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from database.database_connection import SqlConnection
from models.product_model import Products
from models.cart_model import UserCart

class CartServices:
    @staticmethod
    def find_quantity_in_cart(product_id, cart_obj):
        """
        Find the quantity of a product in the user's cart
        
        Args:
            product_id (str): The product ID to search for
            cart_obj: UserCart object containing user_cart_items
            
        Returns:
            int: Quantity of the product if exists, 0 otherwise
        """
        try:
            # Validate cart object
            if not cart_obj or not hasattr(cart_obj, 'user_cart_items'):
                return 0
            if cart_obj.user_cart_items is None:
                return 0
            # Check if product exists in user_cart_items
            if str(product_id) in cart_obj.user_cart_items:
                return cart_obj.user_cart_items[str(product_id)]
            else:
                return 0
            
        except Exception as e:
            return 0
    
    @staticmethod
    def add_to_cart(product_id, user_cart_obj, user_id):
        """
        Add product to cart object and sync with database. If exists, increment quantity by 1
        
        Args:
            product_id (str): Product ID to add
            user_cart_obj: UserCart object
            user_id (str): User ID
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            if not user_cart_obj or not hasattr(user_cart_obj, 'user_cart_items'):
                st.error("Invalid cart object")
                return False
            
            # Update cart object first
            if str(product_id) in user_cart_obj.user_cart_items:
                # Product exists, increment quantity
                user_cart_obj.user_cart_items[str(product_id)] += 1
            else:
                # Product doesn't exist, add with quantity 1
                user_cart_obj.user_cart_items[str(product_id)] = 1
            
            # Sync with database after successful object operation
            database_success = CartServices.add_to_cart_database(product_id, user_cart_obj, user_id)
            
            if not database_success:
                # Rollback object changes if database operation failed
                if str(product_id) in user_cart_obj.user_cart_items:
                    if user_cart_obj.user_cart_items[str(product_id)] > 1:
                        user_cart_obj.user_cart_items[str(product_id)] -= 1
                    else:
                        del user_cart_obj.user_cart_items[str(product_id)]
                st.error("Failed to sync with database. Changes reverted.")
                return False
            
            return True
            
        except Exception as e:
            st.error(f"Error adding to cart: {str(e)}")
            return False


    @staticmethod
    def remove_from_cart(product_id, user_cart_obj, user_id):
        """
        Remove one quantity from cart object and sync with database. If quantity is 1, delete the product
        
        Args:
            product_id (str): Product ID to remove
            user_cart_obj: UserCart object
            user_id (str): User ID
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            if not user_cart_obj or not hasattr(user_cart_obj, 'user_cart_items'):
                st.error("Invalid cart object")
                return False
            
            if str(product_id) not in user_cart_obj.user_cart_items:
                st.warning(f"Product {product_id} not found in cart")
                return False
            
            # Store original state for potential rollback
            original_quantity = user_cart_obj.user_cart_items[str(product_id)]
            was_deleted = False
            
            # Update cart object first
            current_quantity = user_cart_obj.user_cart_items[str(product_id)]
            
            if current_quantity > 1:
                # Decrement quantity
                user_cart_obj.user_cart_items[str(product_id)] -= 1
            else:
                # Quantity is 1, delete the product
                del user_cart_obj.user_cart_items[str(product_id)]
                was_deleted = True
            
            # Sync with database after successful object operation
            database_success = CartServices.remove_from_cart_database(product_id, user_cart_obj, user_id)
            
            if not database_success:
                # Rollback object changes if database operation failed
                if was_deleted:
                    user_cart_obj.user_cart_items[str(product_id)] = original_quantity
                else:
                    user_cart_obj.user_cart_items[str(product_id)] = original_quantity
                st.error("Failed to sync with database. Changes reverted.")
                return False
            
            return True
                
        except Exception as e:
            st.error(f"Error removing from cart: {str(e)}")
            return False


    @staticmethod
    def delete_from_cart(product_id, user_cart_obj, user_id):
        """
        Delete product completely from cart object and sync with database
        
        Args:
            product_id (str): Product ID to delete
            user_cart_obj: UserCart object
            user_id (str): User ID
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            if not user_cart_obj or not hasattr(user_cart_obj, 'user_cart_items'):
                st.error("Invalid cart object")
                return False
            
            if str(product_id) not in user_cart_obj.user_cart_items:
                st.warning(f"Product {product_id} not found in cart")
                return False
            
            # Store original state for potential rollback
            original_quantity = user_cart_obj.user_cart_items[str(product_id)]
            
            # Update cart object first - delete the product from cart
            del user_cart_obj.user_cart_items[str(product_id)]
            
            # Sync with database after successful object operation
            database_success = CartServices.delete_from_cart_database(product_id, user_cart_obj, user_id)
            
            if not database_success:
                # Rollback object changes if database operation failed
                user_cart_obj.user_cart_items[str(product_id)] = original_quantity
                st.error("Failed to sync with database. Changes reverted.")
                return False
            
            return True
                
        except Exception as e:
            st.error(f"Error deleting from cart: {str(e)}")
            return False

    @staticmethod
    def empty_whole_cart(user_cart_obj, user_id):
        """
        Empty the entire cart object and sync with database
        
        Args:
            user_cart_obj: UserCart object
            user_id (str): User ID
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            if not user_cart_obj or not hasattr(user_cart_obj, 'user_cart_items'):
                st.error("Invalid cart object")
                return False
            
            # Store original state for potential rollback
            original_cart = user_cart_obj.user_cart_items.copy()
            
            # Update cart object first - empty the cart
            user_cart_obj.user_cart_items = {}
            
            # Sync with database after successful object operation
            database_success = CartServices.empty_whole_cart_database(user_id)
            
            if not database_success:
                # Rollback object changes if database operation failed
                user_cart_obj.user_cart_items = original_cart
                st.error("Failed to sync with database. Changes reverted.")
                return False
            
            
            return True
            
        except Exception as e:
            st.error(f"Error emptying cart: {str(e)}")
            return False


    @staticmethod
    def empty_whole_cart_database(user_id):
        """
        Empty the entire cart in database for a specific user
        
        Args:
            user_id (str): User ID whose cart to empty
            
        Returns:
            bool: True if successful, False otherwise
        """
        connect = SqlConnection()
        
        try:
            if not user_id:
                st.error("User ID is required")
                return False
            
            if connect.connect():
                # Check if user has any items in cart
                check_sql = "SELECT COUNT(*) as count FROM cart_items WHERE user_id = %s"
                
                with connect.connection.cursor() as cursor:
                    cursor.execute(check_sql, (user_id,))
                    result = cursor.fetchone()
                    
                    if result and result['count'] > 0:
                        # Delete all cart items for the user
                        delete_sql = "DELETE FROM cart_items WHERE user_id = %s"
                        cursor.execute(delete_sql, (user_id,))
                        connect.connection.commit()
                        
                        # Get number of deleted rows
                        deleted_count = cursor.rowcount
                        return True
                    else:

                        return True  # Consider empty cart as success
            else:
                return False
                
        except pymysql.Error as e:
            st.error(f"Database error while emptying cart: {str(e)}")
            if connect.connection:
                connect.connection.rollback()
            return False
        except Exception as e:
            st.error(f"Unexpected error while emptying cart: {str(e)}")
            if connect.connection:
                connect.connection.rollback()
            return False
            
        finally:
            connect.disconnect()
        
        return False

    @staticmethod
    def add_to_cart_database(product_id, user_cart_obj, user_id):
        """
        Add product to cart in database. If exists, increment quantity by 1
        
        Args:
            product_id (str): Product ID to add
            user_cart_obj: UserCart object (for potential updates)
            user_id (str): User ID
            
        Returns:
            bool: True if successful, False otherwise
        """
        connect = SqlConnection()
        
        try:
            if connect.connect():
                # Check if product exists in user's cart
                check_sql = "SELECT quantity FROM cart_items WHERE user_id = %s AND product_id = %s"
                
                with connect.connection.cursor() as cursor:
                    cursor.execute(check_sql, (user_id, product_id))
                    result = cursor.fetchone()
                    
                    if result:
                        # Product exists, increment quantity
                        new_quantity = result['quantity'] + 1
                        update_sql = "UPDATE cart_items SET quantity = %s WHERE user_id = %s AND product_id = %s"
                        cursor.execute(update_sql, (new_quantity, user_id, product_id))
                    else:
                        # Product doesn't exist, insert new record
                        insert_sql = "INSERT INTO cart_items (user_id, product_id, quantity) VALUES (%s, %s, %s)"
                        cursor.execute(insert_sql, (user_id, product_id, 1))
                    
                    connect.connection.commit()
                    return True
            else:
                st.error("Failed to connect to database")
                return False
                
        except pymysql.Error as e:
            st.error(f"Database error while adding to cart: {str(e)}")
            if connect.connection:
                connect.connection.rollback()
            return False
        except Exception as e:
            st.error(f"Unexpected error while adding to cart: {str(e)}")
            if connect.connection:
                connect.connection.rollback()
            return False
            
        finally:
            connect.disconnect()
        
        return False


    @staticmethod
    def remove_from_cart_database(product_id, user_cart_obj, user_id):
        """
        Remove one quantity from cart in database. If quantity is 1, delete the row
        
        Args:
            product_id (str): Product ID to remove
            user_cart_obj: UserCart object (for potential updates)
            user_id (str): User ID
            
        Returns:
            bool: True if successful, False otherwise
        """
        connect = SqlConnection()
        
        try:
            if connect.connect():
                # Check if product exists in user's cart
                check_sql = "SELECT quantity FROM cart_items WHERE user_id = %s AND product_id = %s"
                
                with connect.connection.cursor() as cursor:
                    cursor.execute(check_sql, (user_id, product_id))
                    result = cursor.fetchone()
                    
                    if result:
                        current_quantity = result['quantity']
                        
                        if current_quantity > 1:
                            # Decrement quantity
                            new_quantity = current_quantity - 1
                            update_sql = "UPDATE cart_items SET quantity = %s WHERE user_id = %s AND product_id = %s"
                            cursor.execute(update_sql, (new_quantity, user_id, product_id))
                        else:
                            # Quantity is 1, delete the row
                            delete_sql = "DELETE FROM cart_items WHERE user_id = %s AND product_id = %s"
                            cursor.execute(delete_sql, (user_id, product_id))
                        
                        connect.connection.commit()
                        return True
                    else:
                        return False
            else:
                return False
                
        except pymysql.Error as e:
            if connect.connection:
                connect.connection.rollback()
            return False
        except Exception as e:
            if connect.connection:
                connect.connection.rollback()
            return False
            
        finally:
            connect.disconnect()
        
        return False


    @staticmethod
    def delete_from_cart_database(product_id, user_cart_obj, user_id):
        """
        Delete product completely from cart in database
        
        Args:
            product_id (str): Product ID to delete
            user_cart_obj: UserCart object (for potential updates)
            user_id (str): User ID
            
        Returns:
            bool: True if successful, False otherwise
        """
        connect = SqlConnection()
        
        try:
            if connect.connect():
                # Check if product exists in user's cart
                check_sql = "SELECT quantity FROM cart_items WHERE user_id = %s AND product_id = %s"
                
                with connect.connection.cursor() as cursor:
                    cursor.execute(check_sql, (user_id, product_id))
                    result = cursor.fetchone()
                    
                    if result:
                        # Delete the product from cart
                        delete_sql = "DELETE FROM cart_items WHERE user_id = %s AND product_id = %s"
                        cursor.execute(delete_sql, (user_id, product_id))
                        connect.connection.commit()
                        return True
                    else:
                        return False
            else:
                return False
                
        except pymysql.Error as e:
            if connect.connection:
                connect.connection.rollback()
            return False
        except Exception as e:
            if connect.connection:
                connect.connection.rollback()
            return False
            
        finally:
            connect.disconnect()
        
        return False
    
    @staticmethod
    def total_cart_price(user_id):
        """
        Calculate total cart price for a specific user using user_id
        
        Args:
            user_id (str): User ID to calculate cart total for
            
        Returns:
            int: Total cart price, 0 if error or empty cart
        """
        connect = SqlConnection()
        
        try:
            if connect.connect():
                sql = """
                SELECT 
                    ROUND(SUM(p.price * ci.quantity)) as total_price
                FROM cart_items ci
                JOIN products p ON ci.product_id = p.product_id
                WHERE ci.user_id = %s
                """
                
                with connect.connection.cursor() as cursor:
                    cursor.execute(sql, (user_id,))
                    result = cursor.fetchone()
                    
                    if result and result['total_price']:
                        return int(result['total_price'])
                    else:
                        return 0
            else:
                return 0
                
        except pymysql.Error as e:
            st.error(f"Database error while calculating total cart price: {str(e)}")
            return 0
        except Exception as e:
            st.error(f"Unexpected error while calculating total cart price: {str(e)}")
            return 0
            
        finally:
            connect.disconnect()
        
        return 0


    @staticmethod
    def total_discount_price(user_id):
        """
        Calculate total discount for a specific user using user_id
        
        Args:
            user_id (str): User ID to calculate discount total for
            
        Returns:
            int: Total discount amount, 0 if error or no discounts
        """
        connect = SqlConnection()
        
        try:
            if connect.connect():
                sql = """
                SELECT 
                    ROUND(SUM(
                        CASE 
                            WHEN p.discount IS NOT NULL 
                            THEN (p.price * p.discount / 100) * ci.quantity
                            ELSE 0
                        END
                    )) as total_discount
                FROM cart_items ci
                JOIN products p ON ci.product_id = p.product_id
                WHERE ci.user_id = %s
                """
                
                with connect.connection.cursor() as cursor:
                    cursor.execute(sql, (user_id,))
                    result = cursor.fetchone()
                    
                    if result and result['total_discount']:
                        return int(result['total_discount'])
                    else:
                        return 0
            else:
                return 0
                
        except pymysql.Error as e:
            st.error(f"Database error while calculating total discount: {str(e)}")
            return 0
        except Exception as e:
            st.error(f"Unexpected error while calculating total discount: {str(e)}")
            return 0
            
        finally:
            connect.disconnect()
        
        return 0


    @staticmethod
    def final_cart_price(user_id):
        """
        Calculate final cart price for a specific user (total - discount) using SQL
        
        Args:
            user_id (str): User ID to calculate final price for
            
        Returns:
            int: Final cart price after discounts, 0 if error
        """
        connect = SqlConnection()
        
        try:
            if connect.connect():
                sql = """
                SELECT 
                    ROUND(
                        SUM(p.price * ci.quantity) - SUM(
                            CASE 
                                WHEN p.discount IS NOT NULL 
                                THEN (p.price * p.discount / 100) * ci.quantity
                                ELSE 0
                            END
                        )
                    ) as final_price
                FROM cart_items ci
                JOIN products p ON ci.product_id = p.product_id
                WHERE ci.user_id = %s
                """
                
                with connect.connection.cursor() as cursor:
                    cursor.execute(sql, (user_id,))
                    result = cursor.fetchone()
                    
                    if result and result['final_price']:
                        return int(result['final_price'])
                    else:
                        return 0
            else:
                return 0
                
        except pymysql.Error as e:
            st.error(f"Database error while calculating final cart price: {str(e)}")
            return 0
        except Exception as e:
            st.error(f"Unexpected error while calculating final cart price: {str(e)}")
            return 0
            
        finally:
            connect.disconnect()
        
        return 0