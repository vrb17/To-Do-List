# to-do-list
Functional to-do list web application using Flask. Contains routes to display, add, edit, delete, and mark tasks as completed.

Overall, when the Flask application is run (to_do.py), it starts the server. Upon accessing the root route (/), the index.html template is rendered, displaying the current to-do list. The user can then interact with the application by adding, editing, deleting, and marking tasks as completed, triggering the corresponding routes defined in app.py and updating the todo_list. The changes are reflected in the rendered index.html template, providing a dynamic and interactive to-do list application.

to_do.py:
- Sets up the Flask application, defines routes, and implements the necessary functions to handle requests.
- Renders index.html template for the root route (/) to display the to-do list.
- Renders alter.html template for the /alter/<int:index> route to edit a specific task.
- Implements routes for adding, deleting, and marking tasks as completed.
- Runs the Flask development server.

index.html:
- Displays the to-do list with tasks and their completion status.
- Iterates over the todo_list using a loop and displays each task in a list item (<li>).
- Includes a checkbox to mark tasks as completed, with the checkbox being checked or unchecked based on the completion status.
- Applies a line-through style to completed tasks using conditional logic.
- Provides links to edit, remove, and mark tasks as completed, with the appropriate route specified using url_for.
- Includes a form to add new tasks to the to-do list, which is submitted to the /add route.

alter.html:
- Renders a form to edit a specific task.
- Sets the form's action to the /alter/<int:index> route, allowing the task to be updated.
- Displays the existing task value in an input field (<input>) with the name "todo" and pre-populates it with the current task value.
- Includes a "Save" button to submit the form and trigger the update of the task in the todo_list.
