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
            --primary-light: #818cf8;
            --secondary: #f59e0b;
            --secondary-light: #fbbf24;
            --accent: #06d6a0;
            --accent-light: #34d399;
            --background: #fefefe;
            --card: #ffffff;
            --text-primary: #1a1a1a;
            --text-secondary: #6b7280;
            --text-muted: #9ca3af;
            --border: #e5e7eb;
            --border-light: #f3f4f6;
            --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            --shadow-lg: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
            --shadow-xl: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
            --radius: 16px;
            --radius-sm: 8px;
            --gradient-primary: linear-gradient(135deg, var(--primary), var(--primary-light));
            --gradient-secondary: linear-gradient(135deg, var(--secondary), var(--secondary-light));
            --gradient-accent: linear-gradient(135deg, var(--accent), var(--accent-light));
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #fafafa 0%, #f8fafc 100%);
            color: var(--text-primary);
            line-height: 1.7;
            overflow-x: hidden;
        }

        html {
            font-size: var(--font-size);
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
            box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1);
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

back_button_styles = """
        .st-key-back-button-section {
            display: flex;
            justify-content: space-between;
            padding: 1.5rem 2rem;
            max-width: 1400px;
            margin: 0 auto;
        }

        .st-key-back-button-container {
            display: flex;
            align-items:flex-start;
        }
        .st-key-back-button .stButton{
            min-width:fit-content;
            width:100%;
        }
        .st-key-back-button .stButton button {
            display: inline-flex;
            align-items: center;
            gap: 0.75rem;
            color: var(--text-secondary);
            background: transparent;
            border: 1px solid var(--border);
            font-size: 0.9rem;
            padding: 0.75rem 1.5rem;
            border-radius: var(--radius);
            transition: all 0.3s ease;
            cursor: pointer;
            font-weight: 500;
        }

        .st-key-back-button .stButton button:hover {
            color: var(--primary);
            background: rgba(99, 102, 241, 0.05);
            border-color: var(--primary);
            transform: translateX(-2px);
        }

        .st-key-back-button .stButton button span {
            font-size: 1.4rem;
            transition: transform 0.3s ease;
        }

        .st-key-back-button .stButton button p {
            margin: 0;
            font-weight: 500;
        }
"""

