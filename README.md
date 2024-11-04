# PythonDailyReport
Initial MR request for PythonDailyReport

Step 1: Project Structure
Ensure your project structure remains the same:

arduino
Copy code
test_report_app/
    app.py
    templates/
        report.html
        form.html
    static/
        styles.css
Step 2: Install Bootstrap
You can use Bootstrap via a CDN in your HTML files. No additional installation is required.

Step 3: Update the HTML Templates
form.html
html
Copy code
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
    <title>Test Case Daily Report</title>
</head>
<body>
    <div class="container mt-5">
        <h1 class="text-center">Submit Daily Test Case Report</h1>
        <form action="/submit" method="POST" class="mt-4">
            <div class="form-group">
                <label for="emp_id">Tester Emp ID:</label>
                <input type="text" class="form-control" id="emp_id" name="emp_id" required>
            </div>
            <div class="form-group">
                <label for="pending">Pending:</label>
                <input type="number" class="form-control" id="pending" name="pending" required>
            </div>
            <div class="form-group">
                <label for="in_progress">In Progress:</label>
                <input type="number" class="form-control" id="in_progress" name="in_progress" required>
            </div>
            <div class="form-group">
                <label for="completed">Completed:</label>
                <input type="number" class="form-control" id="completed" name="completed" required>
            </div>
            <div class="form-group">
                <label for="blocked">Blocked:</label>
                <input type="number" class="form-control" id="blocked" name="blocked" required>
            </div>
            <button type="submit" class="btn btn-primary">Submit Report</button>
        </form>
        <a href="/reports" class="btn btn-link">View Reports</a>
    </div>
</body>
</html>
report.html
html
Copy code
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <title>Test Case Reports</title>
</head>
<body>
    <div class="container mt-5">
        <h1 class="text-center">Daily Test Case Reports</h1>
        <table class="table table-bordered mt-4">
            <thead class="thead-light">
                <tr>
                    <th>Emp ID</th>
                    <th>Pending</th>
                    <th>In Progress</th>
                    <th>Completed</th>
                    <th>Blocked</th>
                </tr>
            </thead>
            <tbody>
                {% for report in reports %}
                <tr>
                    <td>{{ report.emp_id }}</td>
                    <td>{{ report.pending }}</td>
                    <td>{{ report.in_progress }}</td>
                    <td>{{ report.completed }}</td>
                    <td>{{ report.blocked }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
        <a href="/" class="btn btn-link">Submit Another Report</a>
    </div>
</body>
</html>
Step 4: Optional Custom CSS
Create a custom CSS file (static/styles.css) to add any additional styling you prefer. For now, we’ll keep it minimal, but feel free to customize it further.

css
Copy code
body {
    background-color: #f8f9fa;
}
Step 5: Update app.py
No changes are required in the app.py file if you have already set it up as described earlier.

Step 6: Running the Application
Run your application again:

bash
Copy code
python app.py
Visit http://127.0.0.1:5000/ to access the form, submit reports, and view them in a styled table.
