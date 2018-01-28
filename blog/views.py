from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from blog.models import Post,Comment,Rule,Registration
from blog.forms import PostForm,CommentForm,RuleForm,RegisterForm
# create your views here

class AboutView(TemplateView):
    template_name = 'about.html'


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')



class PostDetailView(DetailView):
    model = Post


class CreatePostView(CreateView,LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

class UpdatePostView(UpdateView,LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post



class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')


class DraftListViwe(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')

# Comments

# Below method is for handling addition of comments to post

@login_required
def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form=CommentForm()
    return render(request,'blog/comment_form.html',{'form':form})

# Below method is for handling approval of comments

@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)


@login_required
def comment_remove(request,pk):
    comment=get_object_or_404(Comment,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail',pk=post_pk)



@login_required
def post_publish(request,pk):
    post=get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)




# Rules


class RuleListView(ListView):
    model = Rule

    def get_queryset(self):
        return Rule.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')



class RuleDetailView(DetailView):
    model = Rule




class CreateRuleView(CreateView,LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'blog/rule_detail.html'
    form_class = RuleForm
    model = Rule

class UpdateRuleView(UpdateView,LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'blog/rule_detail.html'
    form_class = RuleForm
    model = Rule




class RuleDeleteView(LoginRequiredMixin,DeleteView):
    model = Rule
    success_url = reverse_lazy('rule_list')



@login_required
def rule_publish(request,pk):
    rule=get_object_or_404(Rule,pk=pk)
    rule.publish()
    return redirect('rule_detail',pk=pk)



# Paypal

class PaypalView(TemplateView):
    template_name = 'blog/paypal_form.html'



# Rules

class CreateRegsiterView(CreateView):
    login_url = '/login/'
    redirect_field_name = '/'
    form_class = RegisterForm
    model = Registration