product_styles = """
        .st-key-product-container {
             display: flex;
            gap: 4rem;
            padding: 3rem;
            max-width: 1400px;
            margin: 0 auto;
            align-items: start;
            flex-direction:row;
            background: var(--card);
            border-radius: var(--radius);
            box-shadow: var(--shadow-lg);
            border: 1px solid var(--border-light);
            width:100%;
            flex-wrap:wrap;
        }

        .st-key-product-image-details {
            flex: 1;
            padding: 0;
        }

        .product-image {
            position: relative;
            overflow: hidden;
            border-radius: var(--radius);
        }

        .product-image img {
            width: 100%;
            height: auto;
            object-fit: cover;
            border-radius: var(--radius);
            transition: transform 0.5s ease;
            box-shadow: var(--shadow-xl);
        }

        .st-key-product-details {
            flex: 1.2;
            padding: 0;
        }

        .stVerticalBlock.st-key-product-deatils.st-emotion-cache-p6n0jw.e1msl4mp2{
            width:50%;
        }

        .st-key-product-name h1 {
            font-size: 3rem;
            font-weight: 800;
            margin-bottom: 1.5rem;
            color: var(--text-primary);
            letter-spacing: -0.02em;
            line-height: 1.1;
            background: linear-gradient(135deg, var(--text-primary), var(--text-secondary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        .st-key-price-section .st-emotion-cache-9fqyt2.e1fxfrsf0 {
            display: flex;
            justify-content: flex-start;
            align-items: center;
            gap: 1.5rem;
            margin-bottom: 3rem;
            flex-wrap: wrap;
            padding: 2rem;
        }

        .current-price span {
            font-size: 2.5rem;
            font-weight: 800;
            background: var(--gradient-primary);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            letter-spacing: -0.02em;
        }

        .original-price span {
            font-size: 1.3rem;
            color: var(--text-muted);
            text-decoration: line-through;
            font-weight: 500;
        }

        .discount-badge span {
            background: linear-gradient(135deg, #ef4444, #dc2626);
            color: white;
            padding: 0.5rem 1rem;
            border-radius: var(--radius-sm);
            font-size: 0.85rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            box-shadow: 0 4px 12px rgba(239, 68, 68, 0.3);
        }

        .tax-info {
            width: 100%;
            margin-top: 1rem;
        }

        .tax-info span {
            color: var(--accent);
            font-size: 0.95rem;
            font-weight: 600;
        }

        /* Features */
        .st-key-features {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 1rem;
            margin-bottom: 3rem;
        }

        .feature {
            display: flex;
            align-items: center;
            gap: 1rem;
            font-size: 0.85rem;
            padding: 1.5rem;
            border-radius: var(--radius);
            font-weight: 500;
            transition: all 0.3s ease;
            cursor: pointer;
            border: 1px solid transparent;
        }

        .feature:hover {
            transform: translateY(-2px);
            box-shadow: var(--shadow-lg);
        }

        .feature.delivery {
            background: linear-gradient(135deg, rgba(6, 214, 160, 0.1), rgba(52, 211, 153, 0.05));
            color: var(--accent);
            border-color: rgba(6, 214, 160, 0.2);
        }

        .feature.warranty {
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.1), rgba(129, 140, 248, 0.05));
            color: var(--primary);
            border-color: rgba(99, 102, 241, 0.2);
        }

        .feature.returns {
            background: linear-gradient(135deg, rgba(139, 92, 246, 0.1), rgba(167, 139, 250, 0.05));
            color: #8b5cf6;
            border-color: rgba(139, 92, 246, 0.2);
        }

        .feature-icon {
            width: 28px;
            height: 28px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.8rem;
            flex-shrink: 0;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        }

        .feature-icon.delivery {
            background: var(--gradient-accent);
            color: white;
        }

        .feature-icon.warranty {
            background: var(--gradient-primary);
            color: white;
        }

        .feature-icon.returns {
            background: linear-gradient(135deg, #8b5cf6, #a78bfa);
            color: white;
        }

        .st-key-action-buttons {
            display: flex;
            justify-content: space-between;
            align-items:center;
            flex-direction:row;
            gap: 1.5rem;
            margin-bottom: 3rem;

        }

        .st-key-add-to-cart, .st-key-buy-now {
            flex: 1;
        }

        .st-key-action-buttons .stButton {
            width: 100%;
        }

        .st-key-action-buttons .stButton button {
            width: 100%;
            padding: 1.25rem 2rem;
            border: none;
            border-radius: var(--radius);
            font-size: 1.1rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            position: relative;
            overflow: hidden;
        }

        .st-key-add-to-cart .stButton button {
            background: var(--gradient-primary);
            color: white;
            box-shadow: 0 8px 25px rgba(99, 102, 241, 0.3);
        }

        .st-key-add-to-cart .stButton button:hover {
            background: var(--primary-dark);
            box-shadow: 0 12px 30px rgba(99, 102, 241, 0.4);
        }

        .st-key-buy-now .stButton button {
            background: transparent;
            color: var(--secondary);
            border: 2px solid var(--secondary);
            box-shadow: 0 8px 25px rgba(245, 158, 11, 0.2);
        }

        .st-key-buy-now .stButton button:hover {
            background: var(--gradient-secondary);
            color: white;
            transform: translateY(-3px);
            box-shadow: 0 12px 30px rgba(245, 158, 11, 0.4);
        }

        .stButton button p {
            margin: 0;
        }

        .st-key-description {
            margin-top: 2rem;
            padding: 2rem 0 0 0;
            border-top: 1px solid var(--border-light);
        }

        .st-key-description h3 {
            font-size: 1.5rem;
            margin-bottom: 1rem;
            color: var(--text-primary);
            font-weight: 700;
            position: relative;
        }

        .description h3::after {
            content: '';
            position: absolute;
            bottom: -0.5rem;
            left: 0;
            width: 40px;
            height: 2px;
            background: var(--gradient-primary);
            border-radius: 2px;
        }

        .st-key-description p {
            color: var(--text-secondary);
            line-height: 1.8;
            font-size: 0.95rem;
            font-weight: 400;
        }
        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateY(-20px) scale(0.95);
            }
            to {
                opacity: 1;
                transform: translateY(0) scale(1);
            }
        }

"""

