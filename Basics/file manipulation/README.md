# Information Systems Mark Recording System

The concept of this activity is to test knowledge in Python Data Structures, File I/O, and OOP.
This system will be built in a multi tier approach

## 1. Data Layer

### 1.1 File Management Classes

#### `CSVHandler` (Abstract Base Class)
- **Responsibility**: Provides base functionality for CSV file operations
- **Attributes**:
  - `file_path: str` - Path to the CSV file
- **Methods**:
  - `read() -> List[Dict]` - Reads CSV file and returns list of dictionaries
  - `write(data: List[Dict]) -> bool` - Writes list of dictionaries to CSV file
  - `append(record: Dict) -> bool` - Appends a single record to CSV file

#### `StudentFileHandler` (extends `CSVHandler`)
- **Responsibility**: Handles operations specific to students.csv
- **Methods**:
  - `get_student_by_id(student_id: str) -> Dict` - Retrieves student record by ID
  - `get_students_by_program(program: str) -> List[Dict]` - Retrieves students by program
  - `add_student(student_data: Dict) -> bool` - Adds new student record
  - `update_student(student_id: str, updated_data: Dict) -> bool` - Updates student info
  - `validate_student_data(student_data: Dict) -> bool` - Validates student data format

#### `CourseFileHandler` (extends `CSVHandler`)
- **Responsibility**: Handles operations for course-specific CSV files
- **Attributes**:
  - `course_code: str` - Course code (e.g., "ismx01")
  - `assessments: List[str]` - List of assessment column names in the CSV
- **Methods**:
  - `get_student_marks(student_id: str) -> Dict` - Gets all marks for a student
  - `update_mark(student_id: str, assessment: str, mark: float) -> bool` - Updates specific mark
  - `calculate_final_grade(student_id: str) -> float` - Calculates final grade based on weights
  - `get_assessment_average(assessment: str) -> float` - Calculates class average for an assessment
  - `get_course_structure() -> Dict` - Returns assessment structure and weights

#### `AssessorFileHandler` (extends `CSVHandler`)
- **Responsibility**: Manages assessor information and assignments
- **Methods**:
  - `get_assessors_by_course(course_code: str) -> List[Dict]` - Gets assessors for a course
  - `assign_assessor(assessor_id: str, course_code: str) -> bool` - Assigns assessor to course
  - `validate_assessor_permissions(assessor_id: str, course_code: str) -> bool` - Checks permissions

### 1.2 Data Models

#### `Student`
- **Responsibility**: Represents a student entity
- **Attributes**:
  - `id: str` - Student ID
  - `first_name: str` - First name
  - `last_name: str` - Last name
  - `email: str` - Email address
  - `program: str` - Enrolled program
  - `enrollment_year: int` - Year of enrollment
  - `current_semester: int` - Current semester
- **Methods**:
  - `full_name() -> str` - Returns full name
  - `to_dict() -> Dict` - Converts to dictionary for storage
  - `from_dict(data: Dict) -> Student` - Creates Student object from dictionary (static)

#### `Course`
- **Responsibility**: Represents a course entity
- **Attributes**:
  - `code: str` - Course code
  - `name: str` - Course name
  - `assessments: Dict[str, float]` - Assessment names and their weights
  - `instructor_id: str` - ID of main instructor
- **Methods**:
  - `get_file_name() -> str` - Returns the CSV file name for this course
  - `to_dict() -> Dict` - Converts to dictionary for storage
  - `from_dict(data: Dict) -> Course` - Creates Course object from dictionary (static)

#### `Assessor`
- **Responsibility**: Represents an assessor (instructor/TA)
- **Attributes**:
  - `id: str` - Assessor ID
  - `name: str` - Full name
  - `role: str` - Role (Instructor, TA, etc.)
  - `courses: List[str]` - List of assigned course codes
- **Methods**:
  - `can_assess(course_code: str) -> bool` - Checks if authorized to assess a course
  - `to_dict() -> Dict` - Converts to dictionary for storage
  - `from_dict(data: Dict) -> Assessor` - Creates Assessor object from dictionary (static)

## 2. Business Logic Layer

### 2.1 Service Classes

#### `StudentService`
- **Responsibility**: Manages student-related business logic
- **Dependencies**:
  - `student_file_handler: StudentFileHandler`
- **Methods**:
  - `register_student(student_data: Dict) -> bool` - Registers new student
  - `get_student_details(student_id: str) -> Student` - Gets complete student info
  - `search_students(query: str) -> List[Student]` - Searches students by name/ID
  - `update_student_info(student_id: str, updated_info: Dict) -> bool` - Updates student data

