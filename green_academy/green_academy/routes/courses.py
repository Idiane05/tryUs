from flask import Blueprint, request, jsonify # type: ignore
from flask_login import login_required, current_user # type: ignore
from models import Course, Enrollment, db

courses_bp = Blueprint('courses', __name__)

@courses_bp.route('', methods=['GET'])
@login_required
def get_courses():
    courses = Course.query.all()
    return jsonify([{
        'id': c.id,
        'title': c.title,
        'description': c.description,
        'instructor_id': c.instructor_id
    } for c in courses]), 200

@courses_bp.route('', methods=['POST'])
@login_required
def create_course():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400
        
    course = Course(
        title=data.get('title'),
        description=data.get('description'),
        instructor_id=current_user.id
    )
    
    db.session.add(course)
    db.session.commit()
    
    return jsonify({
        'id': course.id,
        'title': course.title,
        'description': course.description,
        'instructor_id': course.instructor_id
    }), 201

@courses_bp.route('/<int:course_id>', methods=['GET'])
@login_required
def get_course(course_id):
    course = Course.query.get_or_404(course_id)
    return jsonify({
        'id': course.id,
        'title': course.title,
        'description': course.description,
        'instructor_id': course.instructor_id,
        'enrolled_students': len(course.enrollments)
    }), 200

@courses_bp.route('/<int:course_id>/enroll', methods=['POST'])
@login_required
def enroll_course(course_id):
    course = Course.query.get_or_404(course_id)
    
    if Enrollment.query.filter_by(student_id=current_user.id, course_id=course_id).first():
        return jsonify({"error": "Already enrolled in this course"}), 400
        
    enrollment = Enrollment(student_id=current_user.id, course_id=course_id)
    db.session.add(enrollment)
    db.session.commit()
    
    return jsonify({"message": "Successfully enrolled"}), 201
