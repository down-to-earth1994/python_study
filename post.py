import json,urllib2
textmod={
   "extractResultType": 1,
   "id": 278074888927973376,
   "rawvideoUrl": "https://dev.nzb.yunzujia.com.cn/identify/file/temp/20190416/278074888927973376.mp4",
   "resultMsg": "123",
   "resultType": 0,
   "videoClass": 0,
   "videoDuration": "200",
   "videoFormat": "Mp4",
   "videoMd5": "GVJMNRCXLYARXISUIPTKYZGOFXND7CAV",
  "keyframesUrl": [
    "https://dev.nzb.yunzujia.com.cn/identify/file/temp/20190416/278078621812396032.jpeg?740x300"
  ],
  "logoframesUrl": [
    "https://dev.nzb.yunzujia.com.cn/identify/file/temp/20190416/278078621812396032.jpeg?740x300"
  ],
  "peopleframesUrl": [
    "https://dev.nzb.yunzujia.com.cn/identify/file/temp/20190416/278078621812396032.jpeg?740x300"
  ],
  "rareframesUrl": [
    "https://dev.nzb.yunzujia.com.cn/identify/file/temp/20190416/278078621812396032.jpeg?740x300"
  ],
  "sceneframesUrl": [
    "https://dev.nzb.yunzujia.com.cn/identify/file/temp/20190416/278078621812396032.jpeg?740x300"
  ],
   "videoSize": 30
 }
textmod = json.dumps(textmod)
header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',"Content-Type": "application/json"}
url='https://dev.nzb.yunzujia.com.cn/identify/api/index/pars/complete'
req = urllib2.Request(url=url,data=textmod,headers=header_dict)
res = urllib2.urlopen(req)
res = res.read()
print(res)