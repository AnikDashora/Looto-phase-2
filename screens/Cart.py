import streamlit as st
import os 
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from services.product_service import ProductService
from services.cart_service import CartServices

remove_header_footer = """
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    /* Hide the orange loading progress bar */
    div[data-testid="stDecoration"] {
        display: none !important;
    }
    .stDeployButton{
        display:none;
    }
    /* Remove top padding to avoid white space */
    .block-container {
        padding-top: 1rem !important;
    }
"""

page_setup = """
        :root {
            --primary: #6366f1;
            --primary-dark: #4f46e5;
            --secondary: #f59e0b;
            --accent: #06d6a0;
            --background: #fefefe;
            --card: #ffffff;
            --text-primary: #1a1a1a;
            --text-secondary: #6b7280;
            --border: #e5e7eb;
            --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
            --radius: 12px;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: var(--background);
            color: var(--text-primary);
            line-height: 1.6;
        }

        .stApp {
                min-height: 100vh !important;
                display: flex !important;
                flex-direction: column !important;
                background: var(--background) !important;
                padding: var(--page-padding);
                box-sizing: border-box;
            }

            /* Main View Container */
            .stAppViewContainer {
                flex: 1 1 auto !important;
                max-width: var(--max-width);
                margin: 0 auto;
                width: 100%;
                background: transparent !important;
                padding: 0 !important;
                display: flex;
                flex-direction: column;
                gap: 2.5rem;
                
            }

            /* Main Block Container */
            .stMainBlockContainer {
                background: transparent !important;
                padding: 0 !important;
                width: 100% !important;
                max-width: var(--max-width) !important;
                margin: 0 auto;
                flex: 1 1 auto !important;
                display: flex !important;
                flex-direction: column !important;
                gap: 2rem;
            }

            /* In the Main container inside MainBlockContainer */
            .stMain .stMainBlockContainer {
                padding: 0 !important;
                margin: 0 auto;
                
                
            }

            /* Vertical block (commonly for rows of content) */
            

            /* Remove default top padding for block container (as per your remove_header_footer style) */
            .block-container {
                padding-top: 1rem !important;
            }

            .stMainBlockContainer .st-emotion-cache-8fjoqp{
                gap:0rem;
            } 
"""

navbar_styles = """
        .st-key-navbar {
            background: var(--card);
            box-shadow: var(--shadow);
            padding: 1rem 0;
            top: 0;
            z-index: 100;
            border-bottom: 1px solid var(--border);
            position: sticky; /* To keep navbar sticky */
            width: 100%;
        }

        .st-key-nav-container{
            margin: 0 auto;
            padding: 0 2rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 2rem;
            width: 100%;
            max-width: 2000px;
            min-height:fit-content;
        }

        

        .logo {
            font-size: 2rem;
            font-weight: 800;
            color: var(--primary);
            text-decoration: none;
            letter-spacing: -0.02em;
            flex-shrink: 0;
            user-select: none;
            transition: color 0.2s;
        }

        .st-key-navbar .st-emotion-cache-ko87jo{
            display:flex;
            align-items:center;
        }

        .st-key-search-container {
            display:flex;
            align-item:center;
            justify-content:center;
            flex: 1;
            max-width: 700px;
            position: relative;
            margin: 0 1rem;
        }


        .st-key-search-bar {
            width: 100%;
            position: relative;
        }

        .stTextinput{
            width: 100%;
        }

        .stTextInput:focus-within{
            border:none;!important
            outline:none;!important
        }

        div[data-baseweb="input"]{
            border:none;
            height: 45px;
            width:100%;
            padding:0;
            gap:10px
        }

        .stTextInput input {
            width: 100%;
            padding: 0.75rem 1rem 0.75rem 3rem;
            border: 2px solid var(--border);
            border-radius: var(--radius);
            font-size: 1rem;
            transition: all 0.3s ease;
            background: #f8fafc;
        }

        .stTextInput input:focus {
            outline: none;
            border-color: var(--primary);
            background: white;
            box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.2);
        }

        .st-key-search-bar::before {
            content: '\f002';
            font-family: 'Font Awesome 6 Free';
            font-weight: 900;
            position: absolute;
            left: 1rem;
            top: 50%;
            transform: translateY(-50%);
            color: var(--text-secondary);
            z-index: 1;
        }

        .st-key-nav-buttons {
            display: flex;
            align-items: center;
            gap: 1.2rem;
        }

        .st-key-nav-buttons .stHorizontalBlock{
            display: flex;
            align-items: center;
            justify-content:center;
            gap: 1.2rem;
        }

        [class *= "st-key-nav-btn-"]{
            display: flex;
            align-items: center;
        }

        .st-key-nav-buttons .stButton {
            display: flex;
            align-items: center;
            justify-content:center;
        }

        .st-key-nav-buttons .stButton button {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.75rem 1.15rem;
            border: none;
            border-radius: var(--radius);
            font-size: 1rem;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.3s ease;
            text-decoration: none;
            color: var(--text-primary);
            background: white;
            border: 1px solid var(--border);
            overflow: hidden;
            flex-wrap: wrap;
            overwrite: hidden;
            outline: none;
        }

        .st-key-nav-buttons .stButton button:hover,
        .st-key-nav-buttons .stButton button:focus-visible {
            background: var(--primary);
            color: white;
            transform: translateY(-2px) scale(1.03);
            box-shadow: var(--shadow);
        }

        .st-key-nav-btn-3 .stButton button {
            background: linear-gradient(135deg, var(--primary), var(--primary-dark));
            color: white;
            border: none;
        }

        .st-key-nav-btn-3 .stButton button:hover,
        .st-key-nav-btn-3 .stButton button:focus-visible {
            background: linear-gradient(135deg, var(--primary-dark), #3730a3);
        }

        .st-key-nav-buttons .stButton button span {
            display: flex;
            align-items: center;
            justify-content:center;
        }

        .st-key-nav-buttons .stButton button p {
            margin: 0;
        }

        .st-key-search-container {
            display: flex;
            align-items: center;
            justify-content: center;
            flex: 1;
            max-width: 600px;
            position: relative;
            margin: 0 2rem;
        }

        .st-key-search-bar {
            width: 100%;
            position: relative;
        }        

"""

