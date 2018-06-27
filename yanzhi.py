import itchat
from itchat.content import *
from aip import AipFace
import json
import base64
from urllib import parse



APP_ID = "11427368"
API_KEY = "0yF8YaIH7dLmmZd5Y7h1ufyB"
SECRET_KEY	='riisuqlvDMD8c75b4UhUdzbCU9CwMF8K'
client = AipFace(APP_ID, API_KEY, SECRET_KEY)








@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg.download(msg.fileName)
    image = msg.fileName
    itchat.send('@%s@%s' % (
        'img' if msg['Type'] == 'Picture' else 'fil', msg['FileName']),
        msg['FromUserName'])
    return '%s received' % msg['Type']



def image_to_base64(image_path):
    image_data = open(image_path, "rb")
    temp = image_data.read()
    base64_data = base64.b64encode(temp)
    image_data.close()
    data_string = str(base64_data)
    # print (data_string)
    data_string = data_string.strip('\'b')
    # print (data_string)
    return data_string




@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def tupianming(msg):
	msg.download(msg.fileName)
	image = msg.fileName
	image10 = image_to_base64(image)
	imageType = "BASE64"
	options = {"face_field": "age,beauty,type","max_face_num" :10}
	max_face_num = 10
	r = client.detect(image10, imageType, options)
	print (r)
	for o in r:
		cuowu = r["error_msg"]
	# cuowu = {}
	# cuowu = r["error_msg"]
	print (cuowu)

	# print (cuowu)
	if cuowu == 'pic not has face':
	 	mags ="请发送带有人脸的照片"
	 	itchat.send(mags
         ,
         msg['FromUserName'])

	elif cuowu == "SUCCESS":
		z =r['result']['face_list']

		s = z[0]
		b = s['beauty']
		age = s["age"]

		if len(z)>3:
			mags = "暂时只支持4个以下人脸"

		elif len(z)==1:

			mags = "您的颜值分为" + str(b)+","+"您的年龄为"+str(age)

		elif len(z)==2:
			s2 = z[1]
			b2 = s2['beauty']
			age2 = s2["age"]

			mags = "第一个颜值分为" + str(b)+","+"第一个年龄为"+str(age)+ "第二个颜值分为"+ str(b2)+","+"第二个年龄为"+str(age2)+"(顺序依次为从左往右)"

		else :
			s2 = z[1]
			b2 = s2['beauty']
			age2 = s2["age"]
			s3 = z[2]
			b3 = s3['beauty']
			age3 = s3["age"]
			mags = "第一个颜值分为" + str(b)+","+"第一个年龄为"+str(age)+ "第二个颜值分为"+ str(b2)+","+"第二个年龄为"+str(age2)+","+ "第三个颜值分为"+ str(b3)+","+"第三个年龄为"+str(age3)+"(顺序依次为从左往右)"


	itchat.send(str(mags),msg['FromUserName'])
		
			

# @itchat.msg_register([PICTURE,TEXT], isGroupChat=True)
# def text_reply(msg):
# 	xiaoxi = {}
# 	xiaoxi = msg['TEXT']
# 	print (xiaoxi)
    
	# if msg['TEXT']	== '@节奏大师 打分' :
	# 	itchat.send_msg("我已经收到了来自{0}的请求，请发送你的照片".format(msg['ActualNickName']),toUserName=msg['FromUserName'])
	# 	if msg.fileName:
	# 		msg.download(msg.fileName)
	# 		image = msg.fileName
	# 		image10 = image_to_base64(image)
	# 		imageType = "BASE64"
	# 		options = {"face_field": "age,beauty,type","max_face_num" :10}
	# 		max_face_num = 10
	# 		r = client.detect(image10, imageType, options)
	# 		print (r)
	# 		for o in r:
	# 			cuowu = r["error_msg"]
	# 		# cuowu = {}
	# 		# cuowu = r["error_msg"]
	# 		print (cuowu)

	# 		# print (cuowu)
	# 		if cuowu == 'pic not has face':
	# 			mags ="请发送带有人脸的照片"
	# 			itchat.send(mags
	# 			 ,
	# 			 msg['FromUserName'])

	# 		elif cuowu == "SUCCESS":
	# 			z =r['result']['face_list']

	# 			s = z[0]
	# 			b = s['beauty']
	# 			age = s["age"]

	# 			if len(z)>3:
	# 				mags = "暂时只支持4个以下人脸"

	# 			elif len(z)==1:

	# 				mags = "您的颜值分为" + str(b)+","+"您的年龄为"+str(age)

	# 			elif len(z)==2:
	# 				s2 = z[1]
	# 				b2 = s2['beauty']
	# 				age2 = s2["age"]

	# 				mags = "第一个颜值分为" + str(b)+","+"第一个年龄为"+str(age)+ "第二个颜值分为"+ str(b2)+","+"第二个年龄为"+str(age2)+"(顺序依次为从左往右)"

	# 			else :
	# 				s2 = z[1]
	# 				b2 = s2['beauty']
	# 				age2 = s2["age"]
	# 				s3 = z[2]
	# 				b3 = s3['beauty']
	# 				age3 = s3["age"]
	# 				mags = "第一个颜值分为" + str(b)+","+"第一个年龄为"+str(age)+ "第二个颜值分为"+ str(b2)+","+"第二个年龄为"+str(age2)+","+ "第三个颜值分为"+ str(b3)+","+"第三个年龄为"+str(age3)+"(顺序依次为从左往右)"

	# 		itchat.send(mags)




# options = {"face_field": "age,beauty"}


# r = client.detect(image10, imageType, options)
# print (r)


itchat.auto_login()
itchat.run()



