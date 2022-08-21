from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.index,name='index'),
    path('index/',views.index,name='index'),
    path('cart/<c_id>',views.addcart,name='cart'),
    path('showcart/',views.showcart,name='showcart'),
    path('show/',views.showcart,name='show'),
    path('remove/<r_id>',views.removecart,name='remove'),
    path('plus/<p_id>',views.plus,name='plus'),
    path('minus/<m_id>',views.minus,name='minus'),
    path('change/',views.change,name='change'),
    path('product/<int:id>',views.product,name='product'),
    path('product-detail/<my_id>',views.detail,name='detail'),
    path('checkout/',views.checkout,name='checkout'),
    path('my-account/',views.account,name='account'),
    path('wishlist/',views.wishlist,name='wishlist'),
    path('register/',views.register,name='register'),
    path('login/',views.login_user,name='login'),
    path('address/',views.address,name='address'),
    path('edit_address/<e_id>',views.edit_address,name='edit_address'),
    path('contact/',views.contact,name='contact'),
    path('vendor/',views.Vendor,name='vendor'),
    path('logout/',views.logout_user,name='logout'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="reset_password.html"),name='reset_password'),
    path('reset_sent/',auth_views.PasswordResetDoneView.as_view(template_name="reset_sent.html"),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="reset_confirm.html"),name='password_reset_confirm'),
    path('reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="reset_complete.html"),name='password_reset_complete'),
    path('pay/<int:f>',views.pay,name='pay'),
    path('success/' , views.success , name='success')
    ]