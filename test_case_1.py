import combined_links as cl


def test_my_build():
    title = "*This is a test case*"
    linkedin_url = "www.linkedin.com/"
    twitter_url = "www.twitter.com/"
    facebook_url = "www.facebook.com/"
    instagram_url = "www.instagram.com/"
    output1 = cl.prepare_consolidated_message(title, linkedin_url, twitter_url, facebook_url, instagram_url)
    output = """*This is a test case*

*LinkedIn*
www.linkedin.com/

*Twitter*
www.twitter.com/

*Facebook*
www.facebook.com/

*Instagram*
www.instagram.com/
"""

    if output == output1:
        print("expected output received")

test_my_build()