cart_header_style = """
        .st-key-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }

        .st-key-cart-header {
            margin-bottom: 2rem;
            display: flex;
            align-items: center;
            flex-direction: row;
            gap:10rem;
        }

        .st-key-back-button {
            margin-bottom: 1rem;
            max-width:200px;
            width:100%;
            flex-wrap:wrap;
        }

        .st-key-back-button .stButton button {
            width:100%;
            background: transparent;
            border: none;
            border-radius: var(--radius);
            padding: 0.75rem 1rem;
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            cursor: pointer;
            transition: all 0.2s;
            font-weight: 500;
            color: var(--text-secondary);
            font-size: 0.9rem;
        }

        .st-key-back-button .stButton button:hover {
            color: var(--primary-dark);
            background-color: rgba(99, 102, 241, 0.2);
        }

        .cart-title-section .page-title {
            font-size: 2rem;
            font-weight: bold;
            color: var(--primary);
            margin-bottom: 0.5rem;
        }

        .cart-title-section .item-count {
            color: var(--text-secondary);
            font-size: 2rem;
        }
"""

cart_layout_style = """
        .st-key-cart-layout {
            display: grid;
            grid-template-columns: 2fr 1fr;
            gap: 2rem;
        }

        .section-title {
            font-size: 1.25rem;
            font-weight: 600;
            margin-bottom: 1.5rem;
            color: var(--text-primary);
        }

        /* Cart Items */
        .st-key-cart-items {
            background: var(--card);
            border-radius: var(--radius);
            padding: 1.5rem;
            box-shadow: var(--shadow);
            max-height: fit-content;
        }

        [class *= "st-key-cart-item-"] {
            display: flex;
            align-items: center;
            flex-direction: row;
            gap: 1rem;
            padding: 1rem 0;
            /* border-radius: var(--radius); */
            /* margin-bottom: 1rem; */
            transition: all 0.2s;
            border-bottom: 1px solid var(--border);
        }

        [class *= "st-key-cart-item-"]:last-child {
            /* margin-bottom: 0; */
            border-bottom: none;
        }

        [class *= "st-key-details-"]{
            display:flex;
            align-items: center;
            flex-direction: row;
            gap:2rem;
        }
        [class *= "st-key-details-"] .stElementContainer{
            width:fit-content;
        }
        .item-image-details {
            width: 80px;
            height: 80px;
            border-radius: var(--radius);
            overflow: hidden;
            background: #f3f4f6;
            flex-shrink: 0;
            position: relative;
        }

        .item-image-details .item-image {
            width: 100%;
            height: 100%;
            object-fit: cover;
            object-position: center;
            display: block;
            border-radius: var(--radius);
            background: #f3f4f6;
        }

        .item-details {
            flex: 1;
        }

        .item-details .item-name {
            font-size: 1.1rem;
            font-weight: 600;
            margin-bottom: 0.5rem;
            color: var(--text-primary);
            word-break:none;
        }

        .item-details .item-price {
            font-size: 1.3rem;
            font-weight: bold;
            color: var(--primary);
        }

        .item-details .item-original-price {
            /* font-size: 1rem; */
            color: var(--text-secondary);
            text-decoration: line-through;
            margin-left: 0.5rem;
        }

        .item-details .item-subtotal {
            color: var(--text-secondary);
            /* font-size: 0.95rem; */
            margin-top: 0.5rem;
        }

        [class *= "st-key-item-controls-"]{
            display: flex;
            align-items: center;
            justify-content:space-around;
            flex-direction: row;
        }
        [class *= "st-key-quantity-controls-"] {
            display: flex;
            align-items: center;
            flex-direction: row;
            gap: 0.5rem;
            background: rgba(99, 102, 241, 0.2);
            border-radius: 50px;
            padding: 0.25rem;
            width: fit-content;
            border:1px solid var(--border);
        }

        [class *= "st-key-minus-btn-"] .stButton button,
        [class *= "st-key-plus-btn-"] .stButton button {
            width: 2.5rem;
            height: 2.5rem;
            border: none;
            background: var(--primary);
            color: white;
            border-radius: 50%;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 600;
            font-size: 1.1rem;
            transition: background 0.2s;
        }

        [class *= "st-key-minus-btn-"] .stButton button:hover,
        [class *= "st-key-plus-btn-"] .stButton button:hover {
            background: var(--primary-dark);
        }

        .quantity-display {
            min-width: 40px;
            height:40px;
            text-align: center;
            border:none;
            font-weight: 600;
            font-size: 1rem;
            background-color: transparent;
            width: fit-content;
        }

        [class *= "st-key-remove-btn-"] .stButton button {
            width:2.5rem;
            height:2.5rem;
            background: none;
            border: none;
            color: #ef4444;
            padding: 0.5rem;
            border-radius: 50%;
            cursor: pointer;
            font-size: 1.2rem;
            transition: all 0.2s;
            cursor: pointer;
        }

        [class *= "st-key-remove-btn-"] .stButton button:hover {
            background: rgba(239, 68, 68, 0.1);
        }

"""