#### `MarkService`
- **Responsibility**: Handles mark recording and calculations
- **Dependencies**:
  - `course_file_handlers: Dict[str, CourseFileHandler]` - Map of course handlers
- **Methods**:
  - `record_mark(student_id: str, course_code: str, assessment: str, mark: float) -> bool` - Records mark
  - `get_student_course_marks(student_id: str, course_code: str) -> Dict` - Gets all marks in a course
  - `calculate_final_grade(student_id: str, course_code: str) -> float` - Calculates course final grade
  - `calculate_gpa(student_id: str) -> float` - Calculates overall GPA
  - `get_course_statistics(course_code: str) -> Dict` - Gets statistical breakdown of course

#### `ProgressService`
- **Responsibility**: Tracks and analyzes student progress
- **Dependencies**:
  - `student_service: StudentService`
  - `mark_service: MarkService`
- **Methods**:
  - `get_student_progress(student_id: str) -> Dict` - Gets progress across all courses
  - `identify_at_risk_students(threshold: float) -> List[Student]` - Identifies struggling students
  - `generate_progress_report(student_id: str) -> Dict` - Creates detailed progress report
  - `track_performance_trend(student_id: str) -> Dict` - Analyzes performance over time

#### `AssessorService`
- **Responsibility**: Manages assessor operations
- **Dependencies**:
  - `assessor_file_handler: AssessorFileHandler`
- **Methods**:
  - `authenticate_assessor(assessor_id: str, password: str) -> bool` - Authenticates assessor
  - `get_assigned_courses(assessor_id: str) -> List[Course]` - Gets assessor's courses
  - `verify_assessment_permission(assessor_id: str, course_code: str) -> bool` - Checks permissions
  - `assign_to_course(assessor_id: str, course_code: str) -> bool` - Assigns assessor to course

### 2.2 Utility Classes

#### `GradeCalculator`
- **Responsibility**: Handles different grading calculations
- **Methods**:
  - `calculate_weighted_average(marks: Dict[str, float], weights: Dict[str, float]) -> float` - Calculates weighted grade
  - `convert_to_letter_grade(percentage: float) -> str` - Converts percentage to letter grade
  - `convert_to_gpa(percentage: float) -> float` - Converts percentage to GPA points
  - `calculate_class_average(marks: List[float]) -> float` - Calculates class average

#### `DataValidator`
- **Responsibility**: Validates data across the system
- **Methods**:
  - `validate_student_id(student_id: str) -> bool` - Checks student ID format
  - `validate_email(email: str) -> bool` - Validates email format
  - `validate_mark(mark: float, max_mark: float) -> bool` - Ensures mark is within valid range
  - `validate_assessment_name(name: str) -> bool` - Validates assessment name format

#### `ReportGenerator`
- **Responsibility**: Generates various system reports
- **Methods**:
  - `generate_class_report(course_code: str) -> Dict` - Creates course performance report
  - `generate_student_transcript(student_id: str) -> Dict` - Creates student transcript
  - `export_to_pdf(report_data: Dict, template: str) -> bytes` - Exports report to PDF format
  - `export_to_csv(report_data: Dict) -> bytes` - Exports report to CSV format

## 3. Presentation Layer

### 3.1 UI Classes

#### `ConsoleUI`
- **Responsibility**: Main console interface for the system
- **Methods**:
  - `display_menu() -> None` - Shows main menu
  - `get_user_choice() -> int` - Gets user menu selection
  - `display_message(message: str) -> None` - Displays system message
  - `get_input(prompt: str) -> str` - Gets text input from user
  - `clear_screen() -> None` - Clears console screen

#### `AuthenticationView`
- **Responsibility**: Handles user authentication screens
- **Methods**:
  - `login_screen() -> Tuple[str, str]` - Shows login screen, returns credentials
  - `display_login_error() -> None` - Shows login error message
  - `show_password_reset() -> None` - Displays password reset interface

#### `StudentRecordView`
- **Responsibility**: Displays student record interfaces
- **Methods**:
  - `display_student_details(student: Student) -> None` - Shows student information
  - `display_student_marks(marks: Dict) -> None` - Shows student's marks
  - `student_search_interface() -> str` - Interface for searching students
  - `add_student_interface() -> Dict` - Interface for adding a new student

