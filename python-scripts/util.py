import markdown2
import os
import html_template
from dataclasses import dataclass
import datetime
import pathlib

@dataclass
class Blog_page:
    title: str
    date: datetime.date
    mardown_path: pathlib.Path
    html_path: pathlib.Path
    # TODO: It's a little insane to store ALL OF THE CONTENT IN MEMORY, but for
    # now that's fine.
    html_content : str


def write_blog_pages (blog_pages):
    for blog in blog_pages:
        with open(blog.html_path, "w") as html_file:
            html_file.write(blog.html_content)

def convert_markdown_directory_to_blog_pages (markdown_directory, html_directory):
    """
    Given a source markdown_directory containing only markdown files, and a
    destination html_directory, coverts all files in the source directory to
    html. Note that this function will overwrite files with the same name in
    the destination directory.
    """
    # TODO: Add testing suite.
    blog_pages = []

    for filename in os.listdir(markdown_directory):
        markdown_path = os.path.join(markdown_directory, filename)
        with open(markdown_path) as markdown_file:

            contents = markdown_file.readlines()
            title = contents[0].removeprefix("#")
            date_str = contents[1].lower().removeprefix("written on:").strip()
            date = datetime.date.fromisoformat(date_str)
            content_html = markdown2.markdown("".join(contents[2:]))
            html_content = html_template.standard_blog_post(content_html)

            html_filename = filename.removesuffix(".md") + ".html"

            # Note that this relies on the directory structure being there.
            html_path = os.path.join(html_directory, html_filename)
            blog_page = Blog_page(title, date,
                                  markdown_path,
                                  html_path,
                                  html_content)
            blog_pages.append(blog_page)

    return blog_pages


def create_blog_html(blog_pages, blog_file_path):
    """
    Given a directory of html blog posts, creates an html blog landing page
    with a list of blog posts.
    """
    blog_links = []
    # Note that the blog html lives in a different directory relative to
    # the scripts. As such, we have to remove the .. from the path.
    blog_pages.sort(key= lambda blog: blog.date)
    for blog in blog_pages:
        blog_link = blog.html_path.removeprefix("../")
        print(blog_link)
        anchor_tag =\
            f"""<a href= \"{blog_link}\"
            class=\"blog_post\">{blog.date}: {blog.title}</a>
            """
        list_element = f"<li> {anchor_tag} </li>"
        blog_links.append(list_element)

    list_of_links = "<ul>" + ''.join(blog_links) + "</ul>"

    new_blog_content = html_template.standard_top_level_post(list_of_links)
    with open(blog_file_path, "w") as blog_file:
        blog_file.write(new_blog_content)

def regerate_all_blogs_and_create_blog(markdown_directory, html_directory, blog_file_path):

    blog_pages = convert_markdown_directory_to_blog_pages(markdown_directory, html_directory)
    write_blog_pages(blog_pages)
    create_blog_html(blog_pages, blog_file_path)