order_summary_styles = """
        .st-key-order-summary {
            background: var(--card);
            border-radius: var(--radius);
            padding: 1.5rem;
            box-shadow: var(--shadow);
            height: fit-content;
            position: sticky;
            top: 100px;
        }

        .summary-row {
            display: flex;
            justify-content: space-between;
            margin-bottom: 1rem;
            font-size: 1rem;
        }

        .savings {
            color: var(--accent);
            font-weight: 500;
        }

        .shipping-free {
            color: var(--accent);
            font-weight: 600;
        }

        .total-row {
            border-top: 1px solid var(--border);
            padding-top: 1rem;
            margin-top: 1rem;
            font-size: 1.2rem;
            font-weight: 700;
        }

        .total-value {
            font-size: 1.4rem;
            color: var(--primary);
        }

        .icon-small{
            width:16px;
            height:16px;
        }

        .savings-banner {
            background: rgba(6, 214, 160, 0.1);
            border: 1px solid rgba(6, 214, 160, 0.2);
            border-radius: var(--radius);
            padding: 0.75rem;
            margin: 1rem 0;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            color: var(--accent);
            font-size: 0.9rem;
            font-weight: 500;
        }

        .st-key-checkout-btn .stButton button {
            width: 100%;
            background: var(--primary);
            color: white;
            border: none;
            border-radius: var(--radius);
            padding: 1rem;
            cursor: pointer;
            font-weight: 600;
            font-size: 1.1rem;
            transition: all 0.2s;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .st-key-checkout-btn .stButton button:hover {
            background: var(--primary-dark);
            transform: translateY(-2px);
            box-shadow: var(--shadow-lg);
        }

        .st-key-continue-shopping .stButton button {
            width: 100%;
            background: transparent;
            color: var(--primary);
            border: none;
            border-radius: var(--radius);
            padding: 0.75rem;
            cursor: pointer;
            font-weight: 500;
            transition: all 0.2s;
            margin-bottom: 1rem;
        }

        .st-key-continue-shopping .stButton button:hover {
            background: rgba(99, 102, 241, 0.2);
        }

        .trust-indicators {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 1.5rem;
            padding-top: 1rem;
            border-top: 1px solid var(--border);
            font-size: 0.875rem;
            color: var(--text-secondary);
        }

        .trust-item {
            display: flex;
            align-items: center;
            gap: 0.25rem;
            color: var(--accent);
            /* font-size: 0.85rem; */
            /* font-weight: 500; */
        }

        .trust-item .icon-small {
            color: var(--accent);
        }     
"""
reponsive_style = """
        @media (max-width: 768px) {
            .st-key-header-content {
                flex-direction: column;
                gap: 1rem;
                padding: 1rem;
            }

            .st-key-cart-layout {
                grid-template-columns: 1fr;
                gap: 1rem;
            }

            .st-key-order-summary {
                position: static;
            }

            [class *= "st-key-cart-item-"] {
                flex-direction: column;
                text-align: center;
            }

            [class *= "st-key-item-control-"] {
                align-items: center;
                flex-direction: row;
                justify-content: space-between;
            }
        }

"""

