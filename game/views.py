from django.http import HttpResponse

def index(request):
    line1 = '<h1 style="text-align:center;font-size:200%;">术士之战</h1>'
    line2 = '<div style="text-align:center;">'
    line3 = '<img src = "https://img0.baidu.com/it/u=2983326384,4126245808&fm=253&fmt=auto&app=138&f=JPEG?w=641&h=395">'
    line4 = '</div>'
    line5 = '<hr>'
    line6 = '<a href="/play/" style="font-size:300%">开始游戏</a>'

    return HttpResponse(line1 + line2 + line3 + line4 + line5 + line6)

def play(request):
    line1 = '<h1 style="text-align:center;font-size:200%;">游戏界面</h1>'
    line2 = '<div style="text-align:center;">'
    line3 = '<img src = "https://img2.baidu.com/it/u=2744751098,912601295&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=313">'
    line4 = '</div>'
    line5 = '<a href = "/" style="font-size:300%">返回菜单界面</a>'
    return HttpResponse(line1 + line2 + line3 + line4 + line5)

