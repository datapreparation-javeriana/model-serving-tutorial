# Model serving tutorial (Flask version)

Deployment instructions:

1. Install virtualenv: `pip install virtualenv` o `pip3 install virtualenv`.

2. Create the new environment: `python -m venv env` o `python3 -m venv env`.

3. Activate the environment: `source env/bin/activate` (Mac/Linux) o `.\env\Scripts\activate` (Windows).

4. Install the dependencies: `pip install -r requirements.txt` o `pip3 install -r requirements.txt`.

5. Start the server: `flask --app main run`.

6. Testing the service using a tool like Postman:

```
POST /predict HTTP/1.1
Host: 127.0.0.1:5000
Content-Type: application/json

[
	{
		"credit_score": 713,
	    "country": "Spain",
	    "gender": "Female",
	    "age": 48,
	    "tenure": 1,
	    "balance": 163760.82,
	    "products_number": 1,
	    "credit_card": 0,
	    "active_member": 0,
	    "estimated_salary": 42117.90
	}
]
```

7. It is also possible to test it from the browser going to URL: http://localhost:5000/