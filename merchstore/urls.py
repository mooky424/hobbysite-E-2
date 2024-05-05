from django.urls import path

from .views import (
    CartView,
    ProductCreateView,
    ProductDetailView,
    ProductListView,
    ProductUpdateView,
    TransactionDetailView,
    TransactionListView,
)

urlpatterns = [
    path("items", ProductListView.as_view(), name="product_list"),
    path("item/<int:pk>", ProductDetailView.as_view(), name="product_detail"),
    path("item/add", ProductCreateView.as_view(), name="product_create"),
    path("item/<int:pk>", ProductUpdateView.as_view(), name="product_update"),
    path("cart", CartView.as_view(), name="cart"),
    path(
        "transactions",
        TransactionListView.as_view(),
        name="transaction_list",
    ),
    path(
        "transaction/<int:pk>",
        TransactionDetailView.as_view(),
        name="transaction_detail",
    ),
]

app_name = "merchstore"
