import streamlit as st

def check_user_exist():
    if(not(st.session_state["current_user"].user_exist)):
        st.session_state["navigation"].to_signup_page

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
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

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

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            background: var(--background);
            color: var(--text-primary);
            line-height: 1.6;
        }

        html {
            font-size: var(--font-size);
        }
        

            /* Main Streamlit App Container */
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

category_bar_styles = """
        .st-key-category-bar {
            background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
            padding: 1.5rem 0;
            border-bottom: 1px solid var(--border);
        }

        .st-key-category-container {
            margin: 0 auto;
            padding: 0 2rem;
            width: 100%;
            min-width: fit-content;
        }

        .st-key-categories {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
            gap: 1.125rem;
            
        }

        [class *= "st-key-category-btn-"]{
            display: flex;
            margin:0;
        }

        .st-key-categories .stButton {
            width: 100%;
        }

        .st-key-categories .stButton button {
            width: 100%;
            padding: 1rem 0.5rem;
            background: white;
            border: 1px solid var(--border);
            border-radius: var(--radius);
            cursor: pointer;
            transition: all 0.3s ease;
            text-align: center;
            font-weight: 500;
            font-size: 0.9rem;
            color: var(--text-primary);
            box-shadow: var(--shadow);
        }

        .st-key-categories .stButton button:hover {
            background: var(--primary);
            color: white;
            transform: translateY(-3px);
            box-shadow: var(--shadow-lg);
        }

        .st-key-categories .stButton button p {
            margin: 0;
        }

"""

feature_section_styles = """
        .st-key-featured-section {
            background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%);
            color: white;
            padding: 4rem 0;
            margin: 4rem 0;
        }

        .st-key-featured-content {
            max-width: 1400px;
            margin: 0 auto;
            padding: 0 2rem;
            text-align: center;
        }

        .featured-title {
            font-size: 3rem;
            font-weight: 800;
            margin-bottom: 1rem;
        }

        .featured-subtitle {
            font-size: 1.2rem;
            opacity: 0.9;
            margin-bottom: 2rem;
        }


"""

