import views

fronts = [views.secret_front, views.other_front]

routes = {
    '/': views.Index(),
    '/index/': views.Index(),
    '/about/': views.About(),
    '/contact/': views.Contact(),
    '/study_programs/': views.StudyPrograms(),
    '/courses_list/': views.CoursesList(),
    '/create_course/': views.CreateCourse(),
    '/create_category/': views.CreateCategory(),
    '/category_list/': views.CategoryList(),
    '/copy_course/': views.CopyCourse()
}
