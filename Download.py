from requests import session
ss = session()
url = (f'https://thispersondoesnotexist.com/image')
def downloadImange(x):
    get_img = ss.get(url).content
    with open("{}.png".format(x),'wb') as saveImg:
        saveImg.write(get_img)
        print(f"Done {x}")

count = int(input("Enter Count: "))
for x in range(count):
    downloadImange(x)
# hungsaki2003@gmail.com