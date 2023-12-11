from datetime import date

from django.shortcuts import render

all_posts = [
    {
        "slug": "hike-on-the-beach",
        "image": "beach.jpg",
        "author": "Mateusz",
        "date": date(2023,12,11),
        "title": "Beach Hiking",
        "excerpt": "There's nothing like the views you get when hiking on the beach! And I wasn't even prepared for what happend whilst I was enjoying the view!",
        "content": """
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Amet dolorum 
            architecto non similique veritatis voluptatum delectus aperiam earum, 
            deserunt totam nemo ipsam! Ex explicabo corrupti sequi ratione doloribus optio ea?

            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Amet dolorum 
            architecto non similique veritatis voluptatum delectus aperiam earum, 
            deserunt totam nemo ipsam! Ex explicabo corrupti sequi ratione doloribus optio ea?

            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Amet dolorum 
            architecto non similique veritatis voluptatum delectus aperiam earum, 
            deserunt totam nemo ipsam! Ex explicabo corrupti sequi ratione doloribus optio ea?
        """
 },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Mateusz",
        "date": date(2023,12,11),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "into-the-night",
        "image": "sunset.jpg",
        "author": "Mateusz",
        "date": date(2023,12,11),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }
]


def get_date(post):
    return post['date']

# Create your views here.

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })

def post_detail(request, slug):
    indentified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": indentified_post
    })