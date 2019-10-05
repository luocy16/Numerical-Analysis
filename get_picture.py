import urllib.request as ur
import  os

month = 1
date = 1
year = "2018"
#ur.urlretrieve("https://www.rai-playroom.net/gallery/{}/01.jpg".format("20190720a"), "D:/somepicture/1.jpg")

for month in range(1, 8):
    for date in range(1, 30):
        for flag in ['a', 'b', 'c', 'd']:
            target = "".join([year, str(month) if month >= 10 else "".join(["0", str(month)]),
                      str(date) if date >= 10 else "".join(["0", str(date)]),
                      flag])

            try:
                os.mkdir("D:\\somepicture\\{}".format(target))
            except Exception:
                pass

            cnt = 0
            for index in range(1, 30):
                try:
                    path = "https://www.rai-playroom.net/gallery/{0}/{1}.jpg".format(target, str(index) if index >= 10 else "".join(["0", str(index)]))
                    ur.urlretrieve(path, "D:\\somepicture\\{0}\\{1}.jpg".format(target, str(index)))
                    cnt += 1
                except Exception:
                    pass


            print(target ,"we have {} pictures".format(cnt))