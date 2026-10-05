const descriptions = [
  "Write the two required welcome lines to welcome.txt.",
  "Enter a student's details and save them in student.txt.",
  "Read and display all five names from student_names.txt.",
  "Loop through a five-line text file and display each line.",
  "Append a name to students.txt without replacing existing data.",
  "Count the lines in the sample text file.",
  "Count words with split() in the sample text file.",
  "Try to read a file by name and handle a missing file.",
  "Divide two values and handle invalid input or division by zero.",
  "Calculate a square and always display the completion message.",
  "Add or view students with a small menu and a separate file.",
  "Validate age and marks before saving student data.",
  "Search the supplied student names and marks file.",
  "Add, view, or search complete student records.",
  "Keep a student file permanently and add, view, search, or add several records."
];

const taskSelect = document.getElementById("task-id");
const title = document.getElementById("task-title");
const kicker = document.getElementById("task-kicker");
const description = document.getElementById("task-description");
const fieldsContainer = document.getElementById("dynamic-fields");
const operationHint = document.getElementById("operation-hint");
const taskButtons = [...document.querySelectorAll(".task-link")];
const form = document.getElementById("task-form");

const field = (name, label, placeholder = "", wide = false) => ({ name, label, placeholder, wide });
const commonRecordFields = [
  field("name", "Student name", "e.g. Anika"),
  field("age", "Age", "Whole number"),
  field("course", "Course", "e.g. Python"),
  field("marks", "Marks", "0 to 100")
];

function makeInput(item) {
  const wrapper = document.createElement("label");
  wrapper.className = `form-field${item.wide ? " field-wide" : ""}`;
  const caption = document.createElement("span");
  caption.textContent = item.label;
  let control;
  if (item.textarea) {
    control = document.createElement("textarea");
    control.rows = 4;
  } else {
    control = document.createElement("input");
    control.type = "text";
  }
  control.name = item.name;
  control.placeholder = item.placeholder || "Enter " + item.label.toLowerCase();
  control.autocomplete = "off";
  wrapper.append(caption, control);
  return wrapper;
}

function makeActionSelect(taskId, selectedAction) {
  const wrapper = document.createElement("label");
  wrapper.className = "form-field field-wide action-field";
  const caption = document.createElement("span");
  caption.textContent = "Choose an operation";
  const select = document.createElement("select");
  select.name = "action";
  const options = taskId === 11
    ? [["add", "Add Student"], ["view", "View Students"]]
    : [["add", "Add Student"], ["view", "View Students"], ["search", "Search Student"]];
  if (taskId === 15) options.push(["add_more", "Add More Students"]);
  for (const [value, label] of options) {
    const option = document.createElement("option");
    option.value = value;
    option.textContent = label;
    select.append(option);
  }
  select.value = selectedAction;
  wrapper.append(caption, select);
  select.addEventListener("change", () => renderFields(taskId, select.value));
  return wrapper;
}

function fieldsFor(taskId, action) {
  if (taskId === 2) return commonRecordFields;
  if (taskId === 5 || taskId === 13) return [field("name", "Student name", "Search or add a name")];
  if (taskId === 8) return [field("filename", "Filename", "missing_file.txt")];
  if (taskId === 9) return [field("first", "First number"), field("second", "Second number")];
  if (taskId === 10) return [field("number", "Number to square")];
  if (taskId === 11) return action === "add" ? [field("name", "Student name"), field("marks", "Marks")] : [];
  if (taskId === 12) return [field("name", "Student name"), field("age", "Age"), field("marks", "Marks")];
  if (taskId === 14 || taskId === 15) {
    if (action === "add") return commonRecordFields;
    if (action === "search") return [field("name", "Student name")];
    if (action === "add_more") return [field("records", "One record per line: Name, Age, Course, Marks", "Anika, 18, Python, 91", true)];
  }
  return [];
}

function renderFields(taskId, action = "") {
  fieldsContainer.replaceChildren();
  if ([11, 14, 15].includes(taskId)) fieldsContainer.append(makeActionSelect(taskId, action || "add"));
  for (const item of fieldsFor(taskId, action)) fieldsContainer.append(makeInput(item));
  operationHint.textContent = [11, 14, 15].includes(taskId) ? "STUDENT RECORD ACTION" : "SET UP AND RUN";
}

function selectTask(taskId) {
  taskSelect.value = String(taskId);
  title.textContent = taskButtons[taskId - 1].querySelector(".task-link-title").textContent;
  kicker.textContent = `EXERCISE ${String(taskId).padStart(2, "0")} / 15`;
  description.textContent = descriptions[taskId - 1];
  for (const button of taskButtons) {
    const active = Number(button.dataset.task) === taskId;
    button.classList.toggle("is-active", active);
    if (active) button.setAttribute("aria-current", "step");
    else button.removeAttribute("aria-current");
  }
  renderFields(taskId, "add");
  document.getElementById("output-text").classList.add("is-empty");
}

for (const button of taskButtons) {
  button.addEventListener("click", () => selectTask(Number(button.dataset.task)));
}

form.addEventListener("submit", () => {
  const button = form.querySelector(".run-button");
  button.disabled = true;
  button.textContent = "Running...";
});

const selected = Number(document.body.dataset.selected) || 1;
selectTask(selected);
if (document.getElementById("output-text").textContent.trim() && !document.getElementById("output-text").classList.contains("is-empty")) {
  document.getElementById("output-text").classList.remove("is-empty");
}