#### `MarkRecordingView`
- **Responsibility**: Handles mark recording interfaces
- **Methods**:
  - `select_course_interface(courses: List[Course]) -> str` - Interface to select course
  - `select_assessment_interface(assessments: List[str]) -> str` - Interface to select assessment
  - `enter_marks_interface() -> Dict[str, float]` - Interface for entering marks
  - `show_mark_confirmation(student_id: str, assessment: str, mark: float) -> bool` - Confirms mark entry

#### `ReportView`
- **Responsibility**: Displays report interfaces and outputs
- **Methods**:
  - `select_report_type() -> str` - Interface to select report type
  - `display_report(report_data: Dict) -> None` - Displays formatted report
  - `export_report_interface(report_data: Dict) -> str` - Interface for exporting reports
  - `show_report_filters() -> Dict` - Interface for setting report filters

### 3.2 Controller Classes

#### `ApplicationController`
- **Responsibility**: Main controller that coordinates system operations
- **Dependencies**:
  - `console_ui: ConsoleUI`
  - `student_controller: StudentController`
  - `mark_controller: MarkController`
  - `report_controller: ReportController`
- **Methods**:
  - `start() -> None` - Starts the application
  - `process_menu_choice(choice: int) -> None` - Routes to appropriate controller
  - `exit_application() -> None` - Gracefully exits the application
  - `handle_error(error: Exception) -> None` - Global error handler

#### `AuthenticationController`
- **Responsibility**: Handles user authentication and authorization
- **Dependencies**:
  - `authentication_view: AuthenticationView`
  - `assessor_service: AssessorService`
- **Methods**:
  - `login() -> bool` - Processes login attempt
  - `verify_permissions(assessor_id: str, action: str) -> bool` - Verifies action permissions
  - `logout() -> None` - Logs out current user
  - `get_current_user() -> Assessor` - Returns currently logged in user

#### `StudentController`
- **Responsibility**: Controls student-related operations
- **Dependencies**:
  - `student_view: StudentRecordView`
  - `student_service: StudentService`
- **Methods**:
  - `search_student() -> Student` - Processes student search
  - `add_student() -> bool` - Processes adding new student
  - `view_student_details(student_id: str) -> None` - Shows student details
  - `update_student(student_id: str) -> bool` - Updates student information

#### `MarkController`
- **Responsibility**: Controls mark recording operations
- **Dependencies**:
  - `mark_view: MarkRecordingView`
  - `mark_service: MarkService`
  - `authentication_controller: AuthenticationController`
- **Methods**:
  - `record_marks() -> bool` - Processes mark recording workflow
  - `view_student_marks(student_id: str) -> None` - Shows student marks
  - `update_mark(student_id: str, course_code: str, assessment: str) -> bool` - Updates existing mark
  - `calculate_and_display_final_grades(course_code: str) -> None` - Shows final grades

#### `ReportController`
- **Responsibility**: Controls report generation operations
- **Dependencies**:
  - `report_view: ReportView`
  - `progress_service: ProgressService`
  - `report_generator: ReportGenerator`
- **Methods**:
  - `generate_report() -> None` - Handles report generation workflow
  - `view_class_report(course_code: str) -> None` - Shows class report
  - `view_student_progress(student_id: str) -> None` - Shows student progress
  - `export_report(report_data: Dict, format: str) -> bool` - Exports report

## 4. System Integration

### 4.1 Startup and Configuration

#### `ApplicationConfig`
- **Responsibility**: Manages application configuration
- **Methods**:
  - `load_config(config_file: str) -> Dict` - Loads configuration from file
  - `get_file_paths() -> Dict[str, str]` - Returns file paths for CSVs
  - `get_assessments_by_course() -> Dict[str, List[str]]` - Returns course assessment structures
  - `get_grade_scheme() -> Dict` - Returns grading scheme configuration

#### `SystemBootstrapper`
- **Responsibility**: Initializes system components
- **Methods**:
  - `initialize() -> ApplicationController` - Initializes all system components
  - `setup_file_handlers() -> Dict` - Sets up file handlers
  - `setup_services() -> Dict` - Sets up service layer
  - `setup_controllers() -> Dict` - Sets up controller layer

### 4.2 Error Handling

#### `ErrorLogger`
- **Responsibility**: Logs system errors
- **Methods**:
  - `log_error(error: Exception, context: str) -> None` - Logs error with context
  - `log_warning(message: str) -> None` - Logs warning message
  - `get_recent_errors() -> List[Dict]` - Gets recent error logs

## 5. Main Program Entry

#### `Main`
- **Responsibility**: Application entry point
- **Methods**:
  - `main() -> None` - Main entry method
  - `parse_arguments(args: List[str]) -> Dict` - Parses command-line arguments
