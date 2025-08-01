import streamlit as st


main_styles = """
        /* Hide Streamlit default elements */
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}

        /* Hide the orange loading progress bar */
        div[data-testid="stDecoration"] {
            display: none !important;
        }

        /* Remove top padding to avoid white space */
        .block-container {
            padding-top: 0rem !important;
        }

        /* CSS Variables for consistent theming */
        :root {
            --font-size: 14px;
            --background: #fefefe;
            --foreground: #1a1a1a;
            --card: #ffffff;
            --card-foreground: #1a1a1a;
            --popover: #ffffff;
            --popover-foreground: #1a1a1a;
            --primary: #6366f1;
            --primary-foreground: #ffffff;
            --secondary: #f59e0b;
            --secondary-foreground: #ffffff;
            --muted: #f8fafc;
            --muted-foreground: #6b7280;
            --accent: #06d6a0;
            --accent-foreground: #ffffff;
            --destructive: #ef4444;
            --destructive-foreground: #ffffff;
            --border: rgba(99, 102, 241, 0.12);
            --input: transparent;
            --input-background: #f8fafc;
            --switch-background: #e5e7eb;
            --font-weight-medium: 500;
            --font-weight-normal: 400;
            --ring: #6366f1;
            --chart-1: #6366f1;
            --chart-2: #f59e0b;
            --chart-3: #06d6a0;
            --chart-4: #f97316;
            --chart-5: #ef4444;
            --radius: 0.75rem;
            --sidebar: #fafafa;
            --sidebar-foreground: #1a1a1a;
            --sidebar-primary: #6366f1;
            --sidebar-primary-foreground: #ffffff;
            --sidebar-accent: #f8fafc;
            --sidebar-accent-foreground: #374151;
            --sidebar-border: #e5e7eb;
            --sidebar-ring: #6366f1;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        html {
            font-size: var(--font-size);
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: white;
            color: #1a1a1a;
            line-height: 1.6;
            overflow-x: hidden;
        }

        .stMain .stMainBlockContainer{
            padding: 0;
        }

        .stMainBlockContainer .stVerticalBlock{
            row-gap:0;
            column-gap:1rem;
        }

        /* HEADER STYLES */
        .st-key-header {
            padding: 1.5rem 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: transparent;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
            position: relative;
            z-index: 100;
        }

        .logo {
            font-size: 2.5rem;
            font-weight: 700;
            color: var(--primary);
            text-decoration: none;
            animation: logoFloat 3s ease-in-out infinite;
        }

        @keyframes logoFloat {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-5px); }
        }

        /* Navigation buttons container */
        .st-key-nav-buttons {
            display: flex;
            gap: 1rem;
            align-items: center;
            justify-content: flex-end;
            margin-left: auto;
        }

        .st-key-nav-buttons .stHorizontalBlock {
            gap: 1rem !important;
            justify-content: flex-end !important;
            margin-left: auto;
        }

        .st-key-nav-buttons .stColumn {
            flex: 0 0 auto !important;
            width: auto !important;
            min-width: auto !important;
            padding: 0 !important;
        }

        .st-key-nav-buttons .stButton {
            margin: 0 !important;
        }

        .st-key-nav-buttons .stButton button {
            padding: 0.75rem 1.5rem;
            border: none;
            border-radius: var(--radius);
            font-weight: var(--font-weight-medium);
            cursor: pointer;
            transition: all 0.3s ease;
            font-size: 1rem;
            min-width: 80px;
        }

        /* Login button styling */
        .st-key-login-button .stButton button {
            background: transparent !important;
            color: var(--foreground) !important;
            border: 1px solid transparent !important;
        }

        .st-key-login-button .stButton button:hover {
            color: var(--primary) !important;
            transform: translateY(-2px);
        }

        /* Sign in button styling */
        .st-key-sign-in-button .stButton button {
            background: linear-gradient(135deg, var(--primary), #8b5cf6) !important;
            color: var(--primary-foreground) !important;
            box-shadow: 0 4px 15px rgba(99, 102, 241, 0.25);
            border: none !important;
        }

        .st-key-sign-in-button .stButton button:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(99, 102, 241, 0.35);
        }

        /* HERO SECTION STYLES */
        .st-key-hero {
            min-height: 80vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            padding: 4rem 2rem;
            position: relative;
            background: linear-gradient(
                135deg,
                rgba(99, 102, 241, 0.15) 0%,       /* Soft Indigo */
                rgba(245, 158, 11, 0.12) 35%,      /* Warm Amber */
                rgba(6, 214, 160, 0.14) 70%,       /* Fresh Mint */
                rgba(99, 102, 241, 0.10) 100%      /* Return to Indigo */
                );
        }

        .st-key-hero-content {
            position: relative;
            z-index: 10;
            max-width: 800px;
            width: 100%;
        }

        .st-key-hero h1 {
            font-size: 4rem;
            font-weight: 700;
            margin-bottom: 1rem;
            opacity: 0;
            animation: slideInUp 1s ease-out 0.2s forwards;
        }

        .st-key-hero h1 .looto-text {
            background: linear-gradient(135deg, var(--primary), var(--secondary), var(--accent), #8b5cf6);
            background-size: 300% 300%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: gradientShift 4s ease-in-out infinite;
        }

        @keyframes gradientShift {
            0%, 100% { background-position: 0% 50%; }
            25% { background-position: 100% 50%; }
            50% { background-position: 50% 100%; }
            75% { background-position: 50% 0%; }
        }

        .st-key-hero .tagline {
            font-size: 2rem;
            color: var(--secondary);
            margin-bottom: 1.5rem;
            font-weight: var(--font-weight-medium);
            opacity: 1;
            font-family: 'Courier New', monospace;
        }

        .typewriter {
            display: inline-block;
            overflow: hidden;
            white-space: nowrap;
            animation: typewriter 5s steps(19, end) 0.5s infinite, 
                       blink 0.8s step-end infinite;
            width: 0;
            border-right: 3px solid var(--secondary);
        }

        @keyframes typewriter {
            0%, 20% {
                width: 0;
            }
            60%, 80% {
                width: 21ch;
            }
            100% {
                width: 0;
            }
        }

        @keyframes blink {
            0%, 50% {
                border-color: var(--secondary);
            }
            51%, 100% {
                border-color: transparent;
            }
        }

        .hero-description {
            font-size: 1.25rem;
            color: var(--muted-foreground);
            margin-bottom: 3rem;
            line-height: 1.7;
            opacity: 0;
            animation: slideInUp 1s ease-out 0.6s forwards;
        }

        /* Hero Buttons Container - Perfect centering */
        .st-key-hero-buttons {
            display: flex !important;
            justify-content: center;
            align-items: center;
            opacity: 0;
            animation: slideInUp 1s ease-out 0.8s forwards;
            width: 100%;
        }

        .st-key-hero-buttons .stHorizontalBlock {
            justify-content: center !important;
            align-items: center !important;
            gap: 1rem !important;
            width: 100% !important;
        }

        .st-key-hero-buttons .stColumn {
            flex: 0 0 auto !important;
            width: auto !important;
            min-width: auto !important;
            padding: 0 0.5rem !important;
            margin: 0 !important;
        }

        .st-key-hero-buttons .stButton {
            margin: 0 !important;
            width: 100% !important;
        }

        .st-key-hero-buttons .stButton button {
            padding: 1rem 2rem;
            font-size: 1.1rem;
            border-radius: calc(var(--radius) + 4px);
            border: none;
            cursor: pointer;
            transition: all 0.3s ease;
            font-weight: var(--font-weight-medium);
            min-width: 160px;
            white-space: nowrap;
            width: 100%;
            height:60px;
            min-height:fit-content;
        }

        /* Shop Now Button - Primary style */
        .st-key-shop-now-button .stButton button {
            background: linear-gradient(135deg, var(--primary), #8b5cf6) !important;
            color: var(--primary-foreground) !important;
            box-shadow: 0 4px 15px rgba(99, 102, 241, 0.25);
            border: none !important;
        }

        .st-key-shop-now-button .stButton button:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(99, 102, 241, 0.35);
        }

        /* Browse Categories Button - Outline style */
        .st-key-browse-categories-button .stButton button {
            background: transparent !important;
            color: var(--primary) !important;
            border: 2px solid var(--primary) !important;
        }

        .st-key-browse-categories-button .stButton button:hover {
            background: var(--primary) !important;
            color: var(--primary-foreground) !important;
            transform: translateY(-3px);
        }

        /* FEATURES SECTION */
        .st-key-features {
            padding: 6rem 2rem;
            background: var(--muted);
        }

        .st-key-features-container {
            max-width: 1200px;
            margin: 0 auto;
        }

        .st-key-features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin-top: 3rem;
        }

        .feature-card {
            background: var(--card);
            padding: 2.5rem;
            border-radius: calc(var(--radius) + 4px);
            text-align: center;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
            transition: all 0.4s ease;
            position: relative;
            overflow: hidden;
            opacity: 0;
            transform: translateY(30px);
            animation: fadeInUp 0.8s ease-out forwards;
        }

        .feature-card:nth-child(1) {
            animation-delay: 0.2s;
            border: 2px solid rgba(99, 102, 241, 0.15);
        }

        .feature-card:nth-child(2) {
            animation-delay: 0.4s;
            border: 2px solid rgba(245, 158, 11, 0.15);
        }

        .feature-card:nth-child(3) {
            animation-delay: 0.6s;
            border: 2px solid rgba(6, 214, 160, 0.15);
        }

        .feature-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, 
                transparent, 
                rgba(255, 255, 255, 0.4), 
                transparent);
            transition: left 0.6s ease;
        }

        .feature-card:hover::before {
            left: 100%;
        }

        .feature-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
        }

        .feature-icon {
            width: 60px;
            height: 60px;
            border-radius: 50%;
            margin: 0 auto 1.5rem;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
            animation: iconBounce 2s ease-in-out infinite;
        }

        .feature-card:nth-child(1) .feature-icon {
            background: linear-gradient(135deg, var(--primary), #8b5cf6);
            color: white;
            animation-delay: 0s;
        }

        .feature-card:nth-child(2) .feature-icon {
            background: linear-gradient(135deg, var(--secondary), #fb923c);
            color: white;
            animation-delay: 0.3s;
        }

        .feature-card:nth-child(3) .feature-icon {
            background: linear-gradient(135deg, var(--accent), #34d399);
            color: white;
            animation-delay: 0.6s;
        }

        @keyframes iconBounce {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-8px); }
        }

        @keyframes fadeInUp {
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .feature-card h3 {
            font-size: 1.5rem;
            font-weight: var(--font-weight-medium);
            margin-bottom: 1rem;
            color: var(--card-foreground);
        }

        .feature-card:nth-child(1) h3 { color: var(--primary); }
        .feature-card:nth-child(2) h3 { color: var(--secondary); }
        .feature-card:nth-child(3) h3 { color: var(--accent); }

        .feature-card p {
            color: var(--muted-foreground);
            line-height: 1.6;
        }

        /* FOOTER STYLES */
        .st-key-footer {
            background: var(--card);
            padding: 4rem 2rem 2rem;
            border-top: 1px solid var(--border);
        }

        .st-key-footer-container {
            max-width: 1200px;
            margin: 0 auto;
        }

        .st-key-footer-grid {
            display: grid;
            grid-template-columns: 2fr 1fr 1fr 1fr;
            gap: 3rem;
            margin-bottom: 3rem;
        }

        .footer-section h4 {
            font-size: 1.2rem;
            font-weight: var(--font-weight-medium);
            margin-bottom: 1.5rem;
        }

        .footer-section:nth-child(1) h4 { color: var(--primary); }
        .footer-section:nth-child(2) h4 { color: var(--secondary); }
        .footer-section:nth-child(3) h4 { color: var(--accent); }
        .footer-section:nth-child(4) h4 { color: var(--primary); }

        .footer-section ul {
            list-style: none;
        }

        .footer-section ul li {
            margin-bottom: 0.75rem;
        }

        .footer-section a {
            color: var(--muted-foreground);
            text-decoration: none;
            transition: color 0.3s ease;
        }

        .footer-section a:hover {
            color: var(--primary);
        }

        .footer-bottom {
            text-align: center;
            padding-top: 2rem;
            border-top: 1px solid var(--border);
            color: var(--muted-foreground);
        }

        .footer-bottom a {
            color: var(--primary);
            text-decoration: none;
        }

        @keyframes slideInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            .st-key-hero h1 {
                font-size: 2.5rem;
            }

            .tagline {
                font-size: 1.2rem;
            }

            .hero-description {
                font-size: 1.1rem;
            }

            .st-key-hero-buttons .stHorizontalBlock {
                flex-direction: column;
                gap: 0.75rem !important;
            }

            .st-key-hero-buttons .stColumn {
                width: 100% !important;
                padding: 0 !important;
            }

            .st-key-hero-buttons .stButton button {
                min-width: 200px;
            }

            .st-key-footer-grid {
                grid-template-columns: 1fr;
                gap: 2rem;
            }

            .st-key-nav-buttons .stHorizontalBlock {
                flex-direction: column;
                gap: 0.5rem !important;
            }
        }
"""

