import mechanize
br = mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

br.open("https://fw.bits-pilani.ac.in:8090/httpclient.html")
# br.
# br.select_form( nr = 0 )
# br.form['username'] = "f20170118"
# br.form['password'] = "A7PS01186238#"
# response=br.submit()
print(br.forms())
