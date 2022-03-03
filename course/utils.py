from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage



def paginateCourses(request, courses, results):
    page = request.data['page']
    paginator = Paginator(courses, results)
    try:
        courses = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        courses = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        courses = paginator.page(page)
    leftIndex = (int(page) - 4)
    if leftIndex < 1:
        leftIndex = 1
    rightIndex = (int(page) + 5)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1
    custom_range = range(leftIndex, rightIndex)
    return courses
