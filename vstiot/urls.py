from django.urls import path
from . views import home, add, update, delete, upload, branch2, add2branch2, update2branch2, delete2branch2, upload2branch2, search, search_branch3, branch3, add2branch3, update2branch3, delete2branch3, branch4, add2branch4, update2branch4, delete2branch4, upload2branch4, search_branch4, upload2branch3, export_csv, export_csv_branch2, export_csv_branch3, export_csv_branch4, search_branch5

urlpatterns = [
    path('',home,name='home'),
    path('add',add,name='add'),
    path('update/<int:item_id>',update,name='update'),
    path('delete/<int:item_id>',delete,name='delete'),
    path('upload',upload,name='upload'),
    path('branch2',branch2,name='branch2'),
    path('add2branch2',add2branch2,name='add2branch2'),
    path('update2branch2/<int:branch2_id>',update2branch2,name='update2branch2'),
    path('delete2branch2/<int:branch2_id>',delete2branch2,name='delete2branch2'),
    path('upload2branch2',upload2branch2,name='upload2branch2'),
    path('search',search,name='search'),
    path('search_branch3',search_branch3,name='search_branch3'),
    path('branch3',branch3,name='branch3'),
    path('add2branch3',add2branch3,name='add2branch3'),
    path('update2branch3/<int:branch3_id>',update2branch3,name='update2branch3'),
    path('delete2branch3/<int:branch3_id>',delete2branch3,name='delete2branch3'),
    path('branch4',branch4,name='branch4'),
    path('add2branch4',add2branch4,name='add2branch4'),
    path('update2branch4/<int:branch4_id>',update2branch4,name='update2branch4'),
    path('delete2branch4/<int:branch4_id>',delete2branch4,name='delete2branch4'),
    path('upload2branch4',upload2branch4,name='upload2branch4'),
    path('search_branch4',search_branch4,name='search_branch4'),
    path('upload2branch3',upload2branch3,name='upload2branch3'),
    path('export_csv',export_csv,name='export_csv'),
    path('export_csv_branch2',export_csv_branch2,name='export_csv_branch2'),
    path('export_csv_branch3',export_csv_branch3,name='export_csv_branch3'),
    path('export_csv_branch4',export_csv_branch4,name='export_csv_branch4'),
    path('search_branch5',search_branch5,name='search_branch5'),
    
]