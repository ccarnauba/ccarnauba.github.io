import util
import sys
import argparse

def main():
    error_str = "Improper use of script. Check source code."
    if len(sys.argv) < 2:
        # TODO figure out a way to make these errors more maintainable.
        print(error_str)
        return 1
    if sys.argv[1] == "convert-markdown":
        if len(sys.argv) < 4:
            print (error_str)
            return 1
        else:
            util.convert_markdown_directory_to_blog_pages (sys.argv[2], sys.argv[3])
            return 0
    elif sys.argv[1] == "create-blog-html":
        if len(sys.argv) < 4:
            print (error_str)
            return 1
        else:
            util.create_blog_html(sys.argv[2], sys.argv[3])
            return 0
    elif sys.argv[1] == "regenerate-blogs":
        if len(sys.argv) < 5:
            print (error_str)
            return 1
        else:
            util.regerate_all_blogs_and_create_blog(sys.argv[2], sys.argv[3], sys.argv[4])
            return 0
    else:

        print(error_str)
        return 0

if __name__ == '__main__':
    main()
