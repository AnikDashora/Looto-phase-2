import streamlit as st

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
            --success: #10b981;
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

order_header_styles = """
        .st-key-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }

        .st-key-order-header-title {
            margin-bottom: 2rem;
            display: flex;
            align-items: center;
            flex-direction: row;
            gap:10rem;
        }

        .st-key-back-button {
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

        .order-title-section .page-title {
            font-size: 2rem;
            font-weight: bold;
            color: var(--primary);
        }

        .order-title-section .item-count {
            color: var(--text-secondary);
            font-size: 2rem;
        }
""" 

order_box_styles = """
        [class *= "st-key-order-card-"] {
            background: var(--card);
            border-radius: 15px;
            padding: 2rem;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
            margin-bottom: 2rem;
        }

        [class *= "st-key-order-header-"] {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1rem;
        }

        .orders-id-price-details{
            display:flex;
            align-items:center;
            justify-content:space-between;
            flex-direction:row;
        }

        .orders-id-price-details>div{
            min-width:fit-content;
            min-height:fit-content;
        }

        .order-id {
            font-size: 1.25rem;
            font-weight: bold;
            color: var(--text-primary);
        }

        .order-price {
            font-size: 1.5rem;
            font-weight: bold;
            color: var(--primary);
        }

        .order-date {
            color: var(--text-secondary);
            font-size: 0.9rem;
        }

        .status-badge {
            background: rgba(16,185,129,0.3);
            padding: 0.25rem 0.75rem;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 500;
            text-align:center;
            color:black;
        }

        .tracking-info {
            display: flex;
            align-items: center;
            color: var(--text-secondary);
            margin-bottom: 2rem;
            font-size: 0.9rem;
        }

        .tracking-info::before {
            margin-right: 0.5rem;
        }

        [class *= "st-key-product-item-"] {
            display: flex;
            align-items: center;
            justify-content:center;
            flex-direction:row;
            gap: 1rem;
            padding: 1rem;
            border: 1px solid var(--border);
            border-radius: var(--radius);
            background: var(--background);
        }

        [class *= "st-key-product-item-"] div[data-testid="stMarkdownContainer"]{
            margin-bottom:0rem;
        }

        [class *= "st-key-order-product-details-"]{
            display:flex;
            align-items: center;
            flex-direction: row;
            gap:2rem;
        }
        [class *= "st-key-order-product-details-"] .stElementContainer{
            width:fit-content;
        }
        .product-image {
            width: 80px;
            height: 80px;
            border-radius: var(--radius);
            background: var(--background);
            margin-right: 1rem;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
            border: 1px solid var(--border);
        }

        .product-image img {
            display:block;
            width: 100%;
            height: 100%;
            object-fit: cover;
            border-radius: calc(var(--radius) - 1px);
        }

        .product-details {
            flex: 1;
        }

        .product-name {
            font-weight: 600;
            color: var(--text-primary);
            margin-bottom: 0.25rem;
        }

        .product-quantity {
            color: var(--text-secondary);
            font-size: 0.9rem;
            margin-bottom: 0.25rem;
        }

        .product-price {
            color: var(--primary);
            font-weight: 600;
        }

"""

view_button_styles = """
    [class  *= "st-key-view-button-"] .stButton{
        width:max-content;
    }

    [class  *= "st-key-view-button-"] .stButton button {
        background: rgba(99, 102, 241, 0.1);
            color: var(--primary);
            border: 1px solid var(--primary);
            padding: 0.5rem 1rem;
            border-radius: calc(var(--radius) - 4px);
            cursor: pointer;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.5rem;
    }

    [class  *= "st-key-view-button-"] .stButton button:hover {
            background: var(--primary);
            color: var(--card);
            transform: translateY(-2px);
    }

"""

styles = f"""
<style>
{remove_header_footer}
{page_setup}
{navbar_styles}
{order_header_styles}
{order_box_styles}
{view_button_styles}
</style>
"""

def make_price_string(price):
    """Format price with comma separator"""
    price_str = str(price)
    if len(price_str) > 3:
        return price_str[:-3] + "," + price_str[-3:]
    return price_str

def order_page():
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
                            label="My cart",
                            key = "nav-btn-1",
                            type="secondary",
                            icon=":material/shopping_cart:"
                        )
                    with order_col:
                        st.button(
                            label="Orders",
                            key = "nav-btn-2",
                            type="secondary",
                            icon=":material/package_2:"
                        )
                    with user_col:
                        # label = ((st.session_state["current_user"].name).split(" "))[0] if(st.session_state["current_user"].user_exist) else "Login/Signup"
                        st.button(
                            label="Sign Up",
                            key = "nav-btn-3",
                            type="secondary",
                            icon=":material/person:",
                            # on_click=check_user_exist,
                            # help=label
                        )

    with st.container(key = "container"):
        with st.container(key = "order-header-title"):
            st.button(
                label = "Back to Shopping",
                key = "back-button",
                icon = ":material/arrow_back:",
                type = "tertiary"
            )
            st.markdown(
                """
                <div class="order-title-section">
                    <h1 class="page-title">My Orders</h1>
                    <p class="item-count">Track and manage your order history</p>
                </div>
                """,
                unsafe_allow_html=True
            )
        orders = 0
        products = 0
        for order in range(3):
            with st.container(key = f"order-card-{orders+1}"):
                with st.container(key = f"order-header-{orders+1}"):
                    
                    st.markdown(
                        f"""
                        <div class = "orders-id-price-details">
                            <div>
                                <div class="order-id">Order ORD-2024-001</div>
                                <div class="order-date">Placed on 15/01/2024</div>
                            </div>
                            <div>
                                <div class="order-price">₹212,199</div>
                                <div class="status-badge">✓ Delivered</div>
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                    st.markdown(
                        f"""
                            <div class="tracking-info">
                                Tracking: TRK12345789
                            </div>
                        """,
                        unsafe_allow_html=True
                    )

                    for  order_item in range(3):
                        with st.container(key = f"product-item-{products+1}"):
                            with st.container(key = f"order-product-details-{products+1}"):
                                st.markdown(
                                    f"""
                                        <div class="product-image">
                                            <img src="https://images.unsplash.com/photo-1592750475338-74b7b21085ab?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80" alt="iPhone 15 Pro Max">
                                        </div>
                                    """,
                                    unsafe_allow_html=True
                                )

                                st.markdown(
                                    f"""
                                        <div class="product-details">
                                            <div class="product-name">iPhone 15 Pro Max</div>
                                            <div class="product-quantity">Qty: 1</div>
                                            <div class="product-price">₹134,999</div>
                                        </div>
                                    """,
                                    unsafe_allow_html=True
                                )

                            st.button(
                                label="view",
                                type="secondary",
                                key = f"view-button-{products+1}",
                                icon=":material/visibility:"
                            )

                            products += 1

                    orders += 1

order_page()