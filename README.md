# 🛒 Looto.com – Phase 2

Looto.com is an E-Commerce platform built using **Streamlit**, **MySQL**, and **Object-Oriented Programming** principles. This is **Phase 2** of the project, upgraded from a JSON-based system to a more scalable and production-ready backend using MySQL.

---

## 🚀 Features

- ✅ User Signup & Login (Auth)
- ✅ Product Listing and Categorization
- ✅ Add to Cart / Remove from Cart
- ✅ Place Orders
- ✅ Track Orders
- ✅ Persistent MySQL storage
- ✅ Fully modular and scalable architecture (OOP principles)
- ✅ Session management
- ✅ Clean, UI-rich front end using Streamlit

---

## 🧠 Tech Stack

| Layer         | Tools/Languages                |
|---------------|--------------------------------|
| Frontend      | [Streamlit](https://streamlit.io) |
| Backend Logic | Python (OOP-based services)    |
| Database      | MySQL                          |
| Auth Mgmt     | Custom auth via hashed passwords |
| Deployment    | Localhost / Streamlit Sharing (future) |

---

## 📁 Folder Structure

```
looto/
├── .env                  # Environment variables (DB credentials)
├── main.py               # Entry point for the Streamlit app
├── README.md             # You're reading it!

├── auth/                 # Login and Signup logic
│   ├── login.py
│   └── signup.py

├── config/               # Configuration management
│   └── db_config.py      # MySQL DB connector

├── database/             # DB schema and seed data
│   ├── create_tables.sql
│   └── seed_data.sql     # Sample product, user, and order entries

├── models/               # OOP Models
│   ├── user_model.py
│   ├── product_model.py
│   ├── cart_model.py
│   ├── order_model.py    # Combines order and tracking models
│   └── category_model.py

├── screens/              # UI pages (formerly pages/)
│   ├── 1_Landing_Page.py
│   ├── 2_Home.py
│   ├── 3_Product.py
│   ├── 4_Cart.py
│   ├── 5_Orders.py
│   └── 6_Tracking.py

├── services/             # Business logic
│   ├── auth_service.py
│   ├── cart_service.py
│   ├── product_service.py
│   ├── orders_service.py   # Includes tracking logic
│   └── data_validation/
│       └── json_validator.py

├── session_state/        # User session handler
│   └── session_manager.py

└── static/
    └── products/
        └── red_tshirt.png
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/looto-phase2.git
cd looto-phase2
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available:

```bash
pip install streamlit mysql-connector-python python-dotenv
```

### 3. Setup MySQL

- Create a MySQL database (e.g. `looto_db`)
- Execute the scripts:

```bash
mysql -u root -p looto_db < database/create_tables.sql
mysql -u root -p looto_db < database/seed_data.sql
```

### 4. Configure Environment

Create a `.env` file in the root directory with the following content:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=yourpassword
DB_NAME=looto_db
```

### 5. Run the App

```bash
streamlit run main.py
```

---

## 📸 Screenshots (Optional)

> You can add screenshots of Home page, Cart view, Order Tracking, etc. here.

---

## 🙌 Contributors

- 👨‍💻 **Anik Dashora** – Lead Developer

---

## 📄 License

This project is licensed under the MIT License.

---

## 💡 Future Enhancements

- Deploy on Streamlit Sharing or Render
- Add payment gateway mock integration
- Email notifications for order status
- Admin dashboard for inventory management
