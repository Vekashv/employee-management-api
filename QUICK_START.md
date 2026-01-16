# 🚀 Quick Start Guide - How to Run the Project

## Step-by-Step Instructions

### Step 1: Open Terminal/Command Prompt
- Press `Win + R`, type `cmd` or `powershell`, and press Enter
- Navigate to the project directory:
  ```bash
  cd "C:\Users\vekas\Employee Management"
  ```

### Step 2: Create Virtual Environment (Recommended)
```bash
python -m venv venv
```

### Step 3: Activate Virtual Environment
**Windows (Command Prompt):**
```bash
venv\Scripts\activate
```

**Windows (PowerShell):**
```bash
venv\Scripts\Activate.ps1
```

If you get an execution policy error in PowerShell, run:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 5: Run Database Migrations
```bash
python manage.py migrate
```

### Step 6: Create a Test User
```bash
python create_test_user.py
```

This will create:
- **Username:** `testuser`
- **Password:** `testpass123`

### Step 7: Start the Development Server
```bash
python manage.py runserver
```

You should see:
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

### Step 8: Test the API

#### Get JWT Token (Required for all endpoints)

**Using PowerShell/curl:**
```powershell
curl -X POST http://127.0.0.1:8000/api/token/ -H "Content-Type: application/json" -d '{\"username\":\"testuser\",\"password\":\"testpass123\"}'
```

**Or use Postman:**
1. Method: `POST`
2. URL: `http://127.0.0.1:8000/api/token/`
3. Body → raw → JSON:
   ```json
   {
       "username": "testuser",
       "password": "testpass123"
   }
   ```
4. Copy the `access` token from response

#### Test Employee Endpoints

**Create Employee:**
```powershell
curl -X POST http://127.0.0.1:8000/api/employees/ `
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" `
  -H "Content-Type: application/json" `
  -d '{\"name\":\"John Doe\",\"email\":\"john@example.com\",\"department\":\"Engineering\",\"role\":\"Developer\"}'
```

**List Employees:**
```powershell
curl -X GET http://127.0.0.1:8000/api/employees/ `
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## 🧪 Run Tests

```bash
pytest
```

Or:
```bash
python manage.py test
```

## 📝 Common Commands

| Command | Purpose |
|---------|---------|
| `python manage.py runserver` | Start the development server |
| `python manage.py migrate` | Apply database migrations |
| `python manage.py createsuperuser` | Create admin user (optional) |
| `python manage.py shell` | Open Django shell |
| `pytest` | Run all tests |
| `python create_test_user.py` | Create test user for API |

## 🌐 Access Points

- **API Base URL:** `http://127.0.0.1:8000/api/`
- **Admin Panel:** `http://127.0.0.1:8000/admin/` (requires superuser)
- **Token Endpoint:** `http://127.0.0.1:8000/api/token/`

## ⚠️ Troubleshooting

### Issue: "python is not recognized"
**Solution:** Use `py` instead of `python`:
```bash
py manage.py runserver
```

### Issue: "ModuleNotFoundError"
**Solution:** Make sure virtual environment is activated and dependencies are installed:
```bash
pip install -r requirements.txt
```

### Issue: "No such table: employees_employee"
**Solution:** Run migrations:
```bash
python manage.py migrate
```

### Issue: "401 Unauthorized"
**Solution:** Make sure you're including the JWT token in the Authorization header:
```
Authorization: Bearer YOUR_ACCESS_TOKEN
```

## 📚 Next Steps

1. Read `README.md` for complete API documentation
2. Read `PROJECT_EXPLANATION.md` for detailed project breakdown
3. Test all endpoints using Postman (see README for Postman guide)
4. Run the test suite to verify everything works

---

**The server is running when you see:** `Starting development server at http://127.0.0.1:8000/`

