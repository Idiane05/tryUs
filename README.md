<<<<<<< HEAD
# advanced-python-programming-formative-1-green-academy-api

[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/GD_h1bVW)

## Formative Assessment 1: API Design and Core Functionality

### Green Academy API - Phase 1: Course and Enrollment Foundation

**Scenario:**

"The Green Academy is a non-profit organization that provides accessible online education about environmental sustainability and conservation. They need a new, interactive online learning platform to host their courses and engage learners of all ages. The platform should be designed to be user-friendly and informative, emphasizing accessibility for users with disabilities."

**Instructions:**

In this group(group of 2) assignment, you are tasked with building the foundational API endpoints for the Green Academy's new online learning platform. In this phase, focus on designing and implementing the core functionality related to courses and student enrollment while adhering to best data handling and efficiency practices.

### Part 1: API Design Document (20%)

Before you write any code, you'll need to create a document outlining the design of your API endpoints. This document must include:

* **Resources:** Identify the main resources (e.g., Courses, Enrollments).
* **Endpoints:** Define each resource's API endpoints (URIs).
* **HTTP Methods:** Specify the HTTP methods (`GET`, `POST`, etc.) supported by each endpoint.
* **Request/Response Structure:** Describe the expected request body (if applicable) and the structure of the response body (JSON format) for each endpoint. Use examples.
* **Status Codes:** Indicate the appropriate HTTP status codes for various scenarios (success, errors).
* **Pagination:** Describe your chosen pagination method for endpoints that return lists of resources.
* **Personal Data:** Identify any personal data your API will handle and briefly describe your strategy for handling it securely, according to GDPR or other relevant data privacy regulations, if applicable.

## Part 2: Implementation (70%)**

Implement the API endpoints you designed in Part 1 using Django REST Framework. Your implementation must meet the following requirements:

* **Models:** Create Django models for models identified in part 1.
* **Type Hints:** Use Python type hints (variable annotations) throughout your code (models, views, serializers).
* **Asynchronous Programming (Optional):** If you use asynchronous views, justify your decision in your design document.
* **Serializers:** Use DRF serializers to handle data serialization and deserialization.
* **Views:** Implement Django views to handle requests to your API endpoints.
* **Pagination:** Implement pagination for endpoints that return lists of resources (e.g., list of courses, etc,...).
* **Caching:** Implement at least one caching strategy (e.g., in-memory caching, database caching, or using a tool like Redis) to improve the performance of frequently accessed data. Justify your choice of caching strategy in your design document.
* **Personal Data Handling:** Please make sure that your API handles any personal data securely.

## Part 3: Mypy Type Checking (10%)**

* Use `mypy` to perform static type checking on your code.
* Your code should pass `mypy` checks without errors.
* Include a script or instructions in your README for running `mypy`.

**Technical Requirements:**

* Use Django REST Framework for building the API.
* Use Python type hints throughout the code.
* Use `mypy` for static type checking.
* Implement pagination and at least one caching strategy.
* Follow secure practices for handling personal data.
* Organize your code into appropriate Django apps.
* Document your API design in a separate document (e.g., `API_DESIGN.md` ).
* Include a `requirements.txt` file with all project dependencies.
* Provide clear instructions in your README on how to set up and run the project.

**Deliverables:**

* A link to your GitHub repository containing the complete project code.
* A well-structured `README.md` file explaining how to set up, run, and test your API.
* A separate document (`API_DESIGN.md` or a link to a Google Doc) outlining your API design as described in Part 1.

**Assessment Criteria:**

* **API Design Document (20%):**
  * Clarity and completeness of the design document.
  * Adherence to RESTful principles in API design.
  * Appropriate choice of HTTP methods and status codes.
  * Well-defined request and response structures.
  * Thoughtful consideration of pagination and personal data handling.
* **Code Functionality (40%):**
  * Correct implementation of API endpoints as defined in the design document.
  * Proper handling of HTTP requests and responses.
  * Effective use of DRF serializers for data serialization and deserialization.
* **Type Hinting and Mypy (20%):**
  * Consistent and correct use of Python type hints throughout the code.
  * Code passes `mypy` static type checking without errors.
* **Code Quality (10%):**
  * Code is well-organized, readable, and maintainable.
  * Code follows PEP 8 style guidelines (use a linter like `flake8` or `pylint` to check).
  * Code is adequately commented.
* **Pagination, Caching, and Personal Data Handling (10%):**
  * Correct implementation of the chosen pagination method.
  * Effective implementation of the chosen caching strategy, with justification.
  * Secure handling of personal data, as described in the design document.

**Tips for Success:**

* **Start with the design:** A well-thought-out API design will make implementation much easier.
* **Test as you go:** Use Http client, Postman, or a similar tool to test your API endpoints during development.
* **Refer to documentation:** The Django REST Framework documentation is your friend!
* **Don't be afraid to ask for help:** If you get stuck, ask your coach or classmates for assistance.
=======
[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/USEfmVMq)
# Formative Assessment 2: API Security, Authorization, and Documentation
**Green Academy API - Phase 2: Enhancing Security and Usability**

