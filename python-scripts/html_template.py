def standard_head(css_location):
    head_html = f"""
<!doctype html>
<html lang="en-US">

<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width" />
    <title>Caio Dezotti Carnauba</title>

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
<link rel="stylesheet" href= "{css_location}"/>
</head>
"""
    return head_html

def standard_header(path_to_toplevel):
    html_header =\
    f"""
    <header>
        <nav class="main_banner">
            <h1 class="my_name"> Caio Dezotti Carnauba </h1>

            <h2 class="nav_bar">
                <div class="header-pair">
                    <a href= "{path_to_toplevel}index.html" title="Home">
                        <span class="slash"> / </span>
                        <span class="nav-name"> Home </span>
                    </a>
                </div>


                <div class="header-pair">
                    <a href="{path_to_toplevel}blog.html" title="Blog">
                        <span class="slash"> / </span>
                        <span class="nav-name"> Blog </span>
                    </a>
                </div>

                <div class="header-pair">
                    <a href="{path_to_toplevel}worklog.html" title="Worklog">
                        <span class="slash"> / </span>
                        <span class="nav-name"> Worklog </span>
                    </a>
                </div>
            </h2>
        </nav>
    </header>
"""
    return html_header

standard_footer ="""
"""

def standard_stylesheet(path_to_toplevel):  return path_to_toplevel + "styles/home_style.css"

def standard_webpage (content_html, path_to_toplevel):
    """
    Given an html string for the written content of our webpage, outputs
    html with the shared headers and footers.
    """
    webpage = standard_head(standard_stylesheet(path_to_toplevel)) + "<body>" + standard_header(path_to_toplevel)\
    + "<div class=\"text_body\">" + content_html\
    + "</div class=\"text_body\">" + standard_footer\
    + "</body>" + "</html>"
    return webpage

def standard_top_level_post (content_html):
    return standard_webpage(content_html, "")

def standard_blog_post (content_html):
    return standard_webpage(content_html, "../")
