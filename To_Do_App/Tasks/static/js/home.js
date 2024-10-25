// Get references to relevant elements
const taskForm = document.querySelector('.task-form');
const taskInput = document.getElementById('new-task-input');
const taskList = document.querySelector('.task-list');
let taskCounter = 3;  // Continue task numbering from 3

// Show the form to add a new task
function showTaskForm() {
    taskForm.classList.remove('hidden');
}

// Hide the form and clear the input field
function hideTaskForm() {
    taskForm.classList.add('hidden');
    taskInput.value = '';  // Clear the input field
}

// Add a new task to the list when "Add" button is clicked
function addTask() {
    const taskValue = taskInput.value.trim();

    // Check if task input is not empty
    if (taskValue === '') {
        alert('Task cannot be empty!');
        return;
    }

    taskCounter++;
    const newTaskItem = document.createElement('li');
    newTaskItem.classList.add('task-item');

    newTaskItem.innerHTML = `
        <span>Task ${taskCounter}: ${taskValue}</span>
        <button class="delete-btn">Delete</button>
        <input type="checkbox" class="task-checkbox">
    `;

    taskList.appendChild(newTaskItem);

    // Add functionality to delete button and checkbox
    const deleteBtn = newTaskItem.querySelector('.delete-btn');
    const checkbox = newTaskItem.querySelector('.task-checkbox');

    addDeleteFunctionality(deleteBtn);

    checkbox.addEventListener('click', () => {
        if (areAllTasksCompleted()) {
            showCongratulations();
        }
    });

    hideTaskForm();  // Hide form after task is added
    taskInput.value = '';  // Clear the input field
}

// Function to check if all tasks are completed
function areAllTasksCompleted() {
    return Array.from(document.querySelectorAll('.task-checkbox')).every(checkbox => checkbox.checked);
}

// Show congratulations message when all tasks are checked
function showCongratulations() {
    document.querySelector('.congratulations').style.display = 'block';
}

// Reset all tasks and hide the congratulations message
function resetTasks() {
    document.querySelectorAll('.task-checkbox').forEach(checkbox => {
        checkbox.checked = false;
    });
    document.querySelector('.congratulations').style.display = 'none';
}

// Add delete functionality to existing and new tasks
function addDeleteFunctionality(deleteBtn) {
    deleteBtn.addEventListener('click', function () {
        this.parentElement.remove();
    });
}

// Add delete functionality to existing tasks
document.querySelectorAll('.delete-btn').forEach(addDeleteFunctionality);