**Scenario:**

Building upon the foundation laid in Phase 1, this phase focuses on securing the Green Academy API, implementing fine-grained authorization, and generating comprehensive API documentation. Protecting sensitive data, ensuring only authorized users can access specific functionalities, and providing clear documentation are paramount for a robust and usable API.  Additionally, best practices for secure storage of sensitive information will be reinforced.

---

**Instructions:**

In this group (group of 2) assignment, you will significantly enhance the API developed in Phase 1 by implementing robust security measures, including JWT and Basic Authentication, granular authorization, and automated API documentation. You will also reinforce secure storage of sensitive information.  *Testing will be covered in a subsequent phase.*

---

**Part 1: Enhanced API Design Document (20%)**

Update the API Design Document from Phase 1 to include the following enhancements:

*   **Authentication Methods:** Detail the implementation of both JWT (JSON Web Token) and Basic Authentication. Explain the use cases for each method (e.g., JWT for general API access, Basic Auth for specific admin functionalities).
*   **Authorization (Granular Control):** Define specific roles and permissions within the API. Specify which roles have access to which endpoints with a fine-grained approach (e.g., only admins can create courses, instructors can update their own courses, students can only view course content). Explain how you plan to implement role-based access control, including specific examples for different endpoints.  Provide a clear mapping of roles to permissions.
*   **Sensitive Data Handling:** Describe the methods used to securely store sensitive information like passwords, API keys, and JWT secrets. Discuss best practices such as hashing passwords (using bcrypt or scrypt), using environment variables for sensitive keys, and avoiding storing sensitive data directly in the codebase.
*   **Input Validation:** Explain your approach to validating user input to prevent vulnerabilities like SQL injection and cross-site scripting (XSS). Specify the validation techniques you will use (e.g., using DRF serializers, custom validation functions).
*   **Error Handling:** Describe your strategy for handling errors securely. Avoid revealing sensitive information in error messages.  Define specific error codes and messages for common scenarios.
*   **API Documentation:** Explain how you plan to generate API documentation automatically (e.g., using DRF-yasg, Swagger, or similar tools).  Describe the information that will be included in the documentation (e.g., endpoints, request/response formats, authentication requirements, error codes).

---

**Part 2: Implementation (80%)**

Implement the security, authorization, and documentation enhancements designed in Part 1 using Django REST Framework. Your implementation must meet the following requirements:

*   **JWT Authentication:** Implement JWT authentication for API access. Users should be able to obtain a JWT upon successful login and use it for subsequent requests.  Implement token refresh mechanisms.
*   **Basic Authentication:** Implement Basic Authentication for specific endpoints (e.g., admin functionalities).
*   **Granular Role-Based Access Control:** Implement role-based access control to restrict access to certain endpoints based on user roles.  Use Django's built-in permissions system or a custom role management system for fine-grained control.  Provide clear examples in your code demonstrating how different roles are granted access to specific endpoints.
*   **Password Security:** Ensure passwords are securely hashed before being stored in the database (use Django's `make_password` function).
*   **Sensitive Data Storage:** Store sensitive information (e.g., JWT secret key, database credentials) securely using environment variables or a similar secure configuration method. **Do not hardcode sensitive information in your codebase.**
*   **Input Validation:** Implement robust input validation to prevent common web vulnerabilities. Use DRF serializers with appropriate validation rules or custom validation functions.
*   **Error Handling:** Implement secure error handling. Return generic error messages to avoid revealing sensitive information. Use informative error codes.
*   **HTTPS:** (Highly recommended) Configure your development server to use HTTPS if possible. This is crucial for secure communication.
*   **Automated API Documentation:** Integrate a tool like DRF-yasg or Swagger to generate API documentation automatically.  Ensure that your documentation is complete and accurate.

---

**Deliverables:**

*   A link to your GitHub repository containing the updated project code.
*   A well-structured README.md file explaining how to set up, run, and use the API, including instructions for generating the API documentation.
*   An updated API_DESIGN.md document reflecting the enhanced security, authorization, and documentation considerations.

---

**Assessment Criteria:**

*   **Enhanced API Design Document (20%):** Clarity, completeness, and thoroughness of the design document, including detailed authorization strategies and API documentation plans.
*   **Code Functionality (60%):** Correct implementation of JWT and Basic Authentication, granular role-based access control, secure password handling, robust input validation, and secure error handling.
*   **API Documentation (20%):** Completeness and accuracy of the generated API documentation.  All endpoints, request/response formats, authentication requirements, and error codes should be properly documented.
*   **Code Quality (10%):** Well-organized, readable, and maintainable code following PEP 8 style guidelines with adequate comments.
*   **Security Best Practices (10%):** Adherence to security best practices for sensitive data handling, secure configuration of the API, and consideration of HTTPS.
>>>>>>> 35f1441450f87b9e36f7a257843de1dd6664881a
