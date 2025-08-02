import streamlit as st
import os 
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from services.auth_service import ValidateUser

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


other_styles = """
/* =============================================================================
   ENHANCED CSS STYLES FOR STREAMLIT SIGNUP PAGE - VERSATILE VERSION
   ============================================================================= */


/* ===== CSS CUSTOM PROPERTIES (CSS Variables) ===== */
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
    --radius: 0.75rem;
    --shadow-sm: 0 2px 4px rgba(0, 0, 0, 0.05);
    --shadow-md: 0 4px 12px rgba(0, 0, 0, 0.1);
    --shadow-lg: 0 8px 25px rgba(0, 0, 0, 0.15);
    --shadow-xl: 0 20px 40px rgba(0, 0, 0, 0.1);
}


/* ===== BODY AND MAIN CONTAINER STYLING ===== */
body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif !important;
    background: linear-gradient(135deg, 
        rgba(99, 102, 241, 0.08) 0%, 
        rgba(245, 158, 11, 0.06) 35%, 
        rgba(6, 214, 160, 0.08) 70%, 
        rgba(99, 102, 241, 0.05) 100%) !important;
    color: var(--foreground) !important;
    line-height: 1.6 !important;
    margin: 0 !important;
    padding: 0 !important;
    overflow-x: hidden !important;
    min-height: 100vh !important;
}


/* Main Streamlit app container - enable scrolling */
.stApp {
    background: transparent !important;
    min-height: 100vh !important;
    overflow-y: auto !important;
    display: flex !important;
    flex-direction: column !important;
}


/* App view container - allow natural flow */
.stAppViewContainer {
    background: transparent !important;
    padding: 0 !important;
    min-height: 100vh !important;
    flex: 1 !important;
}


/* Main block container - remove fixed positioning constraints */
.stMainBlockContainer {
    background: transparent !important;
    padding: 0 !important;
    max-width: none !important;
    width: 100% !important;
    flex: 1 !important;
    display: flex !important;
    flex-direction: column !important;
}

.stMain .stMainBlockContainer{
    padding: 0;
}

.stMainBlockContainer .stVerticalBlock{
    row-gap:0;
    column-gap:1rem;
}


/* ===== HEADER STYLING (st-key-header) ===== */
.st-key-header {
    background: rgba(255, 255, 255, 0.95) !important;
    backdrop-filter: blur(10px) !important;
    border-bottom: 1px solid var(--border) !important;
    padding: 1rem 2rem !important;
    margin: 0 !important;
    position: sticky !important;
    top: 0 !important;
    z-index: 100 !important;
    animation: slideInDown 0.6s ease-out !important;
    box-shadow: var(--shadow-sm) !important;
}


@keyframes slideInDown {
    from {
        opacity: 0;
        transform: translateY(-20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}


/* Header horizontal layout */
.st-key-header .stHorizontalBlock {
    display: flex !important;
    justify-content: space-between !important;
    align-items: center !important;
    max-width: 1400px !important;
    margin: 0 auto !important;
    width: 100% !important;
}


/* ===== LOGO STYLING ===== */
.logo {
    font-size: clamp(1.5rem, 4vw, 2.2rem) !important;
    font-weight: 700 !important;
    color: var(--primary) !important;
    text-decoration: none !important;
    animation: logoFloat 3s ease-in-out infinite !important;
    letter-spacing: -0.02em !important;
}


@keyframes logoFloat {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-3px); }
}


/* ===== BACK BUTTON STYLING ===== */
.st-key-back-btn{
    display: flex;
    gap: 1rem;
    align-items: flex-end;
    justify-content: flex-end;
    margin-left: auto;
}


.st-key-back-btn .stHorizontalBlock{
    gap: 1rem !important;
    justify-content: flex-end !important;
    margin-left: auto;
}


.st-key-back-btn .stColumn {
    flex: 0 0 auto !important;
    width: auto !important;
    min-width: auto !important;
    padding: 0 !important;
}


.st-key-back-button .stButton button {
    background: rgba(99, 102, 241, 0.08) !important;
    border: 1px solid rgba(99, 102, 241, 0.15) !important;
    color: var(--primary) !important;
    cursor: pointer !important;
    padding: 0.625rem 1.25rem !important;
    border-radius: var(--radius) !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    display: flex !important;
    align-items: center !important;
    font-weight: var(--font-weight-medium) !important;
    font-size: 0.95rem !important;
    box-shadow: var(--shadow-sm) !important;
}


.st-key-back-button .stButton button:hover {
    background: var(--primary) !important;
    color: var(--primary-foreground) !important;
    transform: translateY(-2px) !important;
    box-shadow: var(--shadow-md) !important;
    border-color: var(--primary) !important;
}


.st-key-back-button .stButton button p {
    margin: 0 !important;
    color: inherit !important;
}


/* ===== SIGNUP CONTAINER STYLING ===== */
.st-key-signup-container {
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
    padding: 2rem 1rem !important;
    min-height: calc(100vh - 100px) !important;
    flex: 1 !important;
}


/* Main card container - single unified box */
.st-key-signup-container {
    background: var(--card) !important;
    border-radius: calc(var(--radius) + 8px) !important;
    box-shadow: var(--shadow-xl) !important;
    padding: clamp(2rem, 5vw, 3.5rem) !important;
    max-width: min(450px, 90vw) !important;
    width: 100% !important;
    position: relative !important;
    overflow: hidden !important;
    animation: slideInUp 0.8s ease-out !important;
    height: fit-content !important;
    margin: 0 auto !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
}


@keyframes slideInUp {
    from {
        opacity: 0;
        transform: translateY(30px) scale(0.95);
    }
    to {
        opacity: 1;
        transform: translateY(0) scale(1);
    }
}


/* Animated gradient border */
.st-key-signup-container::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: linear-gradient(90deg, var(--primary), var(--secondary), var(--accent));
    background-size: 200% 100%;
    animation: gradientMove 3s ease-in-out infinite;
}


@keyframes gradientMove {
    0%, 100% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
}


/* Subtle pattern overlay */
.st-key-signup-container::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: radial-gradient(circle at 20% 80%, rgba(99, 102, 241, 0.02) 0%, transparent 50%),
                radial-gradient(circle at 80% 20%, rgba(245, 158, 11, 0.02) 0%, transparent 50%);
    pointer-events: none;
    z-index: -1;
}


/* ===== SIGNUP HEADER STYLING ===== */
.signup-header {
    text-align: center !important;
    margin-bottom: clamp(1.5rem, 4vw, 2.5rem) !important;
    position: relative !important;
}


.signup-title {
    font-size: clamp(2rem, 6vw, 2.8rem) !important;
    font-weight: 700 !important;
    margin-bottom: 0.75rem !important;
    background: linear-gradient(135deg, var(--primary), var(--secondary)) !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    background-clip: text !important;
    animation: titleGlow 2s ease-in-out infinite alternate !important;
    letter-spacing: -0.02em !important;
    line-height: 1.2 !important;
}


@keyframes titleGlow {
    from { filter: brightness(1); }
    to { filter: brightness(1.1); }
}


.signup-subtitle {
    color: var(--muted-foreground) !important;
    font-size: clamp(1rem, 3vw, 1.15rem) !important;
    animation: fadeIn 1s ease-out 0.3s both !important;
    font-weight: 400 !important;
    line-height: 1.5 !important;
}


@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}


/* ===== FORM STYLING ===== */
.st-key-signup-form {
    display: block !important;
    position: relative !important;
}


.st-key-form-group-1,
.st-key-form-group-2,
.st-key-form-group-3 {
    margin-bottom: 1.75rem !important;
    animation: slideInLeft 0.6s ease-out !important;
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    padding: 0 !important;
    position: relative !important;
}


.st-key-form-group-1 { animation-delay: 0.4s !important; }
.st-key-form-group-2 { animation-delay: 0.5s !important; }
.st-key-form-group-3 { animation-delay: 0.6s !important; }


@keyframes slideInLeft {
    from {
        opacity: 0;
        transform: translateX(-20px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}


/* ===== INPUT FIELD STYLING ===== */

.stTextInput:focus-within{
    border:none;!important
    outline:none;!important
}

div[data-baseweb="input"]{
    border:none;
    height: 50px;
    width:100%;
    padding:0;
    border-radius: var(--radius) !important;
}

.stTextInput label {
    display: block !important;
    margin-bottom: 0.625rem !important;
    font-weight: var(--font-weight-medium) !important;
    color: var(--card-foreground) !important;
    font-size: 0.95rem !important;
    transition: color 0.3s ease !important;
    letter-spacing: 0.01em !important;
}


.stTextInput input {
    width: 100% !important;
    padding: 1rem 1.25rem !important;
    border: 1.5px solid var(--border) !important;
    border-radius: var(--radius) !important;
    background: var(--input-background) !important;
    color: var(--card-foreground) !important;
    font-size: 1rem !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    outline: none !important;
    box-shadow: var(--shadow-sm) !important;
    font-family: inherit !important;
    height:50px;
}


.stTextInput input:focus {
    border-color: var(--primary) !important;
    box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.08), var(--shadow-sm) !important;
    background: var(--card) !important;
}


.stTextInput input:hover:not(:focus) {
    border-color: rgba(99, 102, 241, 0.25) !important;
    box-shadow: var(--shadow-md) !important;
}


.stTextInput input::placeholder {
    color: var(--muted-foreground) !important;
    transition: opacity 0.3s ease !important;
    font-size: 1rem !important;
    font-weight:500;
}


.stTextInput input:focus::placeholder {
    opacity: 0.6 !important;
}


/* ===== PASSWORD STRENGTH INDICATOR ===== */
.password-strength {
    margin: 0.5rem 0 0 0 !important;
    font-size: 0.85rem !important;
    color: var(--muted-foreground) !important;
    transition: all 0.3s ease !important;
    padding: 0.5rem 0.75rem !important;
    background: rgba(248, 250, 252, 0.8) !important;
    border-radius: calc(var(--radius) - 2px) !important;
    border-left: 3px solid var(--muted) !important;
    font-weight: var(--font-weight-medium) !important;
}


/* ===== BUTTON STYLING ===== */
.st-key-signup-button {
    margin: 2rem 0 1.5rem 0 !important;

    animation: slideInUp 0.6s ease-out 0.7s both !important;
}


.st-key-signup-button .stButton button {
    background: linear-gradient(135deg, var(--primary), #8b5cf6) !important;
    color: var(--primary-foreground) !important;
    box-shadow: var(--shadow-md) !important;
    width: 100% !important;
    font-size: 1.1rem !important;
    padding: 1.25rem !important;
    border: none !important;
    border-radius: var(--radius) !important;
    font-weight: 600 !important;
    cursor: pointer !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    text-align: center !important;
    position: relative !important;
    overflow: hidden !important;
    letter-spacing: 0.02em !important;
    min-height: 52px !important;
}


.st-key-signup-button .stButton button::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
    transition: left 0.5s ease !important;
}


.st-key-signup-button .stButton button:hover::before {
    left: 100% !important;
}


.st-key-signup-button .stButton button:hover {
    transform: translateY(-2px) !important;
    box-shadow: var(--shadow-lg) !important;
}


.st-key-signup-button .stButton button:active {
    transform: translateY(0px) !important;
    transition: transform 0.1s ease !important;
}


.st-key-signin-page-button {
    animation: fadeIn 0.6s ease-out 0.8s both !important;
    margin: 2rem 0 1.5rem 0 !important;
    display: flex !important;
    justify-content: center !important;
    width:100%;
}


.st-key-signin-page-button .stButton button {
    background: transparent !important;
    color: var(--primary) !important;
    border: 1.5px solid var(--primary) !important;
    width: 100% !important;
    padding: 1rem 1.5rem !important;
    border-radius: var(--radius) !important;
    font-weight: var(--font-weight-medium) !important;
    cursor: pointer !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    font-size: 1rem !important;
    text-align: center !important;
    min-height: 48px !important;
    box-shadow: var(--shadow-sm) !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    min-width: 150px !important;
}


.st-key-signin-page-button .stButton button:hover {
    background: var(--primary) !important;
    color: var(--primary-foreground) !important;
    transform: translateY(-2px) !important;
    box-shadow: var(--shadow-md) !important;
}


.stButton button p {
    margin: 0 !important;
    font-weight: inherit !important;
    color: inherit !important;
    line-height: 1.4 !important;
}


/* ===== DIVIDER STYLING ===== */
.divider {
    display: flex !important;
    align-items: center !important;
    margin: 2rem 0 1.5rem 0 !important;
    color: var(--muted-foreground) !important;
    animation: fadeIn 0.6s ease-out 0.75s both !important;
    position: relative !important;
}


.divider::before,
.divider::after {
    content: '' !important;
    flex: 1 !important;
    height: 1px !important;
    background: linear-gradient(to right, transparent, var(--border), transparent) !important;
}


.divider span {
    padding: 0 1.5rem !important;
    font-size: 0.9rem !important;
    background: var(--card) !important;
    font-weight: var(--font-weight-medium) !important;
    white-space: nowrap !important;
}


/* ===== TERMS STYLING ===== */
.terms {
    font-size: 0.85rem !important;
    color: var(--muted-foreground) !important;
    text-align: center !important;
    margin-top: 1.5rem !important;
    line-height: 1.6 !important;
    animation: fadeIn 0.6s ease-out 0.9s both !important;
    padding: 0 0.5rem !important;
}


.terms a {
    color: var(--primary) !important;
    text-decoration: none !important;
    transition: all 0.3s ease !important;
    font-weight: var(--font-weight-medium) !important;
    position: relative !important;
}


.terms a::after {
    content: '';
    position: absolute;
    width: 0;
    height: 1px;
    bottom: -2px;
    left: 0;
    background-color: var(--primary);
    transition: width 0.3s ease;
}


.terms a:hover {
    color: var(--secondary) !important;
}


.terms a:hover::after {
    width: 100%;
    background-color: var(--secondary);
}


/* ===== STREAMLIT OVERRIDES - REMOVE ALL INTERNAL BOXES ===== */
.stVerticalBlock > div:not(:last-child) {
    margin-bottom: 0 !important;
}


.stElementContainer {
    margin-bottom: 0 !important;
}


/* Remove all internal container styling */
.st-key-signup-form .stVerticalBlock,
.st-key-form-group-1 .stVerticalBlock,
.st-key-form-group-2 .stVerticalBlock,
.st-key-form-group-3 .stVerticalBlock {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    padding: 0 !important;
    margin: 0 !important;
}


/* Remove container backgrounds and borders */
div[data-testid="stVerticalBlock"],
div[data-testid="stHorizontalBlock"] {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
}


/* Specifically target form containers */
.st-key-signup-form > div,
.st-key-form-group-1 > div,
.st-key-form-group-2 > div,
.st-key-form-group-3 > div {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    padding: 0 !important;
}


/* Hide unwanted elements */
.st-emotion-cache-1dumvfu,
[data-testid="stAppIframeResizerAnchor"] {
    display: none !important;
}


/* ===== RESPONSIVE DESIGN ===== */
@media (max-width: 768px) {
    .st-key-signup-container {
        padding: 1.5rem 1rem !important;
        min-height: calc(100vh - 80px) !important;
    }


    .st-key-header {
        padding: 0.875rem 1rem !important;
    }


    .st-key-back-button .stButton button {
        padding: 0.5rem 1rem !important;
        font-size: 0.9rem !important;
    }
    
    .st-key-form-group-1,
    .st-key-form-group-2,
    .st-key-form-group-3 {
        margin-bottom: 1.5rem !important;
    }
    
    .stTextInput input {
        padding: 0.875rem 1rem !important;
        font-size: 16px !important; /* Prevents zoom on iOS */
    }
    
    .st-key-signin-page-button .stButton button {
        min-width: 120px !important;
        padding: 0.875rem 1.25rem !important;
    }
}


@media (max-width: 480px) {
    .st-key-signup-container {
        padding: 1rem !important;
    }
    
    .divider span {
        padding: 0 1rem !important;
        font-size: 0.85rem !important;
    }
    
    .terms {
        font-size: 0.8rem !important;
        padding: 0 !important;
    }
    
    .st-key-signin-page-button .stButton button {
        min-width: 100px !important;
        padding: 0.75rem 1rem !important;
        font-size: 0.9rem !important;
    }
}


@media (min-width: 1200px) {
    .st-key-signup-container {
        max-width: 480px !important;
        padding: 4rem !important;
    }
}


/* ===== ACCESSIBILITY ENHANCEMENTS ===== */
@media (prefers-reduced-motion: reduce) {
    * {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
    }
    
    .st-key-signup-container::before {
        animation: none !important;
    }
    
    .logo {
        animation: none !important;
    }
}


@media (prefers-color-scheme: dark) {
    /* Dark mode support can be added here if needed */
}


/* ===== LOADING STATE STYLING ===== */
.btn-loading {
    position: relative !important;
    color: transparent !important;
}


.btn-loading::after {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 20px;
    height: 20px;
    border: 2px solid transparent;
    border-top: 2px solid currentColor;
    border-radius: 50%;
    animation: spin 1s linear infinite;
}


@keyframes spin {
    to {
        transform: translate(-50%, -50%) rotate(360deg);
    }
}


/* ===== ENHANCED FOCUS STYLES ===== */
.stButton button:focus-visible {
    outline: 2px solid var(--ring) !important;
    outline-offset: 2px !important;
}


.stTextInput input:focus-visible {
    outline: 2px solid var(--ring) !important;
    outline-offset: 2px !important;
}


/* ===== PRINT STYLES ===== */
@media print {
    .st-key-header,
    .st-key-back-button {
        display: none !important;
    }
    
    .st-key-signup-container {
        box-shadow: none !important;
        border: 1px solid #000 !important;
    }
}
"""