product_styles = """
        .st-key-products-section {
            max-width: 1400px;
            margin: 0 auto;
            padding: 3rem 2rem;
            width: 100%;
        }

        .section-title {
            font-size: 2.5rem;
            font-weight: 700;
            text-align: center;
            margin-bottom: 3rem;
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .st-key-products-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(315px, 1fr));
            gap: 2rem;
            margin-bottom: 3rem;
        }

        [class *= "st-key-product-card-"]{
            background: white;
            border-radius: var(--radius);
            overflow: hidden;
            box-shadow: var(--shadow);
            transition: all 0.3s ease;
            border: 1px solid var(--border);
            position: relative;
        }

        [class *= "st-key-product-card-"]:hover{
            transform: translateY(-8px);
            box-shadow: var(--shadow-lg);
        }

        [class *= "product-image-details-"]{
            position: relative;
        }

        .product-image {
            width: 100%;
            height: 220px;
            background: linear-gradient(135deg, #f8fafc, #e2e8f0);
            position: relative;
            overflow: hidden;
        }

        .product-image img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.3s ease;
        }

        [class *= "st-key-product-card-"]:hover .product-image img{
            transform: scale(1.05);
        }

        .product-image::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
            transition: left 0.6s ease;
            z-index: 1;
        }

        [class *= "st-key-product-card-"]:hover .product-image::before{
            left: 100%;
        }

        [class *= "st-key-product-info-"]{
            padding: 1.5rem;
        }

        [class *= "st-key-product-details-"]{
            margin-bottom: 1rem;
        }

        .product-title {
            font-size: 1.2rem;
            font-weight: 600;
            margin-bottom: 0.5rem;
            color: var(--text-primary);
        }

        .product-description {
            color: var(--text-secondary);
            font-size: 0.9rem;
            margin-bottom: 1rem;
            line-height: 1.5;
        }

        .product-price {
            font-size: 1.5rem;
            font-weight: 700;
            color: var(--primary);
            margin-bottom: 1rem;
        }

        [class *= "st-key-view-product-btn-"]{
            width: 100%;
            margin-bottom: 0.75rem;
        }

        [class *= "st-key-view-product-btn-"] .stButton{
            width: 100%;
        }

        [class *= "st-key-view-product-btn-"] .stButton button{
            width: 100%;
            padding: 0.75rem;
            background: transparent;
            color: var(--primary);
            border: 2px solid var(--primary);
            border-radius: calc(var(--radius) - 4px);
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        [class *= "st-key-view-product-btn-"] .stButton button:hover{
            background: var(--primary);
            color: white;
            transform: translateY(-2px);
        }

        [class *= "st-key-view-product-btn-"] .stButton button p{
            margin: 0;
        }

        [class *= "st-key-action-buttons-"]{
            display: flex;
            gap: 1rem;
        }

        [class *= "st-key-add-to-cart-"],[class *= "st-key-buy-now-"]{
            flex: 1;
        }

        [class *= "st-key-add-to-cart-"] .stButton,
        [class *= "st-key-buy-now-"] .stButton{
            width: 100%;
        }

        [class *= "st-key-add-to-cart-"] .stButton button {
            width: 100%;
            padding: 0.75rem;
            border: none;
            border-radius: calc(var(--radius) - 4px);
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            font-size: 0.9rem;
            background: linear-gradient(135deg, var(--primary), var(--primary-dark));
            color: white;
        }

        [class *= "st-key-add-to-cart-"] .stButton button:hover {
            background: linear-gradient(135deg, var(--primary-dark), #3730a3);
            transform: translateY(-2px);
        }

        [class *= "st-key-buy-now-"] .stButton button{
            width: 100%;
            padding: 0.75rem;
            border: none;
            border-radius: calc(var(--radius) - 4px);
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            font-size: 0.9rem;
            background: linear-gradient(135deg, var(--secondary), #d97706);
            color: white;
        }

        [class *= "st-key-buy-now-"] .stButton button:hover{
            background: linear-gradient(135deg, #d97706, #b45309);
            transform: translateY(-2px);
        }

        [class *= "st-key-add-to-cart-"] .stButton button p,[class *= "st-key-buy-now-"] .stButton button p{
            margin: 0;
        }

        .badge {
            position: absolute;
            top: 1rem;
            right: 1rem;
            background: var(--secondary);
            color: white;
            padding: 0.25rem 0.75rem;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 600;
            z-index: 2;
        }
"""

responsive_styles = """
        @media (max-width: 1024px) {
            .st-key-categories {
                grid-template-columns: repeat(5, 1fr);
                gap: 0.75rem;
            }
            
            .st-key-categories .stButton button {
                padding: 0.75rem 0.25rem;
                font-size: 0.8rem;
            }
        }

        @media (max-width: 768px) {
            .st-key-nav-container {
                flex-direction: column;
                gap: 1rem;
                padding: 0 1rem;
            }

            .st-key-search-container {
                order: 3;
                width: 100%;
            }

            .st-key-nav-buttons {
                order: 2;
                flex-wrap: wrap;
                justify-content: center;
            }

            .st-key-categories {
                grid-template-columns: repeat(2, 1fr);
            }

            .st-key-products-grid {
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 1.5rem;
            }

            .featured-title {
                font-size: 2rem;
            }
        }

        @media (max-width: 480px) {
            .st-key-products-grid {
                grid-template-columns: 1fr;
            }
            
            .st-key-nav-buttons .stButton button {
                padding: 0.5rem 1rem;
                font-size: 0.9rem;
            }
        }

        /* Animations */
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        [class *= "st-key-product-card-"]{
            animation: fadeInUp 0.6s ease forwards;
        }

        .st-key-product-card-1 { animation-delay: 0.1s; }
        .st-key-product-card-2 { animation-delay: 0.2s; }
        .st-key-product-card-3 { animation-delay: 0.3s; }
        .st-key-product-card-4 { animation-delay: 0.4s; }
        .st-key-product-card-5 { animation-delay: 0.5s; }
        .st-key-product-card-6 { animation-delay: 0.6s; }
        .st-key-product-card-7 { animation-delay: 0.7s; }
        .st-key-product-card-8 { animation-delay: 0.8s; }

"""