styles = f"""
<style>
{remove_header_footer}
{page_setup}
{navbar_styles}
{cart_header_style}
{cart_layout_style}
{order_summary_styles}
{reponsive_style}
</style>
"""

def apply_discount(price, discount):
    """Calculate discounted price"""
    discounted_price = int(round(price * ((100 - discount) / 100)))
    return discounted_price

def make_price_string(price):
    """Format price with comma separator"""
    price_str = str(price)
    if len(price_str) > 3:
        return price_str[:-3] + "," + price_str[-3:]
    return price_str

# cart_items = [
#     {
#     "name":"iPhone 15 Pro Max",
#     "price":159999,
#     "discount":16,
#     "image":"https://images.unsplash.com/photo-1592750475338-74b7b21085ab?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80",
#     "des":"""
#         The iPhone 15 Pro Max represents the pinnacle of Apple's smartphone technology. Featuring the powerful A17 Pro chip, 
#         an advanced camera system with 5x optical zoom, and a stunning titanium design, this device delivers unparalleled 
#         performance and photography capabilities. With its 6.7-inch Super Retina XDR display and all-day battery life, 
#         the iPhone 15 Pro Max is perfect for professionals and enthusiasts who demand the very best."""
#     },
#     {
#     "name":"iPhone 15 Pro Max",
#     "price":159999,
#     "discount":16,
#     "image":"https://images.unsplash.com/photo-1592750475338-74b7b21085ab?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80",
#     "des":"""
#         The iPhone 15 Pro Max represents the pinnacle of Apple's smartphone technology. Featuring the powerful A17 Pro chip, 
#         an advanced camera system with 5x optical zoom, and a stunning titanium design, this device delivers unparalleled 
#         performance and photography capabilities. With its 6.7-inch Super Retina XDR display and all-day battery life, 
#         the iPhone 15 Pro Max is perfect for professionals and enthusiasts who demand the very best."""
#     },
#     {
#     "name":"iPhone 15 Pro Max",
#     "price":159999,
#     "discount":16,
#     "image":"https://images.unsplash.com/photo-1592750475338-74b7b21085ab?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80",
#     "des":"""
#         The iPhone 15 Pro Max represents the pinnacle of Apple's smartphone technology. Featuring the powerful A17 Pro chip, 
#         an advanced camera system with 5x optical zoom, and a stunning titanium design, this device delivers unparalleled 
#         performance and photography capabilities. With its 6.7-inch Super Retina XDR display and all-day battery life, 
#         the iPhone 15 Pro Max is perfect for professionals and enthusiasts who demand the very best."""
#     },
#     {
#     "name":"iPhone 15 Pro Max",
#     "price":159999,
#     "discount":16,
#     "image":"https://images.unsplash.com/photo-1592750475338-74b7b21085ab?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80",
#     "des":"""
#         The iPhone 15 Pro Max represents the pinnacle of Apple's smartphone technology. Featuring the powerful A17 Pro chip, 
#         an advanced camera system with 5x optical zoom, and a stunning titanium design, this device delivers unparalleled 
#         performance and photography capabilities. With its 6.7-inch Super Retina XDR display and all-day battery life, 
#         the iPhone 15 Pro Max is perfect for professionals and enthusiasts who demand the very best."""
#     }
# ]
def cart_page():
    cart_items = st.session_state["user_cart"].user_cart_items
    list_cart_items = list(cart_items.keys())
    st.set_page_config(
        page_title="Looto - Your Trusted Shopping Destination",
        page_icon="🛍️",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    st.markdown(styles,unsafe_allow_html=True)

    with st.container(key = "navbar"):
        with st.container(key = "nav-container"):
            logo_col,search_bar_col,nav_button_col = st.columns([1,5,4])
            with logo_col:
                st.markdown(
                    """
                    <div class = "logo">Looto</div>
                    """,unsafe_allow_html=True
                )
            
            with search_bar_col:
                with st.container(key = "search-container"):
                    search_item = st.text_input(
                        label="search bar",
                        key="search-bar",
                        label_visibility="collapsed",
                        placeholder="Search for products, brands and more...",
                        icon = ":material/search:"
                    )
            
            with nav_button_col:
                with st.container(key = "nav-buttons"):
                    cart_col,order_col,user_col = st.columns(3)
                    
                    with cart_col:
                        st.button(
                            label="Home",
                            key = "nav-btn-1",
                            type="secondary",
                            icon=":material/home:",
                            on_click=st.session_state["navigation"].to_home_page
                        )
                    with order_col:
                        st.button(
                            label="Orders",
                            key = "nav-btn-2",
                            type="secondary",
                            icon=":material/package_2:",
                            on_click=st.session_state["navigation"].to_order_page
                        )
                    with user_col:
                        label = ((st.session_state["current_user"].name).split(" "))[0] if(st.session_state["current_user"].user_exist) else "Signup"
                        st.button(
                            label=label,
                            key = "nav-btn-3",
                            type="secondary",
                            icon=":material/person:",
                            # on_click=check_user_exist,
                            help=label
                        )

    with st.container(key = "container"):
        with st.container(key = "cart-header"):
            st.button(
                label = "Back to Shopping",
                key = "back-button",
                icon = ":material/arrow_back:",
                type = "tertiary",
                on_click=st.session_state["navigation"].to_last_page
            )
            st.markdown(
                f"""
                <div class="cart-title-section">
                    <h1 class="page-title">My Shopping Cart</h1>
                    <p class="item-count">{len(list_cart_items)} items in your cart</p>
                </div>
                """,
                unsafe_allow_html=True
            )
        
        with st.container(key= "cart-layout"):
            with st.container(key = "cart-items"):
                st.markdown(
                    """
                    <h2 class="section-title">Cart Items</h2>
                    """,
                    unsafe_allow_html=True
                )
                for item in range(len(list_cart_items)):
                    product_id = list_cart_items[item]
                    item_product_data = ProductService.fetch_product_details(product_id)
                    item_quantity = cart_items[product_id]
                    with st.container(key = f"cart-item-{item+1}"):
                        with st.container(key = f"details-{item+1}"):
                            st.markdown(
                                f"""
                                <div class="item-image-details">
                                    <img src={item_product_data["image_url"]} alt={item_product_data["name"]} class="item-image" />
                                </div>
                                """,
                                unsafe_allow_html=True
                            )

                            st.markdown(
                                f"""
                                <div class="item-details">
                                    <h3 class="item-name">{item_product_data["name"]}</h3>
                                    <div>
                                        <span class="item-price">₹{make_price_string(apply_discount(int(item_product_data["price"]),item_product_data["discount"]))}</span>
                                        <span class="item-original-price">₹{make_price_string(int(item_product_data["price"]))}</span>
                                    </div>
                                    <p class="item-subtotal">Subtotal: ₹{make_price_string(item_quantity*apply_discount(int(item_product_data["price"]),item_product_data["discount"]))}</p>
                                </div>
                                """,
                                unsafe_allow_html=True
                            )

                        with st.container(key = f"item-controls-{item+1}"):
                            with st.container(key = f"quantity-controls-{item+1}"):
                                st.button(
                                    type="tertiary",
                                    label="",
                                    icon=":material/remove:",
                                    key=f"minus-btn-{item+1}",
                                    on_click=CartServices.remove_from_cart,
                                    args=(
                                        product_id,
                                        st.session_state["user_cart"],
                                        st.session_state["current_user"].user_id,
                                    )
                                )
                                st.markdown(
                                    f"""
                                    <div class = "quantity-display">{item_quantity}</div>
                                    """,
                                    unsafe_allow_html=True
                                )
                                st.button(
                                    type="tertiary",
                                    label="",
                                    icon=":material/add:",
                                    key=f"plus-btn-{item+1}",
                                    on_click=CartServices.add_to_cart,
                                    args=(
                                        product_id,
                                        st.session_state["user_cart"],
                                        st.session_state["current_user"].user_id,
                                    )
                                )
                            
                            st.button(
                                label="",
                                type = "tertiary",
                                key = f"remove-btn-{item+1}",
                                icon = ":material/delete:",
                                on_click=CartServices.delete_from_cart,
                                args=(
                                    product_id,
                                    st.session_state["user_cart"],
                                    st.session_state["current_user"].user_id,
                                )
                            )

            with st.container(key = "order-summary"):
                st.markdown(
                    """
                    <h2 class="section-title">Order Summary</h2>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown(
                    f"""
                    <div class="summary-row">
                        <span class="summary-label">Subtotal ({len(list_cart_items)} items)</span>
                        <span class="summary-value">₹{make_price_string(int(CartServices.total_cart_price(st.session_state["current_user"].user_id)))}</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown(
                    f"""
                    <div class="summary-row">
                        <span class="summary-label savings">Savings</span>
                        <span class="summary-value savings">-₹{make_price_string(int(CartServices.total_discount_price(st.session_state["current_user"].user_id)))}</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown(
                    """
                    <div class="summary-row">
                        <span class="summary-label">Shipping</span>
                        <span class="shipping-free">FREE</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown(
                    f"""
                    <div class="summary-row total-row">
                        <span class="total-label">Total</span>
                        <span class="total-value">₹{make_price_string(int(CartServices.final_cart_price(st.session_state["current_user"].user_id)))}</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown(
                    f"""
                    <div class="savings-banner">
                        <svg class="icon-small" viewBox="0 0 24 24" style="display: inline; margin-right: 0.5rem;">
                            <path fill="currentColor" d="M20 7h-3V6a4 4 0 0 0-8 0v1H6a1 1 0 0 0-1 1v11a3 3 0 0 0 3 3h8a3 3 0 0 0 3-3V8a1 1 0 0 0-1-1zM11 6a2 2 0 0 1 4 0v1h-4V6zm6 13a1 1 0 0 1-1 1H8a1 1 0 0 1-1-1V9h2v1a1 1 0 0 0 2 0V9h2v1a1 1 0 0 0 2 0V9h2v10z"/>
                        </svg>
                        You're saving ₹55,000 on this order!
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.button(
                    label="Proceed to Checkout",
                    type="secondary",
                    key = "checkout-btn",
                    icon = ":material/payments:"
                )

                st.button(
                    label="Continue Shopping",
                    type="tertiary",
                    key = "continue-shopping",
                    on_click=st.session_state["navigation"].to_home_page
                )

                st.markdown(
                    """
                    <div class="trust-indicators">
                        <div class="trust-item">
                            <svg class="icon-small" viewBox="0 0 24 24" style="margin-right: 0.25rem;">
                                <path fill="currentColor" d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/>
                            </svg>
                            Free Returns
                        </div>
                        <div class="trust-item">
                            <svg class="icon-small" viewBox="0 0 24 24" style="margin-right: 0.25rem;">
                                <path fill="currentColor" d="M20 8h-3V4H3c-1.1 0-2 .9-2 2v11h2c0 1.66 1.34 3 3 3s3-1.34 3-3h6c0 1.66 1.34 3 3 3s3-1.34 3-3h2v-5l-3-4zM6 18.5c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5zm13.5-9l1.96 2.5H17V9.5h2.5zm-1.5 9c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5z"/>
                            </svg>
                            Fast Delivery
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )



            

            