cart_button_styles = """
        .st-key-item-controls{
            display: flex;
            align-items: center;
            justify-content:space-around;
            flex-direction: row;
            width:50%;
        }
        .st-key-quantity-controls {
            display: flex;
            align-items: center;
            justify-content:center;
            flex-direction: row;
            gap: 0.5rem;
            background: rgba(99, 102, 241, 0.2);
            border-radius: 50px;
            padding: 0.25rem;
            width: fit-content;
            border:1px solid var(--border);
            width:100%;
        }

        .st-key-quantity-controls div[data-testid="stMarkdownContainer"]{
            margin-bottom:0rem;
        }

        .st-key-minus-btn .stButton button,
        .st-key-plus-btn .stButton button {
            display:flex;
            align-items:center;
            justify-content:center;
            width: 3.75rem;
            height: 3.75rem;
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

        .st-key-minus-btn .stButton button:hover,
        .st-key-plus-btn .stButton button:hover {
            background: var(--primary-dark);
        }

        .quantity-display {
            display:flex;
            align-items:center;
            justify-content:center;
            min-width: 100%;
            height:40px;
            text-align: center;
            border:none;
            font-weight: 600;
            font-size: 1rem;
            background-color: transparent;
            width: fit-content;
        }

"""

styles = f"""
<style>
    {remove_header_footer}
    {page_setup}
    {navbar_styles}
    {back_button_styles}
    {product_styles}
    {cart_button_styles}
</style>
"""
def apply_discount(price, discount):
    """Calculate discounted price"""
    discounted_price = int(price * ((100 - discount) / 100))
    return discounted_price

def make_price_string(price):
    """Format price with comma separator"""
    price_str = str(price)
    if len(price_str) > 3:
        return price_str[:-3] + "," + price_str[-3:]
    return price_str

product_details = {
    "name":"iPhone 15 Pro Max",
    "price":159999,
    "discount":16,
    "image":"https://images.unsplash.com/photo-1592750475338-74b7b21085ab?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80",
    "des":"""
        The iPhone 15 Pro Max represents the pinnacle of Apple's smartphone technology. Featuring the powerful A17 Pro chip, 
        an advanced camera system with 5x optical zoom, and a stunning titanium design, this device delivers unparalleled 
        performance and photography capabilities. With its 6.7-inch Super Retina XDR display and all-day battery life, 
        the iPhone 15 Pro Max is perfect for professionals and enthusiasts who demand the very best."""
}

