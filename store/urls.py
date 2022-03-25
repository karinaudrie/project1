from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.main, name="main"),
	path('store/', views.store, name="store"),

	path('covid/', views.covid, name="covid"),
	path('cart/', views.cart, name="cart"),
	path('contactus/', views.contactus, name="contactus"),
	path('faq/', views.faq, name="faq"),
	path('event/', views.event, name="event"),
	path('checkout/', views.checkout, name="checkout"),
	path('signin/',views.log_in, name='signin'),
	path('signup/',views.signup, name='signup'),
	path('signout/', views.signout, name='signout'),

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
]
