# How to Import Postman Collection

## Step 1: Import the Collection

1. Open Postman
2. Click **Import** button (top left)
3. Select **File** tab
4. Click **Upload Files**
5. Navigate to your project folder: `C:\Users\vekas\Employee Management`
6. Select file: `Employee_Management_API.postman_collection.json`
7. Click **Import**

## Step 2: Set Up Environment Variables (Optional but Recommended)

### Create Environment:

1. Click **Environments** (left sidebar) → **+** (Create new)
2. Name it: `Employee Management Local`
3. Add variables:
   - Variable: `access_token` (leave value empty)
   - Variable: `refresh_token` (leave value empty)
   - Variable: `base_url` = `http://127.0.0.1:8000`
4. Click **Save**
5. Select this environment from dropdown (top right)

### Auto-Save Token:

The "Get JWT Token" request has a script that automatically saves the token to environment variables. After running it:
- `access_token` will be saved automatically
- All other requests will use it automatically

## Step 3: Test Authentication

1. Expand collection: **Employee Management API**
2. Go to **Authentication** folder
3. Click **Get JWT Token**
4. Click **Send**
5. Check response - you should get `access` and `refresh` tokens
6. The token is automatically saved to environment (if you set it up)

## Step 4: Test Employee Endpoints

All employee endpoints are pre-configured with:
- ✅ Correct URLs
- ✅ Bearer token authentication
- ✅ Sample request bodies
- ✅ Proper headers

Just click **Send** on any request!

## Collection Structure

```
Employee Management API
├── Authentication
│   ├── Get JWT Token (saves token automatically)
│   └── Refresh Token
└── Employees
    ├── Create Employee
    ├── List All Employees
    ├── List Employees - Filter by Department
    ├── List Employees - Filter by Role
    ├── List Employees - Pagination (Page 2)
    ├── Get Employee by ID
    ├── Get Employee - 404 Error
    ├── Update Employee
    ├── Delete Employee
    ├── Create Employee - Duplicate Email Error
    ├── Create Employee - Empty Name Error
    └── List Employees - Without Auth (401 Error)
```

## Quick Start

1. **Import collection** (Step 1)
2. **Run "Get JWT Token"** (Step 3)
3. **Test any endpoint** - token is automatically included!

## Notes

- Token expires in 1 hour - get a new one if needed
- All employee endpoints require authentication
- Change employee IDs in URLs as needed (e.g., `/api/employees/1/` → `/api/employees/2/`)
- Base URL is set to `http://127.0.0.1:8000` - change if your server runs on different port

## Troubleshooting

### Token Not Working
- Make sure you ran "Get JWT Token" first
- Check token hasn't expired (1 hour lifetime)
- Verify environment is selected (top right dropdown)

### 401 Unauthorized
- Get a new token from "Get JWT Token"
- Make sure environment variable `access_token` is set

### Server Not Running
- Run: `python manage.py runserver`
- Verify URL: `http://127.0.0.1:8000`

---

**You're all set! The collection is ready to use.**

