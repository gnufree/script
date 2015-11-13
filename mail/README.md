定制个性化的邮件格式方法
MEME(Multipurpost Internet Mail Extensions,多用途互联网邮件拓展)
Python 中常用的MIME实现类:
email.mime.multipart.MIMEMultipart([_subtype[,boundary[,_subparts[,_params]]]]),作用是生成包含多个部分的邮件体的MIME对象，参数_subtype指定要添加到"Content-type:multipart/subtype"报头可选的三种子类型,分别为mixed,related,alternative，默认值为mixed。
mixed  定义一个带附件的邮件体；
related  定义一个内嵌资源的邮件体；
alternative 定义一个构建文本与超文本共存的邮件体
email.mime.audio.MIMEAudio(_audiodata[,_subtype[,_encoder[,**_params]]]),创建包含音频数据的邮件体
email.mime.image.MIMEImage(_imagedata[,_subtype[,_encoder[,**_params]]]), 创建包含图片数据的邮件体
email.mime.text.MIMEText(_text[,_subtype[,_charset]], 创建包含文本数据的邮件体
