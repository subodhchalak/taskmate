from todolist_app.models import TaskList
from django.db.models import Q 
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage


def paginateProjects(request, projectsList, results):
    page=request.GET.get('page')  # It takes page number query from browser like '/?page=2' where 2 is page number                       

    # results=3                                            # Results per page
    paginator=Paginator(projectsList, results)           
    
    try:
        projectsList=paginator.page(page)                 # Resetting 'projectsList' using 'paginator' object
    except PageNotAnInteger:                              # Raised when page() is given a value that isn’t an integer.
        # If page is not an integer deliver the first page
        page=1
        projectsList=paginator.page(page)
    except EmptyPage:                                     # Raised when page() is given a valid value but no objects exist on that page.
        # If page is out of range deliver last page of results
        page=paginator.num_pages                          # it will give total number of pages
        projectsList=paginator.page(page)                 # if page number is beyond total number of pages,
                                                          # by default, last page will be displayed

    leftIndex=(int(page)-4)                               # On first page it will show max 3 pages

    if leftIndex<1:
        leftIndex=1

    rightIndex=(int(page)+3)                            # It will show maximum 1+3 pages under pagination                           

    if rightIndex>paginator.num_pages:                  # if rightIndex is greater than total number of pages
        rightIndex=paginator.num_pages+1              # then rightIndex will become a last page

    custom_range=range(leftIndex, rightIndex)            # custom page range upto 20 pages
    return custom_range, projectsList