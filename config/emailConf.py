import json
import requests
import TickerConfig

def sendEmail(msg):
    try:
        if TickerConfig.DINGDING_CONF["IS_DING_DING_CHAN"]:
            url=TickerConfig.DINGDING_CONF["ding_url"]
            HEADERS={"Content-Type":"application/json;charset=utf-8"}
            String_textMsg={"msgtype":"text","text":{"content":'恭喜，您已订票成功:'+msg}}
            String_textMsg=json.dumps(String_textMsg)
            res=requests.post(url,data=String_textMsg,headers=HEADERS)
            print(res.text)
            sendDingDingMsgResult=json.loads(res.text)
            if sendDingDingMsgResult['errcode']==0:
                print(u"钉钉已通知, 请查收")
            else:
                print(u"钉钉通知失败，失败原因:"+sendDingDingMsgResult['errmsg'])
    except Exception as e:
        print(u"钉钉配置有误{}".format(e))


if __name__ == '__main__':
    sendEmail("1")