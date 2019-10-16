import yagmail




yagmail.register('cxiesestro@gmail.com', 'secrectPlease')

#body
#keywords[]


#if(body.find(keywords[])) if(true)


receiver = "cxiesestro@gmail.com"
body = "huoueoueoueo"

yag = yagmail.SMTP("cxiesestro@gmail.com")
yag.send(
    to=receiver,
    subject="Yagmail test with attachment",
    contents=body,
)