styles = f"""
    <style>
    {remove_header_footer}
    {page_setup}
    {navbar_styles}
    {category_bar_styles}
    {feature_section_styles}
    {product_styles}
    {responsive_styles}
    </style>
"""

def home_page():
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
                        label = ((st.session_state["current_user"].name).split(" "))[0] if(st.session_state["current_user"].user_exist) else "Login/Signup"
                        st.button(
                            label=label,
                            key = "nav-btn-3",
                            type="secondary",
                            icon=":material/person:",
                            on_click=check_user_exist,
                            help=label
                        )

    with st.container(key = "category-bar"):
        with st.container(key = "category-container"):
            cat_list = [
                "Electronics",
                "Fashion",
                "Home & Garden",
                "Sports",
                "Books",
                "Beauty",
                "Automotive",
                "Toys",
                "Health",
                "Grocer"
            ]
            with st.container(key = "categories"):
                for cat_item in range(len(cat_list)):
                    st.button(
                        label=cat_list[cat_item],
                        key = f"category-btn-{cat_item+1}",
                        type="secondary"
                    )

    with st.container(key = "featured-section"):
        with st.container(key = "featured-content"):
            st.markdown(
                """
                <h2 class="featured-title">Big Sale Today!</h2>
                <p class="featured-subtitle">Up to 70% off on selected items. Limited time offer!</p>
                """,
                unsafe_allow_html=True
            )
            # st.button(
            #     label = "Shop Now",
            #     key = "featured-btn",
            #     type="secondary"
            # )

    with st.container(key = "products-section"):
        st.markdown(
            """
            <h2 class="section-title">Featured Products</h2>
            """,
            unsafe_allow_html=True
        )

        with st.container(key = "products-grid"):
            for product in range(12):
                qty = 0
                with st.container(key = f"product-card-{product+1}"):
                    with st.container(key = f"product-image-details-{product+1}"):
                        st.markdown(
                            """
                            <div class="product-image">
                                <img src="https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=400&h=300&fit=crop" alt="Products">
                            </div>
                            <div class="badge">Hot</div>
                            """,
                            unsafe_allow_html=True
                        )
                    with st.container(key = f"product-info-{product+1}"):
                        with st.container(key = f"product-details-{product+1}"):
                            st.markdown(
                                """
                                <h3 class="product-title">Premium Laptop</h3>
                                <p class="product-description">High-performance laptop with latest specs for work and gaming</p>
                                <div class="product-price">$899.99</div>
                                """,unsafe_allow_html=True
                            )
                        st.button(
                            label="View Product",
                            key=f"st-key-view-product-btn-{product+1}",
                            type="secondary"
                        )
                        with st.container(key = f"action-buttons-{product+1}"):
                            add_to_cart_col,buy_now_col = st.columns(2)
                            with add_to_cart_col:
                                if(qty <= 0):
                                    st.button(
                                        label="Add to Cart",
                                        key=f"add-to-cart-{product+1}",
                                        type="secondary"
                                    )
                                else:
                                    with st.container(key = f"quantity-controls-{product+1}"):
                                        dec_col, qty_col, inc_col = st.columns([0.5, 1, 0.5])
                                        with dec_col:
                                            st.button(
                                                type="tertiary",
                                                label="-",
                                                # icon=":material/remove:",
                                                key=f"minus-btn-{product+1}",
                                            )
                                        with qty_col:
                                            st.markdown(
                                                f"""
                                                <input type="text" class="quantity-display" value="{qty}" readonly>
                                                """,
                                                unsafe_allow_html=True
                                            )
                                        with inc_col:
                                            st.button(
                                                type="tertiary",
                                                label="+",
                                                # icon=":material/add:",
                                                key=f"plus-btn-{product+1}",
                                            )

                            with buy_now_col:
                                st.button(
                                    label="Buy Now",
                                    key=f"buy-now-{product+1}",
                                    type="secondary"
                                )
                                



