# -*- coding: utf-8 -*-
# filename: handle.py
import reply
import receive
import hashlib
import web
import os
import imgfile
import time
import msgtemplate
import pymysql
import comparion
import unknown_face_dispose
cur_path = os.path.dirname(__file__)
session = {}
STATE_TIMEOUT = 180

class Handle(object):
    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "123"  # 请按照公众平台官网\基本配置中信息填写
            list1 = [token, timestamp, nonce]
            list1.sort()
            str_list1 = ''.join(list1)
            print(str_list1)
            sha1 = hashlib.sha1()
            sha1.update(str_list1.encode('utf-8'))
            hashcode = sha1.hexdigest()
            print("handle/GET func: hashcode, signature: ", hashcode, signature)
            if hashcode == signature:
                return echostr
            else:
                return ""
        except Exception as Argument:
            return Argument
    def POST(self):
        flag=False
        webData = web.data()
        #print ("Handle Post webdata is ", webData+'\n')
#后台打日志
        recMsg = receive.parse_xml(webData)
        if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
            #回复信息
            print('------------')
            toUser = recMsg.FromUserName
            print(type(toUser))
            fromUser = recMsg.ToUserName
            print(type(fromUser))
            fromContent = recMsg.Content
            print(type(fromContent))
            print('------------')
            toUser = recMsg.FromUserName
            fromUser = recMsg.ToUserName
            fromContent = recMsg.Content
            fromContent=fromContent.decode("utf8")
            print(type(fromContent))
            cur_time = int(time.time())
            print(session)
            content = "您输入的值为"+fromContent+",请您按要求操作"
            print(content)
            if toUser in session and 'state' in session[toUser] and cur_time < int(session[toUser]['time']):
                #判断fromContent是否合法
                if True and session[toUser]['state'] == 'train_add':
                    session[toUser]['id'] = fromContent
                    content = "请上传一张图片，进行建模"
            elif toUser in session and cur_time >= int(session[toUser]['time']):
                content = '上一个状态已经过期，您输入的值为'+fromContent
                del session[toUser]
            replyMsg = reply.TextMsg(toUser, fromUser, content)
            print(replyMsg)
            return replyMsg.send()
            
        elif isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'image':
            toUser = recMsg.FromUserName
            fromUser = recMsg.ToUserName
            cur_time = int(time.time())
            media_id = recMsg.MediaId
            print("session")
            print(session)
            if toUser in session and 'state' in session[toUser] and cur_time < int(session[toUser]['time']):

                if session[toUser]['state'] == 'verify':
                    if imgfile.save_img(os.path.join(cur_path,'unknown_face'),'1.jpg',media_id):
                        content = "图片上传成功，请等待考勤结果！"
                        flag=True
                        #unknown_face_dispose.dispose()
                        #comparion.comparison("201818810001")
                        if toUser in session:
                            del session[toUser]

                        replyMsg = reply.TextMsg(toUser, fromUser, content)
                        #print(replyMsg)
                        #return "success"
                        return replyMsg.send()
            return "success"
            
        elif isinstance(recMsg,receive.Msg) and recMsg.MsgType == 'event':
            toUser = recMsg.FromUserName
            fromUser = recMsg.ToUserName
            event = recMsg.Event
            print(toUser)
            db = pymysql.connect(host="localhost",
                                 user="root",
                                 password="19951208",
                                 db="face_recognition",
                                 port=3306,
                                 charset='utf8')
            cursor = db.cursor()
            sql = "SELECT t_wx FROM teacher"
            print(sql)
            try:
                cursor.execute(sql)
                results = cursor.fetchall()
            except:
                print("error")
            db.close()
            count=False
            for row in results:
                print(row[0])
                if toUser==row[0]:
                    count=True
                    break
            if count:
                    if event == 'CLICK':
                        eventKey = recMsg.EventKey
                        session[toUser] = {}
                        session[toUser]['state'] = eventKey
                        session[toUser]['time'] = str(int(time.time()) + STATE_TIMEOUT)
                        if eventKey == 'verify':
                            content = "请上传本次考勤的照片"
                            replyMsg = reply.TextMsg(toUser, fromUser, content)
                            return replyMsg.send()
                        # 调用主动推送接口
                        """
                        elif eventKey == 'msg_send':
                            toUser = 'otU-o0SMpY9Kxwww6pjLQ0V5JRSM'
                            msg_dict = {}
                            msg_dict['student_id'] = '2014122920'
                            msg_dict['course'] = '高等数学一'
                            day = msg_dict['day'] = '2018-04-08'
                            msg_dict['time'] = '3:00pm-4:00pm'
                            grade = msg_dict['grade'] = '网络141'
                            room = msg_dict['room'] = 'J104'
                            teacher = msg_dict['teacher'] = 'XX'
                            msgtemplate.send_msg(toUser,msg_dict)
                      """
                    print("success")
                    return "success"
            else:
                content="您没有在后台注册，请联系管理员注册后使用本公众号"
                replyMsg=reply.TextMsg(toUser,fromUser,content)
                return replyMsg.send()