styles = f"""
    <style>
        {main_styles}
    </style>
"""


def landing_page():
    st.set_page_config(
        page_title="Looto - Your Trusted Shopping Destination",
        page_icon="🛍️",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    st.markdown(styles,unsafe_allow_html=True)

    with st.container(key = "header"):
        logo_col,button_col = st.columns([3,1],gap="small")
        with logo_col:
            st.markdown("""<div class="logo">Looto</div>""",unsafe_allow_html=True)
        with button_col:
            with st.container(key = "nav-buttons"):
                login_col,signin_col = st.columns(2,gap=None)
                
                with login_col:
                    st.button(
                        label="Login",
                        key = "login-button",
                        type="tertiary"
                    )
                with signin_col:
                    st.button(
                        label="Sign in",
                        key = "sign-in-button",
                        type="secondary",
                        on_click=st.session_state["navigation"].to_signup_page
                    )

    with st.container(key = "main"):
        with st.container(key = "hero"):
            with st.container(key = "hero-content"):
                st.markdown("""
                    <h1>Welcome to <span class="looto-text">Looto</span></h1>
                    <p class="tagline">
                        <span class="typewriter">Ab nahi Loge tho kab</span>
                    </p>
                    <p class="hero-description">
                        Discover amazing products and unbeatable deals. Your shopping journey starts here.
                    </p>
                """,unsafe_allow_html=True)
                with st.container(key = "hero-buttons"):
                    shop_now_col,browse_categories_col = st.columns(2,gap=None)
                    with shop_now_col:
                        st.button(
                            label="Shop Now",
                            key = "shop-now-button",
                            type="secondary"
                        )
                    with browse_categories_col:
                        st.button(
                            label="Browse Categories",
                            key = "browse-categories-button",
                            type= "tertiary"
                        )
        
        with st.container(key = "features"):
            with st.container(key = "features-container"):
                with st.container(key = "features-grid"):
                    st.markdown(
                        """
                        <div class="feature-card">
                            <div class="feature-icon">●</div>
                            <h3>Quality Products</h3>
                            <p>Curated selection of premium items at the best prices</p>
                        </div>""",
                        unsafe_allow_html=True
                    )
                    st.markdown(
                        """
                        <div class="feature-card">
                            <div class="feature-icon">●</div>
                            <h3>Fast Delivery</h3>
                            <p>Quick and reliable shipping to your doorstep</p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                    st.markdown(
                        """
                        <div class="feature-card">
                            <div class="feature-icon">●</div>
                            <h3>Easy Returns</h3>
                            <p>Hassle-free returns and exchanges within 30 days</p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

    with st.container(key = "footer"):
        with st.container(key = "footer-container"):
            with st.container(key = "footer-grid"):
                st.markdown(
                    """
                    <div class="footer-section">
                        <h4>Looto</h4>
                        <p>Your trusted shopping destination for quality products and great deals.</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown(
                    """
                    <div class="footer-section">
                        <h4>Shop</h4>
                        <ul>
                            <li><a href="#">All Products</a></li>
                            <li><a href="#">Categories</a></li>
                            <li><a href="#">New Arrivals</a></li>
                            <li><a href="#">Sale</a></li>
                        </ul>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown(
                    """
                    <div class="footer-section">
                        <h4>Support</h4>
                        <ul>
                            <li><a href="#">Help Center</a></li>
                            <li><a href="#">Contact Us</a></li>
                            <li><a href="#">Returns</a></li>
                            <li><a href="#">Shipping</a></li>
                        </ul>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown(
                    """
                    <div class="footer-section">
                        <h4>Company</h4>
                        <ul>
                            <li><a href="#">About</a></li>
                            <li><a href="#">Careers</a></li>
                            <li><a href="#">Privacy</a></li>
                            <li><a href="#">Terms</a></li>
                        </ul>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            st.markdown(
                """
                <div class="footer-bottom">
                    <p>© 2025 <a href="#">Looto</a>. All rights reserved.</p>
                </div>
                """,
                unsafe_allow_html=True
            )       

