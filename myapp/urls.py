from django.urls import path
from myapp import views
from myapp import drf_views


urlpatterns = [

    path("", views.home, name = "home"),

    # authentication

    path('sign_up',views.sign_up, name= 'sign_up'),
    path('log_in',views.log_in, name= 'log_in'),
    path('log_out',views.log_out, name= 'log_out'),


    #=================================================================
    path('show_products/<id>',views.show_products, name="show_products"),
    path('show_cart',views.show_cart, name='show_cart'),
    path('cart_remove/<id>', views.cart_item_delete, name = "cart_remove"),
    path('order',views.order, name = "order"),
    path('show_order',views.show_order, name = 'show_order'),
    path('add_customer', views.add_customer, name = 'add_customer'),
    path('sort_by',views.sort_by, name='sort_by'),
    path('search', views.search, name='search'),

    # api
    # # ==========================  product or category ki API  hai yeah ===================================================
    # path("cat_data/<pk>",drf_views.CategoryAPI.as_view(), name ="cat_data"),  # data get through pk
    # path("cat_data",drf_views.CategoryAPI.as_view(), name ="cat_data"),


    # path("pro_data/<pk>",drf_views.ProductAPI.as_view(),name = "pro_data"),
    # path("pro_data",drf_views.ProductAPI.as_view(),name = "pro_data")


    # ============================================================================

    # simple form me query hai 

    path('cat_data',drf_views.CategoryListCreate.as_view()),
    path('cat_data/<pk>',drf_views.CategoryUpdate.as_view()),

    path('customer_data',drf_views.CategoryListCreate.as_view()),
    path('customer_data/<pk>',drf_views.CategoryListCreate.as_view()),

    path('product_data',drf_views.ProductListCreate.as_view()),
    path('product_data/<pk>',drf_views.ProductUpdate.as_view()),

    path('cart_data',drf_views.CartListCreate.as_view()),
    path('cart_data/<pk>',drf_views.CartUpdate.as_view()),

    path('order_data',drf_views.OrderListCreate.as_view()),
    path('order_data/<pk>',drf_views.OrderUpdate.as_view()),

    path('person', drf_views.PersonAPI.as_view()),
]



















