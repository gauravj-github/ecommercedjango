from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MypasswordChangeForm,MyPasswordResetForm, MyPasswordConfirmForm

urlpatterns = [
    # path('', views.home),


    path('',views.ProductViews.as_view(),name="home"),

    # path('product-detail/', views.product_detail, name='product-detail'),
    path('product-detail/<id>',views.ProductDetailView.as_view(), name='product-detail'),

    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/',views.show_cart,name='show-cart'),
    path('pluscart/',views.plus_cart),
    path('minuscart/',views.minus_cart),


    path('remove-cart/<id>',views.remove_item,name='remove-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('remove-address <id>',views.remove_address,name='remove-address'),
    path('orders/', views.orders, name='orders'),

    # path('changepassword/', views.change_password, name='changepassword'),
    
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),

    path('topwear/',views.top_wear,name='topwear'),

    path('bottomwear/',views.bottom_wear,name='bottomwear'),

    path('account/login/', auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name='login'),

    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),

    path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html',form_class= MypasswordChangeForm, success_url='/passwordchangedone/'),name='passwordchange'),
    path('passwordchangedone/',auth_views.PasswordChangeView.as_view(template_name='app/passwordchangedone.html'),name='passwordchangedone') ,

    
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=MyPasswordResetForm),name="password_reset"),
    path('password-reset/Done/',auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'),name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html', form_class=MyPasswordConfirmForm),name="password_reset_confirm"),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'),name="password_reset_complete"),
    


    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    

    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/', views.payment_done, name='paymentdone'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
