from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Post
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.order_by('-id')
        return render(request, 'app/index.html', {
            'post_data': post_data
        })


class PostDetailView(View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        return render(request, 'app/post_detail.html', {
            'post_data': post_data
        })

class CreatePostView(View, LoginRequiredMixin):
    def get(self, request, *args, **kwargs):
        form = PostForm(request.POST or None)
        return render(request, 'app/post_form.html', {
            'form': form
        })
    
    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST or None)

        if form.is_valid():
            post_data = Post()
            post_data.title = form.cleaned_data.get('title')
            post_data.content = form.cleaned_data.get('content')
            post_data.save()
            # return redirect('index')
            return redirect('post_detail', post_data.id)

        # return render(request, 'app/index.html', {
        #     'form': form
        # })

class PostEditView(View, LoginRequiredMixin):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        form = PostForm(
            request.POST or None,
            initial={
                'title': post_data.title,
                'content': post_data.content,
            }
        )

        return render(request, 'app/post_form.html', {
            'form': form
        })
    
    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST or None)

        if form.is_valid():
            post_data = Post.objects.get(id=self.kwargs['pk'])
            post_data.author = request.user
            post_data.title = form.cleaned_data.get('title')
            post_data.content = form.cleaned_data.get('content')
            post_data.save()
            return redirect('post_detail', post_data.id)
        
class PostDeleteView(View, LoginRequiredMixin):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        return render(request, 'app/post_delete.html', {
            'post_data': post_data
        })
    
    def post(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        post_data.delete()
        return redirect('index')