def product_page():
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
                            icon=":material/shopping_cart:",
                            on_click=st.session_state["navigation"].to_cart_page
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
                            help=label
                        )

    with st.container(key = "back-button-section"):
        # back_button_col,empty_col = st.columns([1,9])
        # with back_button_col:
            with st.container(key = "back-button-container"):
                st.button(
                    label = "Back to Home",
                    key = "back-button",
                    type="tertiary",
                    icon=":material/arrow_back:",
                    on_click=st.session_state["navigation"].to_last_page
                )
        # with empty_col:
            # st.empty()
    
    with st.container(key = "product-container"):
        # product_image_col,product_detail_col = st.columns(2)
        # with product_image_col:
            with st.container(key = "product-image-details"):
                st.markdown(
                    f"""
                    <div class="product-image">
                        <img src={product_details['image']} alt="{product_details['name']}">
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        
        # with product_detail_col:
            with st.container(key = "product-deatils"):
                with st.container(key = "product-name"):
                    st.markdown(
                        f"""
                        <h1>{product_details["name"]}</h1>
                        """,
                        unsafe_allow_html=True
                    )
                
                with st.container(key = "price-section"):
                    st.markdown(
                        f"""
                        <div class="current-price">
                            <span>₹{make_price_string(apply_discount(product_details['price'],product_details['discount']))}</span>
                        </div>
                        <div class="original-price">
                            <span>₹{make_price_string(product_details["price"])}</span>
                        </div>
                        <div class="discount-badge">
                            <span>16% OFF</span>
                        </div>
                        <div class="tax-info"><span>Inclusive of all taxes</span></div>
                        """,
                        unsafe_allow_html=True
                    )
                
                with st.container(key = "features"):
                    st.markdown(
                        """
                        <div class="feature delivery">
                            <div class="feature-icon delivery">
                                <svg width="12" height="12" fill="currentColor" viewBox="0 0 24 24">
                                    <path d="M19 7C19 6.45 18.55 6 18 6H14L12 4H8C7.45 4 7 4.45 7 5V7H5C4.45 7 4 7.45 4 8V17C4 18.1 4.9 19 6 19H18C19.1 19 20 18.1 20 17V8C20 7.45 19.55 7 19 7ZM18 17H6V9H18V17ZM8 11H16V13H8V11Z"/>
                                </svg>
                            </div>
                            <span>Free Delivery</span>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                    st.markdown(
                        """
                        <div class="feature warranty">
                            <div class="feature-icon warranty">
                                <svg width="12" height="12" fill="currentColor" viewBox="0 0 24 24">
                                    <path d="M12,1L3,5V11C3,16.55 6.84,21.74 12,23C17.16,21.74 21,16.55 21,11V5L12,1ZM19,11C19,15.52 16.02,19.69 12,20.9C7.98,19.69 5,15.52 5,11V6.3L12,3.19L19,6.3V11ZM7,10L12,15L17,10L15.59,8.59L12,12.17L8.41,8.59L7,10Z"/>
                                </svg>
                            </div>
                            <span>1 Year Warranty</span>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                    st.markdown(
                        """
                        <div class="feature returns">
                            <div class="feature-icon returns">
                                <svg width="12" height="12" fill="currentColor" viewBox="0 0 24 24">
                                    <path d="M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2ZM18,11H13L14.5,9.5C14.5,9.5 14.5,9.5 14.5,9.5L13.08,8.08L9.16,12L13.08,15.92L14.5,14.5L13,13H18V11Z"/>
                                </svg>
                            </div>
                            <span>Easy Returns</span>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                with st.container(key = "action-buttons"):
                    qty = 0
                    # cart_col,order_col = st.columns(2)
                    # with cart_col:
                    if(qty <= 0):
                        st.button(
                            label="Add to Cart",
                            key="add-to-cart",
                            type="secondary"
                        )
                    else:
                        with st.container(key = f"item-controls"):
                            with st.container(key = f"quantity-controls"):
                                st.button(
                                    type="tertiary",
                                    label="",
                                    icon=":material/remove:",
                                    key=f"minus-btn",
                                )
                                st.markdown(
                                    f"""
                                    <div class = "quantity-display">{qty}</div>
                                    """,
                                    unsafe_allow_html=True
                                )
                                st.button(
                                    type="tertiary",
                                    label="",
                                    icon=":material/add:",
                                    key=f"plus-btn",
                                )

                    # with order_col:
                    st.button(
                        label="Buy Now",
                        key=f"buy-now",
                        type="secondary"
                    )  

                with st.container(key = "description"):
                    st.markdown(
                        """<h3>Product Description</h3>""",
                        unsafe_allow_html=True
                    )
                    st.markdown(
                        f"""
                        <p>
                        {product_details["des"]}
                        </p>
                        """,
                        unsafe_allow_html=True
                    )      