styles = f"""
<style>
{remove_header_footer}
{other_styles}
</style>
"""


def signup_page():
    st.markdown(styles, unsafe_allow_html=True)
    st.set_page_config(
        page_title="Looto - Your Trusted Shopping Destination",
        page_icon="🛍️",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # Header section with sticky positioning
    with st.container(key="header"):
        logo_col, button_col = st.columns([3, 1], gap="small")
        with logo_col:
            st.markdown(
                """
                <div class="logo">Looto</div>
                """,
                unsafe_allow_html=True
            )
        with button_col:
            with st.container(key = "back-btn"):
                st.button(
                    label="Back To Home",
                    key="back-button",
                    type="tertiary",
                    icon=":material/arrow_back:",
                    on_click=st.session_state["navigation"].to_last_page
                )


    # Main signup container
    with st.container(key="signup-container"):
        # Signup header
        st.markdown(
            """
            <div class="signup-header">
                <h1 class="signup-title">Join Looto</h1>
                <p class="signup-subtitle">Create your account to start shopping</p>
            </div>
            """,
            unsafe_allow_html=True
        )


        # Signup form
        with st.container(key="signup-form"):
            with st.container(key="form-group-1"):
                name = st.text_input(
                    label="Name",
                    key="form-input-name",
                    placeholder="Enter your name"
                )
                name_flag = ValidateUser.validate_name(name)

            
            with st.container(key="form-group-2"):
                email = st.text_input(
                    label="Email",
                    key="form-input-email",
                    placeholder="Enter your email"
                )
                email_flag = ValidateUser.validate_email(email)
            
            with st.container(key="form-group-3"):
                password = st.text_input(
                    label="Password",
                    key="form-input-password",
                    placeholder="Enter your password",
                    type="password"
                )
                password_flag = ValidateUser.validate_password(password)
                
                # Dynamic password strength indicator
                if password:
                    strength = "Strong" if len(password) >= 8 else "Weak"
                    color = "var(--accent)" if len(password) >= 8 else "var(--destructive)"
                    st.markdown(
                        f"""
                        <div class="password-strength" style="color: {color}; border-left-color: {color};">
                            Password strength: {strength} ({len(password)} characters)
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                else:
                    st.markdown(
                        """
                        <div class="password-strength">
                            Password should be at least 8 characters long
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
            
            # Signup button with validation
            st.button(
                label="Create Account",
                key="signup-button",
                type="secondary"
            )
        
        # Divider
        st.markdown(
            """
            <div class="divider">
                <span>Already have an account?</span>
            </div>
            """,
            unsafe_allow_html=True
        )


        # Sign in button
        st.button(
            label="Sign In Instead",
            key="signin-page-button",
            type="tertiary",
            on_click=st.session_state["navigation"].handel_already_a_user
        )


        # Terms and conditions
        st.markdown(
            """
            <div class="terms">
                By creating an account, you agree to our 
                <a href="#" target="_blank">Terms of Service</a> and 
                <a href="#" target="_blank">Privacy Policy</a>
            </div>
            """,
            unsafe_allow_html=True
        )



