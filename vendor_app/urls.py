from django.urls import path
from .views import *

urlpatterns = [
    path("vendors/", VendorListCreateView.as_view(), name="vendor_list_create"),
    path("vendors/<int:pk>/", VendorRetrieveUpdateDeleteView.as_view(), name="vendor_retrieve_update_delete"),
    path("purchase_orders/", PurchaseOrderListCreateView.as_view(), name="purchase_order_list_create"),
    path("purchase_orders/<int:pk>/", PurchaseOrderRetrieveUpdateDeleteView.as_view(),
         name="purchase_order_retrieve_update_delete"),
    path("vendors/<int:pk>/performance/", VendorPerformanceView.as_view(), name="vendor_performance"),
    path("purchase_orders/<int:pk>/acknowledge/", AcknowledgePurchaseOrderView.as_view(),
         name="acknowledge_purchase_order"),
]
