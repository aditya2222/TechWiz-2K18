from django.urls import path
from blog.views import AboutView,PostListView,PostDetailView,CreatePostView,UpdatePostView,PostDeleteView,DraftListViwe,add_comment_to_post,comment_approve,comment_remove,post_publish,RuleListView,RuleDeleteView,CreateRuleView,RuleDetailView,UpdateRuleView,rule_publish,CreateRegsiterView,PaypalView

urlpatterns=[
    path('posts',PostListView.as_view(),name='post_list'),
    path('',AboutView.as_view(),name='about'),
    path('post/<int:pk>/details',PostDetailView.as_view(),name='post_detail'),
    path('post/new/',CreatePostView.as_view(),name='post_new'),
    path('post/<int:pk>/edit/',UpdatePostView.as_view(),name='post_edit'),
    path('post/<int:pk>/remove/',PostDeleteView.as_view(),name='post_delete'),
    path('drafts/',DraftListViwe.as_view(),name='post_draft_list'),
    path('post/<int:pk>/comment/',add_comment_to_post,name='add_comment_to_post'),
    path('comments/<int:pk>/approve/',comment_approve,name='comment_approve'),
    path('comment/<int:pk>/remove/',comment_remove,name='comment_remove'),
    path('post/<int:pk>/publish/',post_publish,name='post_publish'),
    path('rule',RuleListView.as_view(),name='rule_list'),
    path('rule/<int:pk>/details', RuleDetailView.as_view(), name='rule_detail'),
    path('rule/new/', CreateRuleView.as_view(), name='rule_new'),
    path('rule/<int:pk>/edit/', UpdateRuleView.as_view(), name='rule_edit'),
    path('rule/<int:pk>/remove/', RuleDeleteView.as_view(), name='rule_delete'),
    path('rule/<int:pk>/publish/',rule_publish,name='rule_publish'),
    path('registration',CreateRegsiterView.as_view(),name='register'),
    path('paynow',PaypalView.as_view(),name='pay-now')